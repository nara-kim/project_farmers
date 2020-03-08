from django.urls import path
from information import views

urlpatterns = [
    path('newsinfo/', views.NewsList.as_view()),
    path('newsinfoList/', views.newsinfoList),


    path('dustinfo/', views.DustList.as_view()),
    path('dustinfoList/', views.dustinfoList),
    path('dustliveinfo/', views.dustliveinfo),


    path('WeatherNotice/', views.WeatherNotice.as_view()),
    path('WeathernoticeList/', views.WeathernoticeList),


    path('weatherinfo/', views.WeatherList.as_view()),
    path('weatherinfoList/', views.weatherinfoList),
    path('weatherliveinfo/', views.weatherliveinfo),
    
    path('rainraderinfo/', views.rainraderinfo),
    path('sickinfo/', views.SickList),
    path('buginfo/', views.BugList),
]

