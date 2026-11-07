# 🎓 Asistente Virtual Universitario (NLP / Machine Learning On-Premise)

Sistema completo de atención al estudiante mediante Inteligencia Artificial y Machine Learning local, con panel administrativo en **Django** y widget de chat embebible en **JavaScript puro (Shadow DOM)**.

---

## 🌟 Características Principales

1. **Costo $0.00 USD (100% Local / On-Premise):** No requiere pagos de APIs externas ni suscripciones en la nube.
2. **Motor de IA / NLP Híbrido:**
   - Vectorización con **TF-IDF y N-Grams** (`scikit-learn`).
   - Similitud semántica de Coseno + Boosting por entidades (Cursos, Docentes, Trámites, Fechas).
   - Conector plug-and-play para **Ollama (Llama 3.2 / Mistral)** si deseas RAG generativo con LLMs locales.
3. **Panel Administrativo (Django Admin):**
   - Gestión de Preguntas Frecuentes (FAQs), Categorías y Palabras clave.
   - Administración del Calendario Académico y Fechas de Matrícula.
   - Horarios de Cursos, Secciones, Docentes y Aulas.
   - Trámites Estudiantiles, Requisitos y Costos.
   - Historial de Conversaciones, Nivel de Confianza y Calificaciones (👍 / 👎).
   - Botón de **Reindexación del Motor NLP** en tiempo real.
4. **Widget de Chat Embebible (`chat-widget.js`):**
   - Desarrollado en **Vanilla JavaScript** con **Shadow DOM** (cero conflictos de CSS).
   - Renderizado automático de Markdown, Tablas de horarios, Listas y Enlaces.
   - Chips dinámicos de preguntas sugeridas.
   - Indicador de escritura animado y feedback interactivo.

---

## 🚀 Cómo Iniciar el Proyecto

### 1. Activar el Entorno Virtual
```bash
source .venv/bin/activate
```

### 2. Iniciar el Servidor Django
```bash
python manage.py runserver 0.0.0.0:8000
```

### 3. Accesos y Demostración
- 🌐 **Portal del Estudiante (Demo con Widget Embebido):** [http://localhost:8000/](http://localhost:8000/)
- ⚙️ **Panel de Administración Django:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
  - **Usuario:** `admin`
  - **Contraseña:** `admin123`
- 📡 **Endpoint API REST de Chat:** `POST http://localhost:8000/api/chat/`

---

## 📦 Cómo Embeber el Widget en Cualquier Sitio Web

Para integrar el chatbot en cualquier página HTML, portal de la universidad, WordPress o intranet, solo incluye esta etiqueta al final del `<body>`:

```html
<script src="http://localhost:8000/static/widget/chat-widget.js" defer></script>
```

---

## 📂 Estructura del Código

```
├── config/                      # Configuración principal de Django (settings, urls, wsgi)
├── knowledge_base/              # Módulo de Conocimiento Universitario y NLP
│   ├── models.py                # Modelos (FAQ, Calendario, Cursos, Trámites, Logs)
│   ├── ml_engine.py             # Motor de Machine Learning / NLP Local (Scikit-Learn + TF-IDF + Ollama)
│   ├── admin.py                 # Configuración avanzada del panel Django Admin
│   └── management/commands/     # Comando seed_demo_data para poblar datos de prueba
├── chat_api/                    # API REST (Endpoints para chat, feedback, configuración)
├── static/widget/               # Widget de JavaScript embebible (chat-widget.js)
├── templates/                   # Plantilla HTML del Portal Universitario de demostración
└── requirements.txt             # Dependencias del proyecto
```

---

## 🤖 Integración Opcional con Ollama (LLM Local)

Si en el futuro deseas que un modelo de lenguaje como **Llama 3.2** o **Mistral** redacte las respuestas en lenguaje natural:
1. Instala Ollama y descarga un modelo:
   ```bash
   ollama run llama3.2
   ```
2. En el panel de Django Admin (`/admin/`), ve a **Configuración del Asistente Virtual** y cambia el motor activo a `Ollama Local`.
