from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.sns_create),
    path('todocreate/', views.todo_create),
]
