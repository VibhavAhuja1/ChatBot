from django.urls import path
from .views import chat, ChatHistoryList

urlpatterns = [
    path('chat/', chat, name='chat'),
    path('history/', ChatHistoryList.as_view(), name='history'),
]
