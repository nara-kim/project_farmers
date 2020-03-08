from django.db import models
from django.contrib.auth.models import AbstractUser

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
# Create your models here.

class User(AbstractUser):
    nickname = models.CharField(max_length=50)

    image = ProcessedImageField(
    processors= [ResizeToFill(300,300)],
    format= 'JPEG',
    options= {'quality': 90},
    upload_to= 'media',
    )
    def __str__(self):
        return self.username



