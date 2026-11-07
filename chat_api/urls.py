from django.urls import path
from .views import ChatAPIView, ConfigAPIView, FeedbackAPIView, KnowledgeDirectoryAPIView

app_name = 'chat_api'

urlpatterns = [
    path('chat/', ChatAPIView.as_view(), name='chat'),
    path('config/', ConfigAPIView.as_view(), name='config'),
    path('feedback/', FeedbackAPIView.as_view(), name='feedback'),
    path('directory/', KnowledgeDirectoryAPIView.as_view(), name='directory'),
]
