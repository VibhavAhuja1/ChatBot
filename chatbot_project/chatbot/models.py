from django.db import models

class ChatHistory(models.Model):
    sender = models.CharField(max_length=10)  # Example: 'user' or 'bot'
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)  # Already exists
    # Add created_at field
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender}: {self.message[:50]}"
