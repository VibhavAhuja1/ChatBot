from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatHistory
from langchain_ollama import ChatOllama
from .serializers import ChatHistoryList,ChatHistorySerializer

@api_view(['POST'])
def chat(request):
    user_text = request.data.get('text')
    
    if user_text:
        # Initialize ChatOllama and get response
        model = ChatOllama(model='llama3.2:1b')
        response = model.invoke(user_text).content

        # Save the interaction to the database
        chat_entry = ChatHistory.objects.create(user_text=user_text, response_text=response)

        return Response({'user': user_text, 'response': response})

    return Response({"error": "No text provided"}, status=400)