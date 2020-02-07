from django.shortcuts import render
from .models import NewsInfo, WeatherInfo, DustInfo, PriceInfo
from .serializers import NewsSerializer, WeatherSerializer, DustSerializer, PriceSerializer
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen, re
import xml.etree.ElementTree as elemTree
import json
from django.http import JsonResponse, HttpResponse
import datetime
import numpy as np
import imageio
import os
from PIL import Image



day = clock = (datetime.datetime.now()).strftime('%d')
month = clock = (datetime.datetime.now()).strftime('%m')

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



# class WeatherList(generics.ListAPIView):
    
#     # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
#     # response_body = response.json()

#     # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
#     # sky = response_body['weather']['hourly'][0]['sky']['name']

#     # tc = response_body['weather']['hourly'][0]['temperature']['tc']
#     # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
#     # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
#     # timerelease = response_body['weather']['hourly'][0]['timeRelease']

#     # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)
    
#     queryset = WeatherInfo.objects.all()
#     serializer_class = WeatherSerializer


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
    

class PriceList(generics.ListAPIView):
    # url = 'http://www.kamis.or.kr/service/price/xml.do?action=dailyPriceByCategoryList&p_product_cls_code=01&p_country_code=1101&p_regday=2020-{}-{}&p_convert_kg_yn=N&p_item_category_code=500&p_cert_key=dcdfccb3-6d9d-4472-9bdf-53f25c139663&p_cert_id=222&p_returntype=xml'.format(month, day)
    # xml_data = urlopen(url).read().decode('utf8')
    # data = elemTree.fromstring(xml_data)
    # item = data.find('./data')
    

    # finallist = []
    # for i in item.findall("./item"):
    #     temp = []
    #     temp.append(i.find("./kind_name").text)
    #     temp.append(i.find("./rank").text)
    #     temp.append(i.find("./unit").text)
    #     temp.append(i.find("./dpr1").text)
    #     finallist.append("/")
    #     finallist.append(temp)
    # PriceInfo.objects.create(test=finallist)

    queryset = PriceInfo.objects.all()
    serializer_class = PriceSerializer

# 실시간으로 위치기반해서 데이터 가져오기
@api_view(['GET'])
def WeatherliveList(request):
    print("@@@@@@@@@@@@@@")
    # lat = request.GET.get('Lat')
    # lon = request.GET.get('Lon')

    # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(lat, lon))
    # response_body = response.json()

    # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    # sky = response_body['weather']['hourly'][0]['sky']['name']

    # tc = response_body['weather']['hourly'][0]['temperature']['tc']
    # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    # timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # weatherdata = {'loaction': loaction, 'sky': sky, 'tc': tc, 'tmin': tmin, 'tmx': tmx, 'timerelease':timerelease}
    # # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)
    # return JsonResponse(weatherdata)

class WeatherList(generics.ListAPIView):
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.219839&lon=126.854098')
    # response_body = response.json()

    # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    # sky = response_body['weather']['hourly'][0]['sky']['name']

    # tc = response_body['weather']['hourly'][0]['temperature']['tc']
    # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    # timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)    
    # queryset = WeatherInfo.objects.all()
    # serializer_class = WeatherSerializer




@api_view(['GET'])
def MapList(request):

    print(111111111111111)
    # aaa = request.GET.get('aaa')
    # bbb = request.GET.get('bbb')
    # # print(aaa)

    # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(aaa, bbb))
    # response_body = response.json()

    # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    # sky = response_body['weather']['hourly'][0]['sky']['name']

    # tc = response_body['weather']['hourly'][0]['temperature']['tc']
    # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    # timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # weatherdata = {'loaction': loaction, 'sky': sky, 'tc': tc, 'tmin': tmin, 'tmx': tmx, 'timerelease':timerelease}
    
    # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)
    # return JsonResponse(weatherdata)


    
# def rainraderinfo(request):

def rainraderinfo(request):
    
    #  # 승재
    # base_dir = 'C:/Users/multicampus/seungjae/2월/테트리스 2월 시작/tetris-front/public/img'

    # #승규
    # base_dir = 'C:/Users/saffy/2학기프로젝트/s02p13c104/테트리스 2월 시작/tetris-front/public/img'

    # # 효진
    # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-front/public/img'

    # #나라
    # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-front/public/img'


    # os.chdir(base_dir)
    
    # url = 'http://apis.data.go.kr/1360000/RadarImgInfoService/getCmpImg?serviceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&pageNo=1&numOfRows=10&dataType=XML&data=CMP_WRC&time=2020{}{}'.format(month, day)
    # xml_data = urlopen(url).read().decode('utf8')

    # data = elemTree.fromstring(xml_data)
    # item = data.find('./body/items/item')

    # img_file_lst = []
    
    # clock = int((datetime.datetime.now()).strftime('%H'))
    # if clock == 0:
    #     img = Image.open('rainrader.png')
    #     img.save('rainrader.gif')
    # else:
    #     for i in range(-1, -10, -1):
    #         img_file_lst.append(item[i].text)
    #     img_file_list = img_file_lst.sort()
    #     img_file_to_gif(img_file_lst, "rainrader.gif")
        
    # # 승재
    # base_dir = 'C:/Users/multicampus/seungjae/2월/테트리스 2월 시작/tetris-back'

    # #승규
    # base_dir = 'C:/Users/saffy/2학기프로젝트/s02p13c104/테트리스 2월 시작/tetris-back'
    
    # # 효진
    # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-back'

    # #나라
    # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-back'

    # os.chdir(base_dir)

    weatherdata = {'title': 1}
    return JsonResponse(weatherdata)

# def img_file_to_gif(img_files, output_file_name):
#     imgs_array = [np.array(imageio.imread(img_file)) for img_file in img_files]
#     imageio.mimsave(output_file_name, imgs_array, duration=0.5)
    

