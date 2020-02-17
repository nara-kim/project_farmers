from django.db import models
from django.contrib.auth import get_user_model

from imagekit.processors import ResizeToFill
from imagekit.models import ProcessedImageField
# Create your models here.



class Sns(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="snsuser")
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

class Todo(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


class SnsModel(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='posts'
    )
    title = models.CharField(max_length=100)
    image = ProcessedImageField(
        processors= [ResizeToFill(300,300)],
        format= 'JPEG',
        options= {'quality': 90},
        upload_to= 'media',
    )

class CommentModel(models.Model):
    content = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    sns = models.ForeignKey(SnsModel, on_delete=models.CASCADE)
    create_user = models.ForeignKey(
        get_user_model(),
        on_delete= models.CASCADE,
    )