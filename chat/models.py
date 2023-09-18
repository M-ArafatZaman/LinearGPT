from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=now)

# Create your models here.
class ChatMessage(models.Model):
    '''
    Either it is a ChatGPT response or a user chat message
    '''
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(default=now)
    # ChatGPT response
    response = models.TextField()
