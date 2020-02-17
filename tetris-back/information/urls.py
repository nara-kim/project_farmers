from django.urls import path
from information import views

urlpatterns = [
    path('newsinfo/', views.NewsList.as_view()),
    path('WeatherNotice/', views.WeatherNotice.as_view()),
    path('weatherinfo/', views.WeatherList.as_view()),
    path('weatherinfolive/', views.WeatherliveList),
    path('rainraderinfo/', views.rainraderinfo),
    path('dustinfo/', views.DustList.as_view()),
    path('priceinfo/', views.PriceList.as_view()),
    path('mapinfo/', views.MapList),
    path('sickinfo/', views.SickList),
    path('WeathernoticeList/', views.WeathernoticeList),
    path('buginfo/', views.BugList),
]

