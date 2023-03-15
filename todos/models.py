from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)