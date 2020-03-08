from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.help_create),
    path('gethelp/', views.gethelp),
    path('locationhelp/', views.locationhelp),
    path('helpdetail/<int:id>/', views.helpdetail),

]
