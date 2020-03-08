from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.sns_create),
    path('todocreate/', views.todo_create),
    path('snscreate/', views.snscreate),
    path('snslist/', views.snslist),
    path('<int:id>/commentcreate/', views.commentcreate),
    path('<int:id>/comment/', views.comment),
    path('<int:id>/snsdelete/', views.snsdelete),
]
