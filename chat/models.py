from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    time = models.DateTimeField(default=now)
    # ChatGPT response
    response = models.TextField()
