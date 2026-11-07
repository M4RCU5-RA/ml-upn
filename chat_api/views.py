import uuid
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from knowledge_base.models import (
    Category, FAQ, AcademicCalendar, CourseSchedule, Procedure,
    BotConfig, ChatSession, ChatMessage
)
from knowledge_base.ml_engine import nlp_engine


@method_decorator(csrf_exempt, name='dispatch')
class ChatAPIView(APIView):
    """Endpoint principal para procesar preguntas de estudiantes."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        user_message = request.data.get('message', '').strip()
        session_id = request.data.get('session_id', '').strip()

        if not user_message:
            return Response({'error': 'El mensaje no puede estar vacío.'}, status=status.HTTP_400_BAD_REQUEST)

        # Obtener o crear sesión de chat
        if not session_id:
            session_id = str(uuid.uuid4())
            session = ChatSession.objects.create(
                session_id=session_id,
                user_ip=self._get_client_ip(request)
            )
        else:
            session, _ = ChatSession.objects.get_or_create(
                session_id=session_id,
                defaults={'user_ip': self._get_client_ip(request)}
            )

        # 1. Registrar mensaje del alumno
        ChatMessage.objects.create(
            session=session,
            sender='user',
            message=user_message
        )

        # 2. Procesar con el motor NLP
        result = nlp_engine.answer_query(user_message)

        # 3. Registrar respuesta del Bot
        bot_msg = ChatMessage.objects.create(
            session=session,
            sender='bot',
            message=result['answer'],
            confidence_score=result['confidence'],
            matched_faq_id=result.get('matched_faq_id')
        )

        return Response({
            'session_id': session.session_id,
            'message_id': bot_msg.id,
            'answer': result['answer'],
            'confidence': result['confidence'],
            'source_type': result['source_type'],
            'suggestions': result.get('suggestions', []),
            'timestamp': timezone.now().isoformat()
        })

    def _get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        return request.META.get('REMOTE_ADDR')


@method_decorator(csrf_exempt, name='dispatch')
class ConfigAPIView(APIView):
    """Devuelve la configuración y mensaje de bienvenida para el widget."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        config = BotConfig.get_settings()
        
        # Sugerencias destacadas iniciales
        quick_suggestions = [
            "¿Cuándo es la fecha de matrícula 2026-I?",
            "¿Cuáles son los horarios de Cálculo y Algoritmos?",
            "¿Cómo solicitar retiro de curso o reserva?",
            "¿Dónde y cómo pagar la pensión universitaria?"
        ]

        return Response({
            'bot_name': config.bot_name,
            'university_name': config.university_name,
            'welcome_message': config.welcome_message,
            'quick_suggestions': quick_suggestions,
            'ai_provider': config.get_ai_provider_display(),
        })


@method_decorator(csrf_exempt, name='dispatch')
class FeedbackAPIView(APIView):
    """Permite al estudiante calificar la respuesta del bot."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        message_id = request.data.get('message_id')
        feedback_val = request.data.get('feedback')  # 1 o -1

        if not message_id or feedback_val not in [1, -1]:
            return Response({'error': 'Parámetros inválidos.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            msg = ChatMessage.objects.get(id=message_id, sender='bot')
            msg.feedback = feedback_val
            msg.save(update_fields=['feedback'])
            return Response({'success': True, 'message': 'Gracias por tu feedback.'})
        except ChatMessage.DoesNotExist:
            return Response({'error': 'Mensaje no encontrado.'}, status=status.HTTP_404_NOT_FOUND)


@method_decorator(csrf_exempt, name='dispatch')
class KnowledgeDirectoryAPIView(APIView):
    """Devuelve las categorías y preguntas disponibles para exploración rápida."""
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request):
        categories = Category.objects.prefetch_related('faqs').all()
        data = []
        for cat in categories:
            faqs = cat.faqs.filter(is_active=True).values('id', 'question')
            data.append({
                'id': cat.id,
                'name': cat.name,
                'icon': cat.icon,
                'description': cat.description,
                'faqs': list(faqs)
            })
        return Response({'categories': data})
