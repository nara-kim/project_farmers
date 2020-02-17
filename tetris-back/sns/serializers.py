from rest_framework import serializers
from .models import Sns, Todo, SnsModel, CommentModel


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'completed']

class SnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SnsModel
        fields = ['id', 'title', 'user', 'image']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentModel
        fields = ['id', 'content', 'create_date', 'sns', 'create_user']