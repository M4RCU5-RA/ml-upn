from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from datetime import date
from knowledge_base.models import (
    Category, FAQ, AcademicCalendar, CourseSchedule, Procedure, BotConfig
)
from knowledge_base.ml_engine import nlp_engine


class Command(BaseCommand):
    help = "Puebla la base de datos con información universitaria ficticia de demostración y crea superusuario admin."

    def handle(self, *args, **options):
        self.stdout.write("🚀 Iniciando carga de datos de demostración...")

        # 1. Crear Superusuario para Django Admin
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser("admin", "admin@universidad.edu.pe", "admin123")
            self.stdout.write(self.style.SUCCESS("👤 Superusuario creado: Usuario 'admin' / Contraseña 'admin123'"))
        else:
            self.stdout.write("👤 Superusuario 'admin' ya existía.")

        # 2. Configuración del Bot
        config = BotConfig.get_settings()
        config.university_name = "Universidad Nacional San Agustín de Demo"
        config.bot_name = "UniBot Asistente"
        config.welcome_message = (
            "¡Hola! 👋 Soy UniBot, tu asistente académico universitario. "
            "Puedo ayudarte a consultar fechas de matrícula, horarios de cursos, procedimientos de trámites, pagos y mucho más. "
            "¿Qué consulta tienes hoy?"
        )
        config.ai_provider = "local_nlp"
        config.confidence_threshold = 0.15
        config.save()

        # 3. Categorías
        cat_matr, _ = Category.objects.get_or_create(
            name="Matrículas e Inscripciones",
            defaults={"icon": "📝", "order": 1, "description": "Todo sobre procesos de matrícula, cronogramas y requisitos."}
        )
        cat_cursos, _ = Category.objects.get_or_create(
            name="Cursos y Horarios",
            defaults={"icon": "📚", "order": 2, "description": "Consultas de asignaturas, secciones, docentes y aulas."}
        )
        cat_tramites, _ = Category.objects.get_or_create(
            name="Trámites y Certificados",
            defaults={"icon": "📄", "order": 3, "description": "Retiros, reservas, certificados de estudios y carnés."}
        )
        cat_pagos, _ = Category.objects.get_or_create(
            name="Pagos y Pensiones",
            defaults={"icon": "💳", "order": 4, "description": "Fechas de cuotas, números de cuenta y métodos de pago."}
        )
        cat_servicios, _ = Category.objects.get_or_create(
            name="Servicios Universitarios",
            defaults={"icon": "🏛️", "order": 5, "description": "Biblioteca, comedor, tópico de salud y orientación psicológica."}
        )

        # 4. FAQs
        faqs_data = [
            {
                "category": cat_matr,
                "question": "¿Cuáles son los requisitos para la matrícula del semestre 2026-I?",
                "keywords": "requisitos matricula matricularme estar al dia deudas requisitos academicos",
                "priority": 5,
                "answer": (
                    "Para realizar tu matrícula regular en el periodo 2026-I debes cumplir con los siguientes requisitos:\n\n"
                    "1. **No registrar deudas pendientes** de pensiones o biblioteca del semestre anterior.\n"
                    "2. **Haber completado la encuesta docente** en el portal del estudiante.\n"
                    "3. **Tener habilitado el turno de matrícula** según tu promedio ponderado.\n"
                    "4. Respetar los prerrequisitos de cada curso según tu malla curricular."
                )
            },
            {
                "category": cat_matr,
                "question": "¿Cuántos créditos puedo matricular como máximo?",
                "keywords": "limite creditos maximo creditos cuantos creditos puedo llevar ampliacion",
                "priority": 4,
                "answer": (
                    "El límite estándar de créditos por semestre es de **22 créditos**.\n\n"
                    "• Si tu promedio del semestre anterior es **mayor a 15.00**, puedes solicitar ampliación hasta **26 créditos** mediante solicitud web.\n"
                    "• En caso de estar en condición de riesgo o tercera matrícula, el límite es de **12 créditos**."
                )
            },
            {
                "category": cat_pagos,
                "question": "¿Dónde y cómo puedo pagar mi pensión y matrícula?",
                "keywords": "pagar pension como pagar cuentas bancarias bcp bbva interbank pago cuota",
                "priority": 5,
                "answer": (
                    "Puedes pagar tus pensiones y trámites en los siguientes canales oficiales indicando tu **Código de Estudiante**:\n\n"
                    "• **Banca por Internet / App Móvil:** BCP, BBVA, Interbank y Scotiabank (buscar *Universidad Nacional Demo - Pensiones*).\n"
                    "• **Agentes y Ventanillas:** Directamente en ventanilla bancaria presentando tu DNI/código.\n"
                    "• **Caja del Campus Central:** Pabellón Administrativo (Lunes a Viernes de 08:30 a 16:30 hrs)."
                )
            },
            {
                "category": cat_tramites,
                "question": "¿Cómo puedo tramitar el carné universitario?",
                "keywords": "carne carnet universitario tramite sunedu duplicado renovar",
                "priority": 3,
                "answer": (
                    "El carné universitario oficial se tramita de la siguiente forma:\n\n"
                    "1. Realiza el pago por derecho de carné (`S/. 16.00`) en caja o banca web.\n"
                    "2. Sube tu foto tamaño pasaporte con fondo blanco en formato JPG a tu intranet.\n"
                    "3. La universidad enviará el lote de emisión a la entidad reguladora (SUNEDU).\n"
                    "4. Tiempo de entrega aproximado: **20 a 30 días hábiles**."
                )
            },
            {
                "category": cat_servicios,
                "question": "¿Cuáles son los horarios de la Biblioteca Central y cómo acceder a los libros virtuales?",
                "keywords": "biblioteca libros sala de estudio horario biblioteca virtual bases de datos",
                "priority": 2,
                "answer": (
                    "### 📚 Biblioteca Central\n\n"
                    "• **Horario presencial:** Lunes a Viernes de 08:00 a 20:00 hrs | Sábados de 08:30 a 13:00 hrs.\n"
                    "• **Biblioteca Virtual:** Ingresa a `https://biblioteca.universidad.edu.pe` con tu correo institucional para acceder a IEEE Xplore, ScienceDirect, Scopus y libros digitales."
                )
            },
            {
                "category": cat_servicios,
                "question": "¿Qué servicios médicos y de apoyo psicológico ofrece la universidad?",
                "keywords": "topico medico psicologo salud bienestar atencion medica cita",
                "priority": 2,
                "answer": (
                    "La Dirección de Bienestar Universitario ofrece atención gratuita para alumnos matriculados:\n\n"
                    "• **Tópico Médico:** Pabellón C - 1er piso (Urgencias, medicina general y enfermería).\n"
                    "• **Consultorio Psicológico:** Citas presenciales y virtuales previa reserva en la intranet de Bienestar.\n"
                    "• **Seguro contra Accidentes:** Cobertura 24/7 durante el periodo académico activo."
                )
            }
        ]

        for item in faqs_data:
            faq, _ = FAQ.objects.get_or_create(
                question=item["question"],
                defaults={
                    "category": item["category"],
                    "keywords": item["keywords"],
                    "priority": item["priority"],
                    "answer": item["answer"],
                    "is_active": True
                }
            )

        # 5. Calendario Académico
        calendar_events = [
            {
                "title": "Matrícula Regular 2026-I",
                "period": "2026-I",
                "event_type": "matricula",
                "start_date": date(2026, 2, 16),
                "end_date": date(2026, 2, 27),
                "description": "Matrícula por internet según orden de mérito y turnos asignados en la intranet."
            },
            {
                "title": "Matrícula Extemporánea 2026-I",
                "period": "2026-I",
                "event_type": "matricula",
                "start_date": date(2026, 3, 2),
                "end_date": date(2026, 3, 6),
                "description": "Proceso con recargo administrativo para alumnos que no se matricularon en fecha regular."
            },
            {
                "title": "Inicio de Clases Semestre 2026-I",
                "period": "2026-I",
                "event_type": "clases",
                "start_date": date(2026, 3, 16),
                "end_date": date(2026, 3, 16),
                "description": "Inicio oficial de actividades lectivas para todas las facultades."
            },
            {
                "title": "Semana de Exámenes Parciales",
                "period": "2026-I",
                "event_type": "examenes",
                "start_date": date(2026, 5, 4),
                "end_date": date(2026, 5, 9),
                "description": "Suspensión de clases regulares durante la semana de evaluaciones parciales."
            },
            {
                "title": "Plazo Límite para Retiro de Cursos",
                "period": "2026-I",
                "event_type": "tramites",
                "start_date": date(2026, 5, 22),
                "end_date": date(2026, 5, 22),
                "description": "Último día para solicitar el retiro de una asignatura sin perjuicio académico."
            },
            {
                "title": "Exámenes Finales y Cierre de Semestre",
                "period": "2026-I",
                "event_type": "examenes",
                "start_date": date(2026, 7, 6),
                "end_date": date(2026, 7, 11),
                "description": "Evaluaciones finales y entrega de actas oficiales de notas."
            }
        ]

        for cal in calendar_events:
            AcademicCalendar.objects.get_or_create(
                title=cal["title"],
                period=cal["period"],
                defaults=cal
            )

        # 6. Horarios de Cursos
        courses_data = [
            {
                "course_code": "CS-101",
                "course_name": "Estructuras de Datos y Algoritmos",
                "section": "Sección A",
                "professor": "Dr. Carlos Mendoza Ramos",
                "days_and_time": "Lunes y Miércoles 08:00 - 10:00",
                "classroom": "Pabellón B - Lab 102",
                "credits": 4,
                "period": "2026-I"
            },
            {
                "course_code": "CS-101",
                "course_name": "Estructuras de Datos y Algoritmos",
                "section": "Sección B",
                "professor": "Mg. Patricia Vega Salazar",
                "days_and_time": "Martes y Jueves 14:00 - 16:00",
                "classroom": "Pabellón B - Lab 104",
                "credits": 4,
                "period": "2026-I"
            },
            {
                "course_code": "MAT-201",
                "course_name": "Cálculo Diferencial e Integral",
                "section": "Sección A",
                "professor": "Dr. Fernando Ruiz Paredes",
                "days_and_time": "Lunes y Jueves 10:00 - 12:00",
                "classroom": "Pabellón A - Aula 201",
                "credits": 5,
                "period": "2026-I"
            },
            {
                "course_code": "MAT-201",
                "course_name": "Cálculo Diferencial e Integral",
                "section": "Sección B",
                "professor": "Mg. Elena Morales Soto",
                "days_and_time": "Miércoles y Viernes 08:00 - 10:00",
                "classroom": "Pabellón A - Aula 204",
                "credits": 5,
                "period": "2026-I"
            },
            {
                "course_code": "ML-401",
                "course_name": "Introducción al Machine Learning",
                "section": "Sección A",
                "professor": "Dr. Javier Puentes Díaz",
                "days_and_time": "Martes y Viernes 18:00 - 20:00",
                "classroom": "Pabellón C - Laboratorio IA",
                "credits": 4,
                "period": "2026-I"
            },
            {
                "course_code": "DB-301",
                "course_name": "Sistemas de Bases de Datos",
                "section": "Sección A",
                "professor": "Mg. Andrea Torres Luna",
                "days_and_time": "Lunes y Miércoles 16:00 - 18:00",
                "classroom": "Pabellón B - Lab 201",
                "credits": 4,
                "period": "2026-I"
            }
        ]

        for course in courses_data:
            CourseSchedule.objects.get_or_create(
                course_code=course["course_code"],
                section=course["section"],
                period=course["period"],
                defaults=course
            )

        # 7. Trámites
        procedures_data = [
            {
                "name": "Retiro de Asignatura / Curso",
                "cost": "Gratuito",
                "processing_time": "48 horas hábiles",
                "requirements": (
                    "• Estar debidamente matriculado en el curso.\n"
                    "• No haber superado el número máximo de inasistencias (30%).\n"
                    "• Realizar la solicitud dentro del plazo del calendario académico (hasta el 22 de Mayo de 2026)."
                ),
                "steps": (
                    "1. Ingresa a la intranet estudiantil -> Módulo de Trámites.\n"
                    "2. Selecciona la opción 'Retiro de Curso' y marca la asignatura deseada.\n"
                    "3. Confirma tu solicitud con tu clave de estudiante.\n"
                    "4. Verifica el cambio en tu ficha de matrícula."
                ),
                "portal_link": "https://intranet.universidad.edu.pe/tramites/retiro"
            },
            {
                "name": "Reserva / Suspensión de Matrícula",
                "cost": "S/. 35.00",
                "processing_time": "3 a 5 días hábiles",
                "requirements": (
                    "• Carta o solicitud dirigida al Decano de la Facultad justificando el motivo (laboral, salud o personal).\n"
                    "• Constancia de no adeudo económico.\n"
                    "• Comprobante de pago por derecho de trámite."
                ),
                "steps": (
                    "1. Efectúa el pago en banca por concepto 'Reserva de Matrícula'.\n"
                    "2. Presenta tu solicitud por Mesa de Partes Virtual adjuntando los sustentos.\n"
                    "3. La resolución decanal será emitida y notificada a tu correo institucional en 5 días."
                ),
                "portal_link": "https://intranet.universidad.edu.pe/tramites/reserva"
            },
            {
                "name": "Certificado Oficial de Estudios",
                "cost": "S/. 50.00",
                "processing_time": "5 días hábiles",
                "requirements": (
                    "• No tener retenciones académicas ni financieras.\n"
                    "• 02 fotografías tamaño carné con traje formal.\n"
                    "• Pago de la tasa correspondiente."
                ),
                "steps": (
                    "1. Generar la orden de pago en la intranet.\n"
                    "2. Realizar el abono en cualquier banco afiliado.\n"
                    "3. Recibirás tu Certificado Digital con firma electrónica y código de verificación QR por correo institucional."
                ),
                "portal_link": "https://intranet.universidad.edu.pe/tramites/certificados"
            }
        ]

        for proc in procedures_data:
            Procedure.objects.get_or_create(
                name=proc["name"],
                defaults=proc
            )

        # 8. Reconstruir el índice del motor NLP
        nlp_engine.build_index()

        self.stdout.write(self.style.SUCCESS("✅ Base de datos poblada exitosamente con datos universitarios de demostración."))
        self.stdout.write(self.style.SUCCESS("⚡ Motor NLP local indexado y listo."))
