from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre de Categoría")
    icon = models.CharField(max_length=50, default="📚", verbose_name="Icono / Emoji")
    description = models.TextField(blank=True, verbose_name="Descripción")
    order = models.PositiveIntegerField(default=0, verbose_name="Orden de visualización")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.icon} {self.name}"


class FAQ(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="faqs", verbose_name="Categoría"
    )
    question = models.CharField(max_length=255, verbose_name="Pregunta Frecuente")
    answer = models.TextField(
        verbose_name="Respuesta (Soporta Markdown y saltos de línea)",
        help_text="Explica detalladamente la respuesta oficial de la universidad."
    )
    keywords = models.TextField(
        blank=True,
        verbose_name="Palabras clave / Sinónimos",
        help_text="Palabras separadas por comas (ej. matrícula, matricula, inscripcion, fechas, cuando me matriculo)"
    )
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    priority = models.IntegerField(default=0, verbose_name="Prioridad en búsquedas (Mayor = más relevante)")
    view_count = models.PositiveIntegerField(default=0, verbose_name="Consultas registradas")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")

    class Meta:
        verbose_name = "Pregunta y Respuesta (FAQ)"
        verbose_name_plural = "Preguntas y Respuestas (FAQs)"
        ordering = ['-priority', '-view_count', 'question']

    def __str__(self):
        return self.question


class AcademicCalendar(models.Model):
    EVENT_TYPES = [
        ('matricula', 'Matrícula / Inscripciones'),
        ('clases', 'Inicio / Fin de Clases'),
        ('examenes', 'Exámenes Parciales / Finales'),
        ('tramites', 'Plazo de Trámites (Retiros, Reservas)'),
        ('feriado', 'Feriado / Receso Académico'),
        ('otro', 'Otro Evento'),
    ]

    title = models.CharField(max_length=200, verbose_name="Título del Evento")
    period = models.CharField(max_length=20, default="2026-I", verbose_name="Periodo Académico (ej. 2026-I)")
    event_type = models.CharField(max_length=30, choices=EVENT_TYPES, default='matricula', verbose_name="Tipo de Evento")
    start_date = models.DateField(verbose_name="Fecha de Inicio")
    end_date = models.DateField(null=True, blank=True, verbose_name="Fecha de Fin (Opcional)")
    description = models.TextField(blank=True, verbose_name="Detalles o Instrucciones")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Fecha de Calendario Académico"
        verbose_name_plural = "Calendario Académico"
        ordering = ['start_date']

    def __str__(self):
        date_str = self.start_date.strftime('%d/%m/%Y')
        if self.end_date and self.end_date != self.start_date:
            date_str += f" al {self.end_date.strftime('%d/%m/%Y')}"
        return f"[{self.period}] {self.title} ({date_str})"


class CourseSchedule(models.Model):
    course_code = models.CharField(max_length=20, verbose_name="Código del Curso (ej. MAT-101)")
    course_name = models.CharField(max_length=150, verbose_name="Nombre del Curso")
    section = models.CharField(max_length=20, default="SEC-01", verbose_name="Sección / Grupo")
    professor = models.CharField(max_length=120, verbose_name="Docente a Cargo")
    days_and_time = models.CharField(
        max_length=120, verbose_name="Días y Horarios", help_text="ej. Lun y Mié 08:00 - 10:00"
    )
    classroom = models.CharField(max_length=80, verbose_name="Aula / Laboratorio", help_text="ej. Pabellón B - Aula 302")
    credits = models.PositiveIntegerField(default=4, verbose_name="Créditos")
    period = models.CharField(max_length=20, default="2026-I", verbose_name="Periodo Académico")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Horario de Curso"
        verbose_name_plural = "Horarios de Cursos"
        ordering = ['course_code', 'section']

    def __str__(self):
        return f"{self.course_code} - {self.course_name} ({self.section})"


