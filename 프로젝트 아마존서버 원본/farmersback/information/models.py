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
    laundryday00_value = models.TextField()  
    laundryday00_comment = models.TextField() 
    laundryday01_value = models.TextField()
    laundryday01_comment = models.TextField()
    laundryday02_value = models.TextField() 
    laundryday02_comment = models.TextField()
    udday00_value = models.TextField() 
    udday00_comment = models.TextField()
    udday01_value = models.TextField() 
    udday01_comment = models.TextField()
    udday02_value = models.TextField()
    udday02_comment = models.TextField()
    yesterday_name = models.TextField() 
    yesterday_tmax = models.TextField() 
    yesterday_tmin = models.TextField()
    today_name = models.TextField() 
    today_tmax = models.TextField()
    today_tmin = models.TextField()
    tomorrow_name = models.TextField()
    tomorrow_tmax = models.TextField()
    tomorrow_tmin = models.TextField()
    dayAfterTomorrow_name = models.TextField() 
    dayAfterTomorrow_tmax = models.TextField() 
    dayAfterTomorrow_tmin = models.TextField()

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
