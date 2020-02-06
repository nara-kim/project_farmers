from django.urls import path
from information import views

urlpatterns = [
    path('newsinfo/', views.NewsList.as_view()),
    path('weatherinfo/', views.WeatherList.as_view()),
    path('dustinfo/', views.DustList.as_view()),
    path('priceinfo/', views.PriceList.as_view()),
    path('mapinfo/', views.MapList),
]

