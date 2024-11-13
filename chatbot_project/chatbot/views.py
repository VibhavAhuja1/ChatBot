from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatHistory
import ollama
from langchain_ollama import ChatOllama
from .serializers import ChatHistoryList,ChatHistorySerializer
 
 
 
def chatbot(request):
    """
    Render the frontend for the chatbot.
    """
    return render(request, 'index.html')
 
 
 
 
@api_view(['POST'])
def chat(request):
    user_text = request.data.get('text')
   
    if user_text:
        # Initialize ChatOllama and get response
        model = ChatOllama(model='llama3.2:1b')
        response = model.invoke(user_text).content
        print(response)
 
        return Response({'response': response})
 
    return Response({"error": "No text provided"}, status=400)