from django.shortcuts import render
from .models import NewsInfo, WeatherInfo, DustInfo, MapInfo
from .serializers import NewsSerializer, WeatherSerializer, DustSerializer, MapSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from bs4 import BeautifulSoup
import requests
from django.http import JsonResponse, HttpResponse

# 이미지 수정
class NewsList(generics.ListCreateAPIView):
    # url = "http://www.newsfarm.co.kr/news/articleList.html?view_type=sm"
    # page = requests.get(url)
    # for i in range(1, 6):
    #     soup = BeautifulSoup(page.content, 'html.parser')
        
    #     title = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-titles > a > strong'.format(i))[0].get_text().strip()
    #     title = title.encode('euc-kr','ignore').decode('euc-kr')
        
    #     discription = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > p > a'.format(i))[0].get_text().strip()        
    #     discription = discription.encode('euc-kr','ignore').decode('euc-kr')
        
    #     created_date = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-dated'.format(i))[0].get_text().strip()
    #     created_date = created_date.encode('euc-kr','ignore').decode('euc-kr')
        
    #     temp = str(soup.select("#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-titles > a".format(i))[0])
    #     temp = temp.encode('euc-kr','ignore').decode('euc-kr')
    #     temp_length = len(temp)
    #     link = "http://www.newsfarm.co.kr"
    #     break_point = 0
    #     for i in range(temp_length):
    #         if temp[i] == '/' and temp[i+1] == 'n':
    #             for t in range(i, temp_length):
    #                 link += temp[t]
    #                 if temp[t+1] == '"' and temp[t+2] == ' ':
    #                     break_point = 1
    #                     break
    #             if break_point == 1:
    #                 break

    #     img = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + title
    #     img = requests.get(img)
    #     img = BeautifulSoup(img.content, 'html.parser')
    #     if len(img.select('#sp_nws1 > div > a > img')) == 1:
    #         tmp = str(img.select('#sp_nws1 > div > a > img')[0])
    #         length = len(tmp)
    #         img = ""
    #         checkpoint = 0
    #         for j in range(length):
    #             if tmp[j] == "h" and tmp[j+1] == "t" and tmp[j+2] == "t":
    #                 for x in range(j, length):
    #                     img += tmp[x]
    #                     if tmp[x] == "g" and tmp[x-1] =="p" and tmp[x-2] == "j" and tmp[x-3] == ".": 
    #                         checkpoint = 1
    #                         break
    #                 if checkpoint == 1:
    #                     break
    #     else:
    #         img = "https://previews.123rf.com/images/ittipol/ittipol1607/ittipol160700133/60202028-%EC%8C%80-%EB%86%8D%EC%82%AC-%EC%9E%91%EC%97%85.jpg"

    #     NewsInfo.objects.create(title=title, discription=discription, created_date=created_date, newslink=link, newsimg=img)

    queryset = NewsInfo.objects.all()
    serializer_class = NewsSerializer



class WeatherList(generics.ListAPIView):
    
    # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
    # response_body = response.json()

    # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    # sky = response_body['weather']['hourly'][0]['sky']['name']

    # tc = response_body['weather']['hourly'][0]['temperature']['tc']
    # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    # timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)
    
    queryset = WeatherInfo.objects.all()
    serializer_class = WeatherSerializer


class DustList(generics.ListAPIView):
    # # 측정소 이름
    # url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX=182762.385094418788&tmY=189606.15128087346&ServiceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&_returnType=json"
    # r = requests.get(url)
    # response_body = r.json()
    # stationname= response_body["list"][0]["stationName"]

    # # 나머지 데이터
    # url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName=%EC%98%A4%EC%84%A0%EB%8F%99&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&ver=1.3&_returnType=json"
    # r = requests.get(url)
    # response_body = r.json()
    
    # dataTime  = response_body['list'][0]["dataTime"]
    # pm25Value  = response_body['list'][0]["pm25Value"]
    # pm25Value24  = response_body['list'][0]["pm25Value24"]
    # pm10Value  = response_body['list'][0]["pm10Value"]
    # pm10Value24  = response_body['list'][0]["pm10Value24"]
    # o3Value  = response_body['list'][0]["o3Value"]
    # no2Value  = response_body['list'][0]["no2Value"]
    # so2Value  = response_body['list'][0]["so2Value"]
    # khaiValue  = response_body['list'][0]["khaiValue"]

    # DustInfo.objects.create(stationname=stationname, dataTime=dataTime, pm25Value=pm25Value, pm25Value24=pm25Value24, pm10Value=pm10Value, pm10Value24=pm10Value24,
    #                         o3Value=o3Value, no2Value=no2Value, so2Value=so2Value, khaiValue=khaiValue)

    
    queryset = DustInfo.objects.all()
    serializer_class = DustSerializer
    


# class MapList(generics.ListAPIView):    
#     # MapInfo.objects.create(location="들어간다 개색기야!!!")
#     queryset = MapInfo.objects.all()
#     serializer_class = MapSerializer



@api_view(['GET'])
def MapList(request):
    print(111111111111111)
    aaa = request.GET.get('aaa')
    bbb = request.GET.get('bbb')

    response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(aaa, bbb))
    response_body = response.json()

    loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    sky = response_body['weather']['hourly'][0]['sky']['name']

    tc = response_body['weather']['hourly'][0]['temperature']['tc']
    tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    timerelease = response_body['weather']['hourly'][0]['timeRelease']

    weatherdata = {'loaction': loaction, 'sky': sky, 'tc': tc, 'tmin': tmin, 'tmx': tmx, 'timerelease':timerelease}
    
    # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)
    return JsonResponse(weatherdata)
