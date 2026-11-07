from django.shortcuts import render
from .models import BotConfig, AcademicCalendar, Category

def demo_portal_view(request):
    """Renderiza el portal universitario de demostración donde el widget de chat está embebido."""
    config = BotConfig.get_settings()
    upcoming_events = AcademicCalendar.objects.filter(is_active=True).order_by('start_date')[:4]
    categories = Category.objects.all()[:6]
    return render(request, 'demo_portal.html', {
        'config': config,
        'upcoming_events': upcoming_events,
        'categories': categories,
    })

def presentation_view(request):
    """Renderiza las diapositivas de presentación del proyecto en HTML."""
    return render(request, 'presentation.html')
