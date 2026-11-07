from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from knowledge_base.views import demo_portal_view, presentation_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chat_api.urls')),
    path('', demo_portal_view, name='demo_portal'),
    path('presentacion/', presentation_view, name='presentation'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
