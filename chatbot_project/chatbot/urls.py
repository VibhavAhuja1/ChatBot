from django.urls import path
from .views import chat, chatbot, chat_history_view
from . import views

urlpatterns = [
    path('', chatbot, name='chatbot'),
    path('chat/', chat, name='chat'),
    path('chat/history', chat_history_view, name='chat_history'),
]