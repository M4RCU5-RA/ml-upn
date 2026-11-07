import re
import unicodedata
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import requests
from django.db import DatabaseError, OperationalError


def normalize_text(text: str) -> str:
    """Normaliza texto eliminando tildes, caracteres especiales y convirtiendo a minúsculas."""
    if not text:
        return ""
    text = text.lower()
    text = text.replace('ñ', '###N_TILDE###')
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = text.replace('###N_TILDE###', 'ñ')
    text = re.sub(r'[^\w\s]', ' ', text)
    return ' '.join(text.split())


# Palabras de parada comunes en español para no ponderar en coincidencias de títulos
SPANISH_STOPWORDS = {
    'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'de', 'del', 'a', 'al', 'en', 'para',
    'por', 'con', 'sin', 'sobre', 'y', 'e', 'o', 'u', 'que', 'es', 'son', 'como', 'cual', 'cuales',
    'cuando', 'donde', 'quien', 'quienes', 'cuanto', 'cuantos', 'cuanta', 'cuantas', 'mi', 'mis',
    'tu', 'tus', 'su', 'sus', 'me', 'se', 'este', 'esta', 'estos', 'estas', 'este', 'año', 'semestre'
}


class UniversityNLPEngine:
    """Motor de IA / NLP Local para Procesamiento de Lenguaje Natural en Consultas Universitarias."""

    def __init__(self):
        self.corpus_items = []
        self.vectorizer = None
        self.tfidf_matrix = None
        self._is_indexed = False

    def build_index(self):
        """Indexa todos los documentos de la base de conocimientos con manejo seguro de DB."""
        from .models import FAQ, AcademicCalendar, CourseSchedule, Procedure

        self.corpus_items = []
        texts = []

        try:
            # 1. Indexar FAQs
            for faq in FAQ.objects.filter(is_active=True).select_related('category'):
                search_doc = f"{faq.question} {faq.keywords} {faq.category.name} {faq.answer}"
                self.corpus_items.append({
                    'type': 'faq',
                    'object': faq,
                    'title': faq.question,
                    'keywords': faq.keywords,
                    'search_text': normalize_text(search_doc),
                    'priority_boost': 1.0 + (faq.priority * 0.05)
                })
                texts.append(normalize_text(search_doc))

            # 2. Indexar Calendario Académico
            for cal in AcademicCalendar.objects.filter(is_active=True):
                search_doc = f"fechas cronograma calendario cuando inicia cuando es {cal.title} {cal.get_event_type_display()} {cal.period} {cal.description}"
                self.corpus_items.append({
                    'type': 'calendar',
                    'object': cal,
                    'title': f"{cal.title} ({cal.period})",
                    'keywords': f"fecha fechas cronograma calendario {cal.title}",
                    'search_text': normalize_text(search_doc),
                    'priority_boost': 1.15
                })
                texts.append(normalize_text(search_doc))

            # 3. Indexar Horarios de Cursos
            for course in CourseSchedule.objects.filter(is_active=True):
                search_doc = f"horario curso materia asignatura clase profesor docente {course.course_code} {course.course_name} {course.section} {course.professor} {course.days_and_time} {course.classroom}"
                self.corpus_items.append({
                    'type': 'course',
                    'object': course,
                    'title': f"{course.course_code} - {course.course_name}",
                    'keywords': f"{course.course_name} {course.course_code} {course.professor} horario horarios curso clase",
                    'search_text': normalize_text(search_doc),
                    'priority_boost': 1.2
                })
                texts.append(normalize_text(search_doc))

            # 4. Indexar Trámites
            for proc in Procedure.objects.filter(is_active=True):
                search_doc = f"tramite solicitud como solicitar como hacer como realizar requisito costo pasos {proc.name} {proc.requirements} {proc.steps}"
                self.corpus_items.append({
                    'type': 'procedure',
                    'object': proc,
                    'title': proc.name,
                    'keywords': f"tramite solicitud requisitos como solicitar {proc.name}",
                    'search_text': normalize_text(search_doc),
                    'priority_boost': 1.2
                })
                texts.append(normalize_text(search_doc))

            if texts:
                self.vectorizer = TfidfVectorizer(
                    ngram_range=(1, 3),
                    min_df=1,
                    sublinear_tf=True
                )
                self.tfidf_matrix = self.vectorizer.fit_transform(texts)
                self._is_indexed = True
            else:
                self.vectorizer = None
                self.tfidf_matrix = None
                self._is_indexed = True

        except (DatabaseError, OperationalError, Exception):
            self.vectorizer = None
            self.tfidf_matrix = None
            self._is_indexed = False

    def search(self, query: str, top_k: int = 4):
        """Calcula la similitud semántica y coincidencia léxica para ranking de alta precisión."""
        if not self._is_indexed or not self.vectorizer or self.tfidf_matrix is None:
            self.build_index()
            if not self.vectorizer or self.tfidf_matrix is None:
                return []

        norm_query = normalize_text(query)
        if not norm_query:
            return []

        query_tokens = [w for w in norm_query.split() if w not in SPANISH_STOPWORDS and len(w) > 2]
        query_vec = self.vectorizer.transform([norm_query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix)[0]

        boosted_scores = []
        for i, tfidf_score in enumerate(similarities):
            item = self.corpus_items[i]
            title_norm = normalize_text(item['title'])
            keywords_norm = normalize_text(item.get('keywords', ''))
            
            # Coincidencias de tokens clave en el título y palabras clave
            keyword_match_count = 0
            for token in query_tokens:
                if token in title_norm:
                    keyword_match_count += 1.5
                elif token in keywords_norm:
                    keyword_match_count += 0.8

            # Bonus si es pregunta de horario y coincide el curso
            bonus = 0.0
            if item['type'] == 'course':
                course_obj = item['object']
                course_name_norm = normalize_text(course_obj.course_name)
                # Si el nombre del curso está en la consulta (ej. 'calculo', 'algoritmos', 'fisica')
                if any(w in norm_query for w in course_name_norm.split() if len(w) > 3):
                    bonus += 0.4
                if course_obj.course_code.lower() in norm_query:
                    bonus += 0.6

            elif item['type'] == 'procedure':
                proc_name_norm = normalize_text(item['object'].name)
                if any(w in norm_query for w in proc_name_norm.split() if len(w) > 3 and w not in ['curso', 'asignatura']):
                    bonus += 0.35

            elif item['type'] == 'calendar':
                if any(w in norm_query for w in ['fecha', 'fechas', 'cuando', 'cronograma', 'calendario', 'inicio', 'plazo']):
                    bonus += 0.25

            final_score = (tfidf_score * item['priority_boost']) + (keyword_match_count * 0.12) + bonus
            boosted_scores.append((final_score, item))

        boosted_scores.sort(key=lambda x: x[0], reverse=True)
        return [(score, item) for score, item in boosted_scores[:top_k] if score > 0.08]

    def answer_query(self, user_query: str):
        """Genera la respuesta más apropiada para el estudiante."""
        from .models import BotConfig
        config = BotConfig.get_settings()
        matches = self.search(user_query, top_k=4)

        if not matches or matches[0][0] < config.confidence_threshold:
            suggestions = [
                "¿Cuándo son las fechas de matrícula?",
                "¿Cuáles son los horarios de Cálculo?",
                "¿Cómo solicitar retiro de curso?",
                "¿Cuáles son las formas de pago de pensión?"
            ]
            return {
                'answer': config.fallback_message,
                'confidence': float(matches[0][0]) if matches else 0.0,
                'source_type': 'fallback',
                'matched_faq_id': None,
                'suggestions': suggestions
            }

        top_score, top_item = matches[0]
        item_type = top_item['type']
        obj = top_item['object']

        if config.ai_provider == 'ollama':
            ollama_ans = self._query_ollama(user_query, matches, config)
            if ollama_ans:
                return {
                    'answer': ollama_ans,
                    'confidence': float(top_score),
                    'source_type': 'ollama_rag',
                    'matched_faq_id': obj.id if item_type == 'faq' else None,
                    'suggestions': self._generate_suggestions(item_type, obj)
                }

        formatted_answer, matched_faq_id = self._format_local_response(item_type, obj, user_query, matches)
        suggestions = self._generate_suggestions(item_type, obj)

        return {
            'answer': formatted_answer,
            'confidence': round(float(top_score), 4),
            'source_type': item_type,
            'matched_faq_id': matched_faq_id,
            'suggestions': suggestions
        }

    def _format_local_response(self, item_type: str, obj, user_query: str, all_matches: list):
        """Formatea las respuestas locales con Markdown amigable."""
        matched_faq_id = None
        from .models import CourseSchedule

        if item_type == 'faq':
            matched_faq_id = obj.id
            obj.view_count += 1
            obj.save(update_fields=['view_count'])
            return obj.answer, matched_faq_id

        elif item_type == 'calendar':
            date_info = obj.start_date.strftime('%d/%m/%Y')
            if obj.end_date and obj.end_date != obj.start_date:
                date_info += f" hasta el {obj.end_date.strftime('%d/%m/%Y')}"

            answer = (
                f"### 📅 **{obj.title}** ({obj.period})\n\n"
                f"• **Fecha oficial:** {date_info}\n"
                f"• **Tipo de evento:** {obj.get_event_type_display()}\n\n"
                f"{obj.description}\n\n"
                f"💡 *Recuerda verificar tu estado de matrícula y deudas en el portal del estudiante antes de esta fecha.*"
            )
            return answer, None

        elif item_type == 'course':
            related_courses = CourseSchedule.objects.filter(
                is_active=True,
                course_name__icontains=obj.course_name
            )
            
            lines = [f"### 📖 **Horarios disponibles: {obj.course_name} ({obj.course_code})**\n"]
            lines.append(f"**Créditos:** {obj.credits} | **Periodo:** {obj.period}\n")
            lines.append("| Sección | Docente | Horario | Aula |")
            lines.append("| :--- | :--- | :--- | :--- |")

            for c in related_courses:
                lines.append(f"| **{c.section}** | {c.professor} | {c.days_and_time} | {c.classroom} |")

            lines.append("\n📌 *Nota: La asignación final de aula puede variar según la capacidad de aforo.*")
            return "\n".join(lines), None

        elif item_type == 'procedure':
            answer = (
                f"### 📋 **Trámite: {obj.name}**\n\n"
                f"• **Costo de trámite:** `{obj.cost}`\n"
                f"• **Tiempo estimado:** {obj.processing_time}\n\n"
                f"#### **📌 Requisitos:**\n{obj.requirements}\n\n"
                f"#### **🚀 Pasos a seguir:**\n{obj.steps}\n"
            )
            if obj.portal_link:
                answer += f"\n🔗 [Ingresar al Portal de Trámites]({obj.portal_link})"
            return answer, None

        return "Información encontrada en la base universitaria.", None

    def _generate_suggestions(self, item_type: str, obj):
        """Genera preguntas sugeridas relacionadas dinámicamente."""
        from .models import FAQ

        if item_type == 'faq':
            related = FAQ.objects.filter(category=obj.category, is_active=True).exclude(id=obj.id)[:3]
            if related.exists():
                return [f.question for f in related]

        elif item_type == 'calendar':
            return [
                "¿Cuáles son los requisitos de matrícula?",
                "¿Cómo solicitar reserva de matrícula?",
                "¿Dónde veo mis horarios de clases?"
            ]

        elif item_type == 'course':
            return [
                "¿Cuándo es la fecha límite para retiro de curso?",
                "¿Cuántos créditos máximos puedo matricular?",
                "¿Dónde consulto los datos de mi docente?"
            ]

        elif item_type == 'procedure':
            return [
                "¿Cuáles son las formas de pago?",
                "¿Cómo solicitar certificado de estudios?",
                "¿Dónde contactar a Mesa de Partes?"
            ]

        return [
            "¿Cuándo inicia el periodo de matrícula?",
            "¿Cómo solicitar carné universitario?",
            "¿Cuáles son los horarios de atención de biblioteca?"
        ]

    def _query_ollama(self, user_query: str, matches: list, config):
        """Consulta RAG a Ollama si el servicio está corriendo localmente."""
        try:
            context_docs = []
            for _, item in matches:
                context_docs.append(f"Documento: {item['title']}\nContenido: {item['search_text']}")

            prompt = (
                f"Eres {config.bot_name}, el asistente oficial de {config.university_name}.\n"
                f"Usa exclusivamente el siguiente contexto universitario para responder en español de forma concisa, educada y clara al estudiante.\n\n"
                f"--- CONTEXTO ---\n" + "\n\n".join(context_docs) + "\n\n"
                f"--- PREGUNTA DEL ESTUDIANTE ---\n{user_query}\n\n"
                f"--- RESPUESTA ---"
            )

            res = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": config.ollama_model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=8
            )
            if res.status_code == 200:
                return res.json().get('response', '')
        except Exception:
            pass
        return None


# Instancia singleton del motor NLP
nlp_engine = UniversityNLPEngine()
