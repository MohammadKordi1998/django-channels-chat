from uuid import uuid4

from django.db import models

from users.models import UsersModel


class ChatModel(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)

    text = models.CharField(max_length=3000)
    user_sender = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='user_sender')
    user_receiver = models.ForeignKey(UsersModel, on_delete=models.CASCADE, related_name='user_receiver')
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'chat'
