from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Category, FAQ, AcademicCalendar, CourseSchedule, Procedure,
    BotConfig, ChatSession, ChatMessage
)
from .ml_engine import nlp_engine


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('icon_name', 'order', 'faq_count')
    list_editable = ('order',)
    search_fields = ('name', 'description')

    def icon_name(self, obj):
        return f"{obj.icon} {obj.name}"
    icon_name.short_description = "Categoría"

    def faq_count(self, obj):
        return obj.faqs.count()
    faq_count.short_description = "Total FAQs"


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'category', 'priority', 'view_count', 'is_active', 'updated_at')
    list_filter = ('category', 'is_active', 'priority')
    search_fields = ('question', 'answer', 'keywords')
    list_editable = ('priority', 'is_active')
    actions = ['rebuild_nlp_index', 'mark_active', 'mark_inactive']

    def rebuild_nlp_index(self, request, queryset):
        nlp_engine.build_index()
        self.message_user(request, "✅ Motor de IA reindexado exitosamente.")
    rebuild_nlp_index.short_description = "⚡ Reindexar Motor de Búsqueda NLP"

    def mark_active(self, request, queryset):
        queryset.update(is_active=True)
        nlp_engine.build_index()
        self.message_user(request, "Preguntas activadas.")
    mark_active.short_description = "Activar seleccionados"

    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)
        nlp_engine.build_index()
        self.message_user(request, "Preguntas desactivadas.")
    mark_inactive.short_description = "Desactivar seleccionados"

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        nlp_engine.build_index()


@admin.register(AcademicCalendar)
class AcademicCalendarAdmin(admin.ModelAdmin):
    list_display = ('title', 'period', 'event_type', 'start_date', 'end_date', 'is_active')
    list_filter = ('period', 'event_type', 'is_active')
    search_fields = ('title', 'description', 'period')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        nlp_engine.build_index()


@admin.register(CourseSchedule)
class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_name', 'section', 'professor', 'days_and_time', 'classroom', 'period', 'is_active')
    list_filter = ('period', 'is_active')
    search_fields = ('course_code', 'course_name', 'professor', 'classroom')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        nlp_engine.build_index()


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'processing_time', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'requirements', 'steps')
    list_editable = ('is_active',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        nlp_engine.build_index()


@admin.register(BotConfig)
class BotConfigAdmin(admin.ModelAdmin):
    list_display = ('bot_name', 'university_name', 'ai_provider', 'confidence_threshold')

    def has_add_permission(self, request):
        # Solo permitir 1 registro de configuración
        return not BotConfig.objects.exists()


class ChatMessageInline(admin.TabularInline):
    model = ChatMessage
    extra = 0
    readonly_fields = ('sender', 'message', 'confidence_score', 'matched_faq', 'feedback', 'created_at')
    can_delete = False


@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ('session_id_short', 'user_ip', 'total_messages', 'created_at', 'last_activity')
    inlines = [ChatMessageInline]
    readonly_fields = ('session_id', 'user_ip', 'created_at', 'last_activity')

    def session_id_short(self, obj):
        return f"{obj.session_id[:12]}..."
    session_id_short.short_description = "ID de Sesión"

    def total_messages(self, obj):
        return obj.messages.count()
    total_messages.short_description = "Mensajes"


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ('sender_badge', 'message_snippet', 'confidence_display', 'matched_faq', 'feedback', 'created_at')
    list_filter = ('sender', 'feedback', 'created_at')
    search_fields = ('message',)
    readonly_fields = ('session', 'sender', 'message', 'matched_faq', 'confidence_score', 'feedback', 'created_at')

    def message_snippet(self, obj):
        return obj.message[:60] + ("..." if len(obj.message) > 60 else "")
    message_snippet.short_description = "Mensaje"

    def sender_badge(self, obj):
        if obj.sender == 'user':
            return format_html('<span style="color:#2563eb; font-weight:bold;">👤 Alumno</span>')
        return format_html('<span style="color:#059669; font-weight:bold;">🤖 Bot</span>')
    sender_badge.short_description = "Emisor"

    def confidence_display(self, obj):
        if obj.sender == 'user':
            return "-"
        score = obj.confidence_score * 100
        color = "#16a34a" if score >= 40 else ("#ca8a04" if score >= 20 else "#dc2626")
        return format_html(f'<span style="color:{color}; font-weight:bold;">{score:.1f}%</span>')
    confidence_display.short_description = "Confianza NLP"


# Personalización del panel de Django Admin
admin.site.site_header = "Portal de Administración - Asistente Universitario IA"
admin.site.site_title = "Admin Asistente Universitario"
admin.site.index_title = "Gestión de Base de Conocimientos y Consultas de Alumnos"
