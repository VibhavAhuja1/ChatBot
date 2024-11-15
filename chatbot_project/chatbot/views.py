from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ChatHistory
import ollama
from langchain_ollama import ChatOllama
from .serializers import ChatHistoryList, ChatHistorySerializer
from django.http import JsonResponse
from .models import ChatHistory

def chatbot(request):
    """
    Render the frontend for the chatbot.
    """
    return render(request, 'index.html')

@api_view(['POST','GET'])
def chat(request):
    if request.method == 'GET':
        # Render the frontend for the chatbot when the page is first loaded
        return render(request, 'index.html')
    elif request.method == 'POST':
        # Handle the chat response when a message is sent
        user_text = request.data.get('text')

        if user_text:
            try:
                # Pull the model if it's not available
                ollama.pull("llama3.2:1b")

                # Initialize the ChatOllama model
                model = ChatOllama(model='llama3.2:1b')

                # Get the response from the model
                response = model.invoke(user_text).content
                print('Response:', response)  # Log only the response, no input logging

                return Response({'response': response})

            except Exception as e:
                # Log the exception and return an error response
                print(f"Error invoking model: {e}")
                return Response({"error": "Error generating response"}, status=500)

        return Response({"error": "No text provided"}, status=400)




def chat_history_view(request):
    # Fetch recent chat messages (limit to last 20 for simplicity)
    messages = ChatHistory.objects.all().order_by('-timestamp')[:20]
    chat_history = [
        {'sender': message.sender, 'message': message.message, 'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for message in messages
    ]
    #return render(request, 'chatbot/chat_history.html', {'chat_history': chat_history})
    return render(request, 'chat_history.html', {'chat_history': chat_history})
