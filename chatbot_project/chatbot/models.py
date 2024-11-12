from django.db import models

class ChatHistory(models.Model):
    user_text = models.TextField()
    response_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)