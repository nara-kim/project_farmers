from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class Sns(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="snsuser")
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)