from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class HelpModel(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    help_select = models.CharField(max_length=50)
    people = models.IntegerField()
    title = models.CharField(max_length=50)
    location1 = models.CharField(max_length=50)
    location2 = models.CharField(max_length=50)
    help_date = models.CharField(max_length=50)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=50)