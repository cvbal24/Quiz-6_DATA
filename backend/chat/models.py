from django.db import models
from users.models import CustomUser


class ChatHistory(models.Model):
    """Track conversation history between user and AI chatbot."""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='chat_history')
    message = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.email} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
