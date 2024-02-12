# chat/models.py
from django.db import models
from accounts.models import CustomUser

class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='chats')
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='admin_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_admin_message = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.timestamp}"

    class Meta:
        ordering = ['-timestamp']
