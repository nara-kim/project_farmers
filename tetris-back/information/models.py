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

# class RainraderInfo(models.Model):
#     raderimg = models.TextField()

class WeatherNoticeInfo(models.Model):
    content = models.TextField()
    year = models.TextField()
    month = models.TextField()
    day = models.TextField()
    time = models.TextField()


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

class BugInfo(models.Model):
    cropname = models.CharField(max_length=10)
    sickname = models.CharField(max_length=10)
    image = models.TextField()
    symptom = models.TextField()
    condition = models.TextField()
    prevent = models.TextField()



class PriceInfo(models.Model):
    test = models.TextField()
    # itemname = models.TextField()
    # kindname = models.TextField()
    # rank = models.TextField()
    # unit = models.TextField()
    # day1 = models.TextField()
    # dpr1 = models.TextField()
    # day2 = models.TextField()
    # dpr2 = models.TextField()
    # day3 = models.TextField()
    # dpr3 = models.TextField()
    # day4 = models.TextField()
    # dpr4 = models.TextField()
    # day5 = models.TextField()
    # dpr5 = models.TextField()
    # day6 = models.TextField()
    # dpr6 = models.TextField()
    # day7 = models.TextField()
    # dpr7 = models.TextField()
    # itemname = models.TextField()
    # kindname = models.TextField()
    # rank = models.TextField()
    # unit = models.TextField()
    # day1 = models.TextField()
    # dpr1 = models.TextField()
    # day2 = models.TextField()
    # dpr2 = models.TextField()
    # day3 = models.TextField()
    # dpr3 = models.TextField()
    # day4 = models.TextField()
    # dpr4 = models.TextField()
    # day5 = models.TextField()
    # dpr5 = models.TextField()
    # day6 = models.TextField()
    # dpr6 = models.TextField()
    # day7 = models.TextField()
    # dpr7 = models.TextField()



# class MapInfo(models.Model):
#     location = models.TextField()
#     degree = models.TextField()