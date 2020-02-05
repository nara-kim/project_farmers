from rest_framework import serializers
from .models import Sns, Todo

class SnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sns
        fields = ['id', 'user', 'title', 'completed']

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'user', 'title', 'completed']