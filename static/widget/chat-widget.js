(function () {

    const OFFLINE_KB = {"bot_name": "UniBot Asistente", "university_name": "Universidad Nacional San Agustín de Demo", "welcome_message": "¡Hola! 👋 Soy UniBot, tu asistente académico universitario. Puedo ayudarte a consultar fechas de matrícula, horarios de cursos, procedimientos de trámites, pagos y mucho más. ¿Qué consulta tienes hoy?", "fallback_message": "Disculpa, no encontré información exacta sobre esa consulta en mi base de conocimientos. 🤔\n\nPuedes preguntarme sobre:\n• **Fechas de matrícula y calendario académico**\n• **Horarios de cursos** (Cálculo, Algoritmos, Machine Learning, Bases de Datos)\n• **Trámites** (Retiro de curso, Reserva de matrícula, Certificado de estudios, Carné)\n• **Pagos de pensión, Biblioteca y Servicios Médicos**", "quick_suggestions": ["¿Cuándo es la fecha de matrícula 2026-I?", "¿Cuáles son los horarios de Cálculo?", "¿Cómo solicitar retiro de curso?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?"], "entries": [{"type": "faq", "title": "¿Cuáles son los requisitos para la matrícula del semestre 2026-I?", "keywords": "requisitos matricula matricularme estar al dia deudas requisitos academicos", "priority_boost": 1.25, "answer": "Para realizar tu matrícula regular en el periodo 2026-I debes cumplir con los siguientes requisitos:\n\n1. **No registrar deudas pendientes** de pensiones o biblioteca del semestre anterior.\n2. **Haber completado la encuesta docente** en el portal del estudiante.\n3. **Tener habilitado el turno de matrícula** según tu promedio ponderado.\n4. Respetar los prerrequisitos de cada curso según tu malla curricular.", "suggestions": ["¿Cuántos créditos puedo matricular como máximo?", "¿Cuándo es la fecha de matrícula 2026-I?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?"]}, {"type": "faq", "title": "¿Cuántos créditos puedo matricular como máximo?", "keywords": "limite creditos maximo creditos cuantos creditos puedo llevar ampliacion", "priority_boost": 1.2, "answer": "El límite estándar de créditos por semestre es de **22 créditos**.\n\n• Si tu promedio del semestre anterior es **mayor a 15.00**, puedes solicitar ampliación hasta **26 créditos** mediante solicitud web.\n• En caso de estar en condición de riesgo o tercera matrícula, el límite es de **12 créditos**.", "suggestions": ["¿Cuáles son los requisitos para la matrícula del semestre 2026-I?", "¿Cuándo es la fecha de matrícula 2026-I?", "¿Cuáles son los horarios de Cálculo?"]}, {"type": "faq", "title": "¿Dónde y cómo puedo pagar mi pensión y matrícula?", "keywords": "pagar pension como pagar cuentas bancarias bcp bbva interbank pago cuota", "priority_boost": 1.25, "answer": "Puedes pagar tus pensiones y trámites en los siguientes canales oficiales indicando tu **Código de Estudiante**:\n\n• **Banca por Internet / App Móvil:** BCP, BBVA, Interbank y Scotiabank (buscar *Universidad Nacional Demo - Pensiones*).\n• **Agentes y Ventanillas:** Directamente en ventanilla bancaria presentando tu DNI/código.\n• **Caja del Campus Central:** Pabellón Administrativo (Lunes a Viernes de 08:30 a 16:30 hrs).", "suggestions": ["¿Cómo puedo tramitar el carné universitario?", "¿Cuáles son los requisitos para la matrícula del semestre 2026-I?", "¿Cómo solicitar certificado de estudios?"]}, {"type": "faq", "title": "¿Cómo puedo tramitar el carné universitario?", "keywords": "carne carnet universitario tramite sunedu duplicado renovar", "priority_boost": 1.15, "answer": "El carné universitario oficial se tramita de la siguiente forma:\n\n1. Realiza el pago por derecho de carné (`S/. 16.00`) en caja o banca web.\n2. Sube tu foto tamaño pasaporte con fondo blanco en formato JPG a tu intranet.\n3. La universidad enviará el lote de emisión a la entidad reguladora (SUNEDU).\n4. Tiempo de entrega aproximado: **20 a 30 días hábiles**.", "suggestions": ["¿Dónde y cómo puedo pagar mi pensión y matrícula?", "¿Cómo solicitar certificado de estudios?", "¿Cuáles son los horarios de la Biblioteca Central?"]}, {"type": "faq", "title": "¿Cuáles son los horarios de la Biblioteca Central y cómo acceder a los libros virtuales?", "keywords": "biblioteca libros sala de estudio horario biblioteca virtual bases de datos", "priority_boost": 1.1, "answer": "### 📚 Biblioteca Central\n\n• **Horario presencial:** Lunes a Viernes de 08:00 a 20:00 hrs | Sábados de 08:30 a 13:00 hrs.\n• **Biblioteca Virtual:** Ingresa a `https://biblioteca.universidad.edu.pe` con tu correo institucional para acceder a IEEE Xplore, ScienceDirect, Scopus y libros digitales.", "suggestions": ["¿Qué servicios médicos y de apoyo psicológico ofrece la universidad?", "¿Cómo puedo tramitar el carné universitario?", "¿Cuáles son los horarios de Cálculo?"]}, {"type": "faq", "title": "¿Qué servicios médicos y de apoyo psicológico ofrece la universidad?", "keywords": "topico medico psicologo salud bienestar atencion medica cita", "priority_boost": 1.1, "answer": "La Dirección de Bienestar Universitario ofrece atención gratuita para alumnos matriculados:\n\n• **Tópico Médico:** Pabellón C - 1er piso (Urgencias, medicina general y enfermería).\n• **Consultorio Psicológico:** Citas presenciales y virtuales previa reserva en la intranet de Bienestar.\n• **Seguro contra Accidentes:** Cobertura 24/7 durante el periodo académico activo.", "suggestions": ["¿Cuáles son los horarios de la Biblioteca Central y cómo acceder a los libros virtuales?", "¿Cómo solicitar reserva de matrícula?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?"]}, {"type": "calendar", "title": "Matrícula Regular 2026-I (2026-I)", "keywords": "fecha fechas cronograma calendario cuando inicia cuando es Matrícula Regular 2026-I", "priority_boost": 1.25, "answer": "### 📅 **Matrícula Regular 2026-I** (2026-I)\n\n• **Fecha oficial:** 16/02/2026 hasta el 27/02/2026\n• **Tipo de evento:** Matrícula\n\nMatrícula por internet según orden de mérito y turnos asignados en la intranet.\n\n💡 *Recuerda verificar tu estado de matrícula y deudas en el portal del estudiante antes de esta fecha.*", "suggestions": ["¿Cuáles son los requisitos para la matrícula del semestre 2026-I?", "¿Cómo solicitar reserva de matrícula?", "¿Cuáles son los horarios de Cálculo?"]}, {"type": "calendar", "title": "Inicio de Clases Semestre 2026-I y Exámenes", "keywords": "fecha fechas inicio clases examenes parciales finales semestre 2026", "priority_boost": 1.15, "answer": "### 📅 **Calendario Académico Semestre 2026-I**\n\n• **Matrícula Regular:** 16/02/2026 al 27/02/2026\n• **Matrícula Extemporánea:** 02/03/2026 al 06/03/2026\n• **Inicio de Clases:** 16/03/2026\n• **Exámenes Parciales:** 04/05/2026 al 09/05/2026\n• **Plazo Límite Retiro de Cursos:** 22/05/2026\n• **Exámenes Finales:** 06/07/2026 al 11/07/2026", "suggestions": ["¿Cuáles son los horarios de Cálculo?", "¿Cómo solicitar retiro de curso?", "¿Cuáles son los requisitos para la matrícula del semestre 2026-I?"]}, {"type": "course", "title": "MAT-201 - Cálculo Diferencial e Integral", "keywords": "Cálculo Diferencial e Integral MAT-201 Fernando Ruiz Elena Morales horario horarios curso clase", "priority_boost": 1.3, "answer": "### 📖 **Horarios disponibles: Cálculo Diferencial e Integral (MAT-201)**\n\n**Créditos:** 5 | **Periodo:** 2026-I\n\n| Sección | Docente | Horario | Aula |\n| :--- | :--- | :--- | :--- |\n| **Sección A** | Dr. Fernando Ruiz Paredes | Lunes y Jueves 10:00 - 12:00 | Pabellón A - Aula 201 |\n| **Sección B** | Mg. Elena Morales Soto | Miércoles y Viernes 08:00 - 10:00 | Pabellón A - Aula 204 |\n\n📌 *Nota: La asignación final de aula puede variar según la capacidad de aforo.*", "suggestions": ["¿Cuáles son los horarios de Estructuras de Datos y Algoritmos?", "¿Cuáles son los horarios de Machine Learning?", "¿Cuántos créditos puedo matricular como máximo?"]}, {"type": "course", "title": "CS-101 - Estructuras de Datos y Algoritmos", "keywords": "Estructuras de Datos y Algoritmos CS-101 Carlos Mendoza Patricia Vega horario horarios curso clase", "priority_boost": 1.3, "answer": "### 📖 **Horarios disponibles: Estructuras de Datos y Algoritmos (CS-101)**\n\n**Créditos:** 4 | **Periodo:** 2026-I\n\n| Sección | Docente | Horario | Aula |\n| :--- | :--- | :--- | :--- |\n| **Sección A** | Dr. Carlos Mendoza Ramos | Lunes y Miércoles 08:00 - 10:00 | Pabellón B - Lab 102 |\n| **Sección B** | Mg. Patricia Vega Salazar | Martes y Jueves 14:00 - 16:00 | Pabellón B - Lab 104 |\n\n📌 *Nota: La asignación final de aula puede variar según la capacidad de aforo.*", "suggestions": ["¿Cuáles son los horarios de Cálculo?", "¿Cuáles son los horarios de Machine Learning?", "¿Cuáles son los horarios de Bases de Datos?"]}, {"type": "course", "title": "ML-401 - Introducción al Machine Learning", "keywords": "Introducción al Machine Learning ML-401 Javier Puentes IA inteligencia artificial horario horarios curso", "priority_boost": 1.3, "answer": "### 📖 **Horarios disponibles: Introducción al Machine Learning (ML-401)**\n\n**Créditos:** 4 | **Periodo:** 2026-I\n\n| Sección | Docente | Horario | Aula |\n| :--- | :--- | :--- | :--- |\n| **Sección A** | Dr. Javier Puentes Díaz | Martes y Viernes 18:00 - 20:00 | Pabellón C - Laboratorio IA |\n\n📌 *Nota: La asignación final de aula puede variar según la capacidad de aforo.*", "suggestions": ["¿Cuáles son los horarios de Bases de Datos?", "¿Cuáles son los horarios de Estructuras de Datos y Algoritmos?", "¿Cuántos créditos puedo matricular como máximo?"]}, {"type": "course", "title": "DB-301 - Sistemas de Bases de Datos", "keywords": "Sistemas de Bases de Datos DB-301 Andrea Torres horario horarios curso clase", "priority_boost": 1.3, "answer": "### 📖 **Horarios disponibles: Sistemas de Bases de Datos (DB-301)**\n\n**Créditos:** 4 | **Periodo:** 2026-I\n\n| Sección | Docente | Horario | Aula |\n| :--- | :--- | :--- | :--- |\n| **Sección A** | Mg. Andrea Torres Luna | Lunes y Miércoles 16:00 - 18:00 | Pabellón B - Lab 201 |\n\n📌 *Nota: La asignación final de aula puede variar según la capacidad de aforo.*", "suggestions": ["¿Cuáles son los horarios de Cálculo?", "¿Cuáles son los horarios de Machine Learning?", "¿Cómo solicitar retiro de curso?"]}, {"type": "procedure", "title": "Retiro de Asignatura / Curso", "keywords": "tramite solicitud requisitos como solicitar retiro de curso asignatura retirarme", "priority_boost": 1.25, "answer": "### 📋 **Trámite: Retiro de Asignatura / Curso**\n\n• **Costo de trámite:** `Gratuito`\n• **Tiempo estimado:** 48 horas hábiles\n\n#### **📌 Requisitos:**\n• Estar debidamente matriculado en el curso.\n• No haber superado el número máximo de inasistencias (30%).\n• Realizar la solicitud dentro del plazo del calendario académico (hasta el 22 de Mayo de 2026).\n\n#### **🚀 Pasos a seguir:**\n1. Ingresa a la intranet estudiantil -> Módulo de Trámites.\n2. Selecciona la opción 'Retiro de Curso' y marca la asignatura deseada.\n3. Confirma tu solicitud con tu clave de estudiante.\n4. Verifica el cambio en tu ficha de matrícula.\n\n🔗 [Ingresar al Portal de Trámites](https://intranet.universidad.edu.pe/tramites/retiro)", "suggestions": ["¿Cómo solicitar reserva de matrícula?", "¿Cómo solicitar certificado de estudios?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?"]}, {"type": "procedure", "title": "Reserva / Suspensión de Matrícula", "keywords": "tramite solicitud requisitos como solicitar reserva suspension de matricula reservar", "priority_boost": 1.25, "answer": "### 📋 **Trámite: Reserva / Suspensión de Matrícula**\n\n• **Costo de trámite:** `S/. 35.00`\n• **Tiempo estimado:** 3 a 5 días hábiles\n\n#### **📌 Requisitos:**\n• Carta o solicitud dirigida al Decano de la Facultad justificando el motivo (laboral, salud o personal).\n• Constancia de no adeudo económico.\n• Comprobante de pago por derecho de trámite.\n\n#### **🚀 Pasos a seguir:**\n1. Efectúa el pago en banca por concepto 'Reserva de Matrícula'.\n2. Presenta tu solicitud por Mesa de Partes Virtual adjuntando los sustentos.\n3. La resolución decanal será emitida y notificada a tu correo institucional en 5 días.\n\n🔗 [Ingresar al Portal de Trámites](https://intranet.universidad.edu.pe/tramites/reserva)", "suggestions": ["¿Cómo solicitar retiro de curso?", "¿Cómo solicitar certificado de estudios?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?"]}, {"type": "procedure", "title": "Certificado Oficial de Estudios", "keywords": "tramite solicitud requisitos como solicitar certificado oficial de estudios constancia", "priority_boost": 1.25, "answer": "### 📋 **Trámite: Certificado Oficial de Estudios**\n\n• **Costo de trámite:** `S/. 50.00`\n• **Tiempo estimado:** 5 días hábiles\n\n#### **📌 Requisitos:**\n• No tener retenciones académicas ni financieras.\n• 02 fotografías tamaño carné con traje formal.\n• Pago de la tasa correspondiente.\n\n#### **🚀 Pasos a seguir:**\n1. Generar la orden de pago en la intranet.\n2. Realizar el abono en cualquier banco afiliado.\n3. Recibirás tu Certificado Digital con firma electrónica y código de verificación QR por correo institucional.\n\n🔗 [Ingresar al Portal de Trámites](https://intranet.universidad.edu.pe/tramites/certificados)", "suggestions": ["¿Cómo puedo tramitar el carné universitario?", "¿Dónde y cómo puedo pagar mi pensión y matrícula?", "¿Cómo solicitar retiro de curso?"]}]};
    function normalizeOffline(str) {
        return (str || '').toLowerCase()
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
            .replace(/[^\w\s]/g, ' ').replace(/\s+/g, ' ').trim();
    }
    function answerOffline(query) {
        const normQ = normalizeOffline(query);
        const stop = new Set(['el','la','los','las','un','una','de','del','a','al','en','para','por','con','y','o','que','es','son','como','cual','cuales','cuando','donde','mi','mis','tu','tus','su']);
        const tokens = normQ.split(' ').filter(w => w.length > 2 && !stop.has(w));
        let best = null;
        let bestScore = 0;
        for (const item of OFFLINE_KB.entries) {
            const titleNorm = normalizeOffline(item.title);
            const kwNorm = normalizeOffline(item.keywords);
            const textNorm = normalizeOffline(item.answer);
            let score = 0;
            for (const t of tokens) {
                if (titleNorm.includes(t)) score += 0.5;
                else if (kwNorm.includes(t)) score += 0.35;
                else if (textNorm.includes(t)) score += 0.15;
            }
            score *= (item.priority_boost || 1.0);
            if (score > bestScore) {
                bestScore = score;
                best = item;
            }
        }
        if (!best || bestScore < 0.15) {
            return {
                answer: OFFLINE_KB.fallback_message,
                suggestions: OFFLINE_KB.quick_suggestions
            };
        }
        return {
            message_id: Math.floor(Math.random() * 10000),
            answer: best.answer,
            suggestions: best.suggestions
        };
    }
    const _origFetch = window.fetch.bind(window);
    window.fetch = async function(url, options) {
        try {
            const res = await _origFetch(url, options);
            if (res.ok) return res;
        } catch (e) {}
        const urlStr = String(url);
        if (urlStr.includes('/api/config/')) {
            return new Response(JSON.stringify(OFFLINE_KB), { status: 200, headers: { 'Content-Type': 'application/json' } });
        }
        if (urlStr.includes('/api/chat/') && options && options.body) {
            const body = JSON.parse(options.body);
            const reply = answerOffline(body.message || '');
            return new Response(JSON.stringify(reply), { status: 200, headers: { 'Content-Type': 'application/json' } });
        }
        if (urlStr.includes('/api/feedback/')) {
            return new Response(JSON.stringify({ success: true }), { status: 200, headers: { 'Content-Type': 'application/json' } });
        }
        throw new Error('Offline');
    };

    // Configuración base del widget
    const SCRIPT_TAG = document.currentScript || document.querySelector('script[src*="chat-widget.js"]');
    const API_BASE_URL = SCRIPT_TAG ? new URL(SCRIPT_TAG.src).origin : window.location.origin;
    const STORAGE_KEY = 'unibot_session_id';

    // Crear contenedor con Shadow DOM para aislamiento total de estilos
    const hostElement = document.createElement('div');
    hostElement.id = 'unibot-chat-widget-root';
    document.body.appendChild(hostElement);
    const shadow = hostElement.attachShadow({ mode: 'open' });

    // Estilos encapsulados
    const styles = `
        :host {
            --primary: #1e40af;
            --primary-hover: #1d4ed8;
            --bg-user: #2563eb;
            --text-user: #ffffff;
            --bg-bot: #f1f5f9;
            --text-bot: #0f172a;
            --border-color: #e2e8f0;
            --font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            font-family: var(--font-family);
            z-index: 999999;
            position: fixed;
            bottom: 24px;
            right: 24px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        /* Botón flotante disparador */
        .chat-trigger {
            width: 62px;
            height: 62px;
            border-radius: 50%;
            background: linear-gradient(135deg, #1e40af, #3b82f6);
            color: #ffffff;
            border: none;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.35);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.2s;
            position: relative;
        }

        .chat-trigger:hover {
            transform: scale(1.08);
            box-shadow: 0 12px 30px rgba(37, 99, 235, 0.45);
        }

        .badge-pulse {
            position: absolute;
            top: 2px;
            right: 2px;
            width: 14px;
            height: 14px;
            background-color: #10b981;
            border: 2px solid #ffffff;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
            70% { transform: scale(1.1); box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }

        /* Ventana principal de chat */
        .chat-window {
            position: fixed;
            bottom: 96px;
            right: 24px;
            width: 400px;
            max-width: calc(100vw - 32px);
            height: 620px;
            max-height: calc(100vh - 120px);
            background: #ffffff;
            border-radius: 18px;
            box-shadow: 0 14px 40px rgba(0, 0, 0, 0.16), 0 2px 10px rgba(0, 0, 0, 0.06);
            display: flex;
            flex-direction: column;
            overflow: hidden;
            border: 1px solid rgba(226, 232, 240, 0.8);
            opacity: 0;
            pointer-events: none;
            transform: translateY(16px) scale(0.96);
            transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        .chat-window.open {
            opacity: 1;
            pointer-events: auto;
            transform: translateY(0) scale(1);
        }

        /* Cabecera */
        .chat-header {
            background: linear-gradient(135deg, #1e3a8a, #2563eb);
            color: #ffffff;
            padding: 16px 18px;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .header-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .bot-avatar {
            width: 40px;
            height: 40px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 22px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .header-titles h3 {
            font-size: 15px;
            font-weight: 700;
            line-height: 1.2;
        }

        .header-titles p {
            font-size: 11px;
            opacity: 0.88;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .status-dot {
            width: 7px;
            height: 7px;
            background: #4ade80;
            border-radius: 50%;
            display: inline-block;
        }

        .header-actions {
            display: flex;
            gap: 6px;
        }

        .icon-btn {
            background: transparent;
            border: none;
            color: #ffffff;
            opacity: 0.85;
            cursor: pointer;
            width: 28px;
            height: 28px;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            transition: all 0.15s;
        }

        .icon-btn:hover {
            opacity: 1;
            background: rgba(255, 255, 255, 0.15);
        }

        /* Área de mensajes */
        .chat-messages {
            flex: 1;
            overflow-y: auto;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            background: #f8fafc;
        }

        .message-row {
            display: flex;
            flex-direction: column;
            gap: 4px;
            max-width: 86%;
        }

        .message-row.user {
            align-self: flex-end;
            align-items: flex-end;
        }

        .message-row.bot {
            align-self: flex-start;
            align-items: flex-start;
        }

        .message-bubble {
            padding: 12px 16px;
            border-radius: 16px;
            font-size: 13.5px;
            line-height: 1.5;
            word-break: break-word;
        }

        .message-row.user .message-bubble {
            background: var(--bg-user);
            color: var(--text-user);
            border-bottom-right-radius: 4px;
        }

        .message-row.bot .message-bubble {
            background: #ffffff;
            color: var(--text-bot);
            border: 1px solid var(--border-color);
            border-bottom-left-radius: 4px;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
        }

        /* Markdown y Tablas dentro de las respuestas */
        .message-bubble h3 { font-size: 14px; margin-bottom: 6px; color: #1e3a8a; }
        .message-bubble h4 { font-size: 13px; margin: 8px 0 4px 0; color: #334155; }
        .message-bubble p { margin-bottom: 6px; }
        .message-bubble p:last-child { margin-bottom: 0; }
        .message-bubble ul, .message-bubble ol { margin: 6px 0 6px 18px; }
        .message-bubble li { margin-bottom: 3px; }
        .message-bubble code { background: #f1f5f9; padding: 2px 5px; border-radius: 4px; font-size: 12px; color: #b91c1c; }
        .message-bubble a { color: #2563eb; text-decoration: underline; }
        
        .message-bubble table {
            width: 100%;
            border-collapse: collapse;
            margin: 8px 0;
            font-size: 12px;
            background: #ffffff;
        }
        .message-bubble th, .message-bubble td {
            border: 1px solid #e2e8f0;
            padding: 6px 8px;
            text-align: left;
        }
        .message-bubble th {
            background: #f1f5f9;
            font-weight: 600;
        }

        .message-footer {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 10.5px;
            color: #94a3b8;
            padding: 0 4px;
        }

        .feedback-btns {
            display: flex;
            gap: 4px;
            margin-left: 4px;
        }

        .feedback-btn {
            background: transparent;
            border: none;
            cursor: pointer;
            font-size: 11px;
            opacity: 0.6;
            padding: 1px 3px;
            border-radius: 3px;
            transition: all 0.15s;
        }

        .feedback-btn:hover {
            opacity: 1;
            background: #e2e8f0;
        }

        /* Chips de sugerencias */
        .suggestions-container {
            display: flex;
            flex-wrap: wrap;
            gap: 6px;
            margin-top: 6px;
        }

        .chip {
            background: #eff6ff;
            color: #1d4ed8;
            border: 1px solid #bfdbfe;
            border-radius: 14px;
            padding: 6px 12px;
            font-size: 11.5px;
            cursor: pointer;
            transition: all 0.15s;
            text-align: left;
            line-height: 1.3;
        }

        .chip:hover {
            background: #dbeafe;
            border-color: #93c5fd;
            transform: translateY(-1px);
        }

        /* Indicador de escribiendo */
        .typing-indicator {
            display: flex;
            align-items: center;
            gap: 4px;
            padding: 10px 14px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 16px;
            width: fit-content;
        }

        .typing-dot {
            width: 6px;
            height: 6px;
            background: #94a3b8;
            border-radius: 50%;
            animation: bounce 1.3s infinite ease-in-out;
        }

        .typing-dot:nth-child(2) { animation-delay: 0.15s; }
        .typing-dot:nth-child(3) { animation-delay: 0.3s; }

        @keyframes bounce {
            0%, 80%, 100% { transform: translateY(0); }
            40% { transform: translateY(-6px); background: #2563eb; }
        }

        /* Formulario de entrada */
        .chat-input-area {
            padding: 12px 14px;
            background: #ffffff;
            border-top: 1px solid var(--border-color);
            display: flex;
            gap: 8px;
            align-items: center;
        }

        .chat-input {
            flex: 1;
            border: 1px solid #cbd5e1;
            border-radius: 22px;
            padding: 10px 16px;
            font-size: 13.5px;
            outline: none;
            font-family: inherit;
            transition: border-color 0.15s;
        }

        .chat-input:focus {
            border-color: var(--primary);
            box-shadow: 0 0 0 2px rgba(37, 99, 235, 0.15);
        }

        .send-btn {
            width: 38px;
            height: 38px;
            border-radius: 50%;
            background: var(--primary);
            color: #ffffff;
            border: none;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 16px;
            transition: all 0.15s;
            flex-shrink: 0;
        }

        .send-btn:hover:not(:disabled) {
            background: var(--primary-hover);
            transform: scale(1.05);
        }

        .send-btn:disabled {
            background: #cbd5e1;
            cursor: not-allowed;
        }
    `;

    // Estructura HTML del widget
    const template = document.createElement('template');
    template.innerHTML = `
        <style>${styles}</style>
        
        <button class="chat-trigger" id="widgetTrigger" title="Abrir asistente universitario">
            💬
            <span class="badge-pulse"></span>
        </button>

        <div class="chat-window" id="widgetWindow">
            <div class="chat-header">
                <div class="header-info">
                    <div class="bot-avatar">🤖</div>
                    <div class="header-titles">
                        <h3 id="botHeaderTitle">UniBot Asistente</h3>
                        <p><span class="status-dot"></span> <span id="botHeaderSubtitle">En línea • Atención 24/7</span></p>
                    </div>
                </div>
                <div class="header-actions">
                    <button class="icon-btn" id="resetBtn" title="Reiniciar conversación">🔄</button>
                    <button class="icon-btn" id="closeBtn" title="Cerrar chat">✕</button>
                </div>
            </div>

            <div class="chat-messages" id="messagesContainer">
                <!-- Los mensajes se inyectan dinámicamente -->
            </div>

            <div class="chat-input-area">
                <input type="text" id="userInput" class="chat-input" placeholder="Pregunta sobre matrículas, cursos, fechas..." autocomplete="off" />
                <button id="sendBtn" class="send-btn" title="Enviar mensaje">➤</button>
            </div>
        </div>
    `;

    shadow.appendChild(template.content.cloneNode(true));

    // Referencias a elementos
    const trigger = shadow.getElementById('widgetTrigger');
    const windowEl = shadow.getElementById('widgetWindow');
    const closeBtn = shadow.getElementById('closeBtn');
    const resetBtn = shadow.getElementById('resetBtn');
    const inputEl = shadow.getElementById('userInput');
    const sendBtn = shadow.getElementById('sendBtn');
    const messagesContainer = shadow.getElementById('messagesContainer');
    const botHeaderTitle = shadow.getElementById('botHeaderTitle');

    let sessionId = localStorage.getItem(STORAGE_KEY) || '';
    let isOpen = false;

    // Utilidad simple para parsear Markdown básico a HTML seguro
    function formatMarkdown(text) {
        if (!text) return '';
        let html = text
            .replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
            // Encabezados
            .replace(/^### (.*$)/gim, '<h3>$1</h3>')
            .replace(/^#### (.*$)/gim, '<h4>$1</h4>')
            // Negrita e itálica
            .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
            .replace(/\*(.*?)\*/gim, '<em>$1</em>')
            // Código inline
            .replace(/`(.*?)`/gim, '<code>$1</code>')
            // Enlaces [texto](url)
            .replace(/\[([^\]]+)\]\(([^)]+)\)/gim, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>')
            // Listas
            .replace(/^\s*•\s+(.*$)/gim, '<li>$1</li>')
            .replace(/^\s*\*\s+(.*$)/gim, '<li>$1</li>');

        // Procesar tablas Markdown si existen
        if (html.includes('|')) {
            const lines = html.split('\n');
            let inTable = false;
            let tableHtml = '<table>';
            let processedLines = [];

            for (let line of lines) {
                const trimmed = line.trim();
                if (trimmed.startsWith('|') && trimmed.endsWith('|')) {
                    if (trimmed.includes(':---') || trimmed.includes('---')) {
                        continue; // Fila separadora
                    }
                    const cells = trimmed.slice(1, -1).split('|').map(c => c.trim());
                    if (!inTable) {
                        inTable = true;
                        tableHtml += '<thead><tr>' + cells.map(c => `<th>${c}</th>`).join('') + '</tr></thead><tbody>';
                    } else {
                        tableHtml += '<tr>' + cells.map(c => `<td>${c}</td>`).join('') + '</tr>';
                    }
                } else {
                    if (inTable) {
                        inTable = false;
                        tableHtml += '</tbody></table>';
                        processedLines.push(tableHtml);
                        tableHtml = '<table>';
                    }
                    processedLines.push(line);
                }
            }
            if (inTable) {
                tableHtml += '</tbody></table>';
                processedLines.push(tableHtml);
            }
            html = processedLines.join('\n');
        }

        // Reemplazar saltos de línea con párrafos / br
        html = html.replace(/\n\n/g, '<br><br>').replace(/\n/g, '<br>');
        return html;
    }

    // Cargar configuración inicial del servidor
    async function loadConfig() {
        try {
            const res = await fetch(`${API_BASE_URL}/api/config/`);
            if (res.ok) {
                const data = await res.json();
                botHeaderTitle.innerText = data.bot_name || 'UniBot';
                
                // Mensaje inicial de bienvenida
                renderBotMessage({
                    answer: data.welcome_message,
                    suggestions: data.quick_suggestions || []
                });
            }
        } catch (e) {
            renderBotMessage({
                answer: "¡Hola! 👋 Soy tu asistente universitario. ¿En qué puedo orientarte hoy sobre matrículas, horarios o trámites?",
                suggestions: ["¿Cuándo es la matrícula?", "¿Cuáles son los horarios de Cálculo?"]
            });
        }
    }

    // Renderizar mensaje de usuario
    function renderUserMessage(text) {
        const row = document.createElement('div');
        row.className = 'message-row user';
        row.innerHTML = `
            <div class="message-bubble">${text.replace(/</g, "&lt;")}</div>
            <div class="message-footer">Tú • ${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}</div>
        `;
        messagesContainer.appendChild(row);
        scrollToBottom();
    }

    // Renderizar indicador de "escribiendo"
    function showTypingIndicator() {
        const ind = document.createElement('div');
        ind.id = 'activeTypingIndicator';
        ind.className = 'message-row bot';
        ind.innerHTML = `
            <div class="typing-indicator">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        `;
        messagesContainer.appendChild(ind);
        scrollToBottom();
    }

    function removeTypingIndicator() {
        const ind = shadow.getElementById('activeTypingIndicator');
        if (ind) ind.remove();
    }

    // Renderizar mensaje del Bot
    function renderBotMessage(data) {
        const row = document.createElement('div');
        row.className = 'message-row bot';

        let formattedText = formatMarkdown(data.answer);
        let feedbackHtml = '';
        if (data.message_id) {
            feedbackHtml = `
                <div class="feedback-btns">
                    <button class="feedback-btn" data-id="${data.message_id}" data-val="1" title="Respuesta útil">👍</button>
                    <button class="feedback-btn" data-id="${data.message_id}" data-val="-1" title="Respuesta no útil">👎</button>
                </div>
            `;
        }

        let suggestionsHtml = '';
        if (data.suggestions && data.suggestions.length > 0) {
            suggestionsHtml = '<div class="suggestions-container">' +
                data.suggestions.map(s => `<button class="chip" data-question="${s.replace(/"/g, '&quot;')}">${s}</button>`).join('') +
                '</div>';
        }

        row.innerHTML = `
            <div class="message-bubble">${formattedText}</div>
            <div class="message-footer">
                UniBot • ${new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                ${feedbackHtml}
            </div>
            ${suggestionsHtml}
        `;

        messagesContainer.appendChild(row);

        // Listeners para chips de sugerencias
        row.querySelectorAll('.chip').forEach(btn => {
            btn.addEventListener('click', () => {
                const q = btn.getAttribute('data-question');
                sendMessage(q);
            });
        });

        // Listeners para feedback
        row.querySelectorAll('.feedback-btn').forEach(btn => {
            btn.addEventListener('click', async () => {
                const msgId = btn.getAttribute('data-id');
                const val = parseInt(btn.getAttribute('data-val'));
                try {
                    await fetch(`${API_BASE_URL}/api/feedback/`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ message_id: msgId, feedback: val })
                    });
                    btn.parentElement.innerHTML = '<span style="color:#10b981; font-size:10px;">¡Gracias!</span>';
                } catch (e) {}
            });
        });

        scrollToBottom();
    }

    function scrollToBottom() {
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    }

    // Enviar mensaje al backend
    async function sendMessage(text) {
        const query = (text || inputEl.value).trim();
        if (!query) return;

        inputEl.value = '';
        renderUserMessage(query);
        showTypingIndicator();

        try {
            const res = await fetch(`${API_BASE_URL}/api/chat/`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: query,
                    session_id: sessionId
                })
            });

            removeTypingIndicator();

            if (res.ok) {
                const data = await res.json();
                if (data.session_id) {
                    sessionId = data.session_id;
                    localStorage.setItem(STORAGE_KEY, sessionId);
                }
                renderBotMessage(data);
            } else {
                renderBotMessage({
                    answer: "Lo siento, ocurrió un inconveniente al consultar el servidor. Intenta de nuevo en unos segundos."
                });
            }
        } catch (err) {
            removeTypingIndicator();
            renderBotMessage({
                answer: "⚠️ No pude conectar con el servidor. Verifica que el servidor de Django esté ejecutándose."
            });
        }
    }

    // Toggle ventana de chat
    function toggleChat(force) {
        isOpen = force !== undefined ? force : !isOpen;
        if (isOpen) {
            windowEl.classList.add('open');
            trigger.style.transform = 'scale(0.85)';
            inputEl.focus();
        } else {
            windowEl.classList.remove('open');
            trigger.style.transform = '';
        }
    }

    // Eventos
    trigger.addEventListener('click', () => toggleChat());
    closeBtn.addEventListener('click', () => toggleChat(false));
    
    resetBtn.addEventListener('click', () => {
        messagesContainer.innerHTML = '';
        sessionId = '';
        localStorage.removeItem(STORAGE_KEY);
        loadConfig();
    });

    sendBtn.addEventListener('click', () => sendMessage());
    
    inputEl.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            e.preventDefault();
            sendMessage();
        }
    });

    // Inicializar
    loadConfig();
})();
