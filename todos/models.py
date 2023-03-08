from django.db import models

# Create your models here.
class Todo(models.Model):
    author = models.CharField(max_length=50)
    body = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)