class Procedure(models.Model):
    name = models.CharField(max_length=150, verbose_name="Nombre del Trámite")
    cost = models.CharField(max_length=50, default="Gratuito", verbose_name="Costo / Tasa")
    processing_time = models.CharField(max_length=80, default="3 a 5 días hábiles", verbose_name="Tiempo de Atención")
    requirements = models.TextField(verbose_name="Requisitos indispensables")
    steps = models.TextField(verbose_name="Pasos a seguir")
    portal_link = models.URLField(blank=True, verbose_name="Enlace al Portal de Trámites")
    is_active = models.BooleanField(default=True, verbose_name="Activo")

    class Meta:
        verbose_name = "Trámite Estudiantil"
        verbose_name_plural = "Trámites Estudiantiles"
        ordering = ['name']

    def __str__(self):
        return self.name


class BotConfig(models.Model):
    PROVIDER_CHOICES = [
        ('local_nlp', 'Motor NLP Local (100% Offline / Cero Costo / TF-IDF + Embeddings)'),
        ('ollama', 'Ollama Local (LLM Llama 3.2 / Mistral On-Premise)'),
        ('gemini', 'Google Gemini API (Cloud)'),
    ]

    university_name = models.CharField(
        max_length=150, default="Universidad Nacional Demo", verbose_name="Nombre de la Institución"
    )
    bot_name = models.CharField(max_length=80, default="UniBot Asistente", verbose_name="Nombre del Asistente")
    welcome_message = models.TextField(
        default="¡Hola! 👋 Soy el asistente virtual de la universidad. Puedo ayudarte con fechas de matrícula, horarios de cursos, trámites y reglamentos. ¿En qué puedo orientarte hoy?",
        verbose_name="Mensaje de Bienvenida"
    )
    fallback_message = models.TextField(
        default="Disculpa, no encontré información exacta para tu consulta. Te sugiero revisar las opciones frecuentes o acercarte a la Oficina de Asuntos Académicos.",
        verbose_name="Mensaje cuando no encuentra respuesta"
    )
    ai_provider = models.CharField(
        max_length=20, choices=PROVIDER_CHOICES, default='local_nlp', verbose_name="Motor de IA Activo"
    )
    ollama_model = models.CharField(
        max_length=60, default="llama3.2", verbose_name="Modelo Ollama (si está activo)", help_text="ej. llama3.2, mistral, gemma2"
    )
    confidence_threshold = models.FloatField(
        default=0.25, verbose_name="Umbral mínimo de confianza (0.0 a 1.0)", help_text="Mínima similitud para dar una respuesta directa"
    )

    class Meta:
        verbose_name = "Configuración del Asistente Virtual"
        verbose_name_plural = "Configuración del Asistente Virtual"

    def __str__(self):
        return f"Configuración: {self.bot_name} ({self.get_ai_provider_display()})"

    @classmethod
    def get_settings(cls):
        config, _ = cls.objects.get_or_create(id=1)
        return config


class ChatSession(models.Model):
    session_id = models.CharField(max_length=64, unique=True, verbose_name="ID de Sesión")
    user_ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP del Alumno")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Inicio")
    last_activity = models.DateTimeField(auto_now=True, verbose_name="Última Actividad")

    class Meta:
        verbose_name = "Sesión de Chat"
        verbose_name_plural = "Sesiones de Chat"
        ordering = ['-created_at']

    def __str__(self):
        return f"Sesión {self.session_id[:8]}... ({self.created_at.strftime('%d/%m %H:%M')})"


class ChatMessage(models.Model):
    SENDER_CHOICES = [
        ('user', 'Alumno'),
        ('bot', 'UniBot'),
    ]

    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages", verbose_name="Sesión")
    sender = models.CharField(max_length=10, choices=SENDER_CHOICES, verbose_name="Emisor")
    message = models.TextField(verbose_name="Mensaje")
    matched_faq = models.ForeignKey(FAQ, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="FAQ Coincidente")
    confidence_score = models.FloatField(default=0.0, verbose_name="Nivel de Confianza (ML)")
    feedback = models.SmallIntegerField(
        choices=[(1, 'Útil 👍'), (-1, 'No útil 👎'), (0, 'Sin valorar')],
        default=0,
        verbose_name="Feedback del Alumno"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora")

    class Meta:
        verbose_name = "Historial de Mensaje"
        verbose_name_plural = "Historial de Mensajes"
        ordering = ['created_at']

    def __str__(self):
        return f"[{self.get_sender_display()}] {self.message[:40]}..."
