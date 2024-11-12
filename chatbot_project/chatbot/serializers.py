from rest_framework import serializers
from .models import ChatHistory
from rest_framework.generics import ListAPIView
from .models import ChatHistory

class ChatHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatHistory
        fields = ['user_text', 'response_text', 'created_at']


class ChatHistoryList(ListAPIView):
    queryset = ChatHistory.objects.all().order_by('-created_at')
    serializer_class = ChatHistorySerializer
