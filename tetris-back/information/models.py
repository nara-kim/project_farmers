from django.db import models

# Create your models here.

class NewsInfo(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    created_date = models.CharField(max_length=50)  
    newsimg = models.TextField()
    newslink = models.TextField()

class WeatherInfo(models.Model):
    loaction = models.TextField()
    sky = models.TextField()  
    tc = models.TextField()  
    tmin = models.TextField()  
    tmx = models.TextField()  
    timerelease = models.TextField()  

class DustInfo(models.Model):
    # 순서대로
    # 측정소정보, 측정시간, 초미세먼지, 초미세먼지24시간, 적당한미세먼지, 적당한미세먼지24시간, 오존농도, 이산화질소농도, 아황산가스농도, 통합대기
    stationname = models.TextField()  
    dataTime = models.TextField()    
    pm25Value = models.TextField()  
    pm25Value24 = models.TextField()
    pm10Value = models.TextField()
    pm10Value24 = models.TextField()
    o3Value = models.TextField()  
    no2Value = models.TextField()  
    so2Value = models.TextField() 
    khaiValue = models.TextField()

class MapInfo(models.Model):
    location = models.TextField()