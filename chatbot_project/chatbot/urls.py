from django.urls import path
from .views import chat, ChatHistoryList, chatbot
 
urlpatterns = [
    path('', chatbot, name='chatbot'),
    path('chat/', chat, name='chat'),
    path('history/', ChatHistoryList.as_view(), name='history'),
]