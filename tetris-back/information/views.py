from django.shortcuts import render
from .models import NewsInfo, WeatherInfo, DustInfo, PriceInfo, WeatherNoticeInfo, BugInfo
from .serializers import NewsSerializer, WeatherSerializer, DustSerializer, PriceSerializer, WeatherNoticeSerializer
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
    # for i in range(1, 7):
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

    queryset = NewsInfo.objects.all().order_by('-id')[:6]
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
    
    queryset = DustInfo.objects.all().order_by('-id')[:1]
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
    print("@@@@")
    # response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.219839&lon=126.854098')
    # response_body = response.json()

    # loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    # sky = response_body['weather']['hourly'][0]['sky']['name']

    # tc = response_body['weather']['hourly'][0]['temperature']['tc']
    # tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    # tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    # timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease)    
    # queryset = WeatherInfo.objects.all().order_by('-id')[:1]
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
#     # 승재
#     base_dir = 'C:/Users/multicampus/seungjae/2월 3주차/테트리스 2월 시작/tetris-front/public/img'

# #     # #승규
# #     # base_dir = 'C:/Users/saffy/2학기프로젝트/s02p13c104/테트리스 2월 시작/tetris-front/public/img'

# #     # # 효진
# #     # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-front/public/img'

# #     # #나라
# #     # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-front/public/img'


#     os.chdir(base_dir)
    
#     url = 'http://apis.data.go.kr/1360000/RadarImgInfoService/getCmpImg?serviceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&pageNo=1&numOfRows=10&dataType=XML&data=CMP_WRC&time=2020{}{}'.format(month, day)
#     xml_data = urlopen(url).read().decode('utf8')

#     data = elemTree.fromstring(xml_data)
#     item = data.find('./body/items/item')

#     img_file_lst = []
    
#     clock = int((datetime.datetime.now()).strftime('%H'))
#     if clock == 0:
#         img = Image.open('rainrader.png')
#         img.save('rainrader.gif')
#     else:
#         for i in range(-1, -10, -1):
#             img_file_lst.append(item[i].text)
#         img_file_list = img_file_lst.sort()
#         img_file_to_gif(img_file_lst, "rainrader.gif")
        
#     # 승재
#     base_dir = 'C:/Users/multicampus/seungjae/2월 3주차/테트리스 2월 시작/tetris-back'

#     # #승규
#     # base_dir = 'C:/Users/saffy/2학기프로젝트/s02p13c104/테트리스 2월 시작/tetris-back'
    
#     # # 효진
#     # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-back'

#     # #나라
#     # base_dir = 'C:/Users/saffy/프로젝트폴더/s02p13c104/테트리스 2월 시작/tetris-back'

#     os.chdir(base_dir)

    weatherdata = {'title': 1}
    return JsonResponse(weatherdata)

# def img_file_to_gif(img_files, output_file_name):
#     imgs_array = [np.array(imageio.imread(img_file)) for img_file in img_files]
#     imageio.mimsave(output_file_name, imgs_array, duration=0.5)
    



@api_view(['GET'])
def SickList(request):
    html = urlopen("http://www.mafra.go.kr/FMD-AI/")  
    bsObject = BeautifulSoup(html, "html.parser") 
    bsObject = bsObject.select("#menu603_obj175 > div > img")
    for tag in bsObject:
        sickimg = tag.get("src")
    print(sickimg)
    return JsonResponse({"sick":sickimg})  

# 날씨 예보 통보문 실시간으로 데이터 받아오기
@api_view(['GET'])
def WeathernoticeList(request):
    url = 'http://apis.data.go.kr/1360000/VilageFcstMsgService/getWthrSituation?serviceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&pageNo=1&numOfRows=10&dataType=XML&stnId=108'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    content = soup.select('wfSv1')
    content = content[0].get_text()
    date = soup.select('tmFc')
    date = date[0].get_text()
    year = date[:4]
    month = date[4:6]
    day = date[6:8]
    time = date[8::]
    WeatherNoticeInfo.objects.create(content=content, year=year, month=month, day=day, time=time)
    return JsonResponse({"ASDF":"ASDf"})

# 날씨 예보 통보문 데이터 건네주기
class WeatherNotice(generics.ListAPIView):
    queryset = WeatherNoticeInfo.objects.all().order_by('-id')[:1]
    
    serializer_class = WeatherNoticeSerializer


# 병해충 정보
@api_view(['GET'])
def BugList(request):
    allbug = BugInfo.objects.all()
    cropName = request.GET.get('selected')
    sickNameKor = request.GET.get('selected2')

    search = BugInfo.objects.filter(cropname=cropName, sickname=sickNameKor)
    crop = search.values('cropname')[0]["cropname"]
    sick = search.values('sickname')[0]["sickname"]
    condition = search.values('condition')[0]["condition"]
    symptom = search.values('symptom')[0]["symptom"]
    prevent = search.values('prevent')[0]["prevent"]
    image = search.values('image')[0]["image"]
    return JsonResponse({"작물명": crop, "병명":sick, "발생환경":condition, "증상":symptom, "방제방법":prevent, "이미지":image})

# namelist = ['가지', '감', '감귤', '감자', '감초', '갓', '개나리', '거베라', '고구마', '고추'
#             , '고추냉이', '곰취', '과꽃', '관음죽', '구기자', '국화', '군자란', '글라디올러스', '금어초', '금잔화', '은빛담쟁이덩굴', '꽃양배추', '논벼', '다알리아', '당근'
#             , '금잔화', '은빛담쟁이덩굴', '꽃양배추', '논벼', '다알리아', '당근', '대추', '더덕', '도라지', '동백나무', '동양심비', '드라세나', '디펜바키아', '딸기', '마', '마늘'
#             , '매실', '맥문동', '메리골드', '모과', '모란', '몬스테라', '무', '무궁화', '무화과', '문주란', '미나리', '밤', '배', '배추', '백일홍', '백합', '복숭아', '봉선화', '부추', '붓꽃'
#             , '블루베리', '비파', '사과', '산수유', '살구', '삽주', '상추', '샐러리', '샐비어', '생강', '선인장', '소철', '수국', '수박', '순무', '쉐프렐라', '스파티필럼', '시금치', '시써스', '식나무'
#             , '심비디움', '쑥갓', '아나시스', '아레카야자', '아마릴리스', '아스파라가스', '아스파라거스', '아욱', '아이비', '안개꽃', '앵두', '양배추', '양파', '오미자', '오이', '옥수수', '우엉', '유자'
#             , '자두', '작약', '장미', '제라늄', '종려죽', '지치', '지황', '진달래', '참다래', '참당귀(당귀)', '참외', '천궁', '천일홍', '치자나무', '카네이션', '칸나', '케일', '켄차야자', '콩', '클레로덴드럼'
#             , '토마토', '튤립', '파', '파슬리', '팔손이', '패랭이꽃', '팬지', '페튜니아', '포도', '피닉스야자', '해바라기', '협죽도', '호두나무', '호박', '황기'
#               ] 
# result = []
# for i in namelist:
#     url = "http://ncpms.rda.go.kr/npmsAPI/service?apiKey=2020bc251a4e18ca0830201bff4ebe390037&serviceCode=SVC01&serviceType=XML&cropName={}".format(i)
#     res = requests.get(url)
#     soup = BeautifulSoup(res.content, 'html.parser')
#     final = []
#     for item in soup.findAll("item"):
#         sickcode = item.select('sicKKey')
#         sickcode = sickcode[0].get_text()
#         final.append(sickcode)
#     for code in final:
#         ans = []
#         url = "http://ncpms.rda.go.kr/npmsAPI/service?apiKey=2020bc251a4e18ca0830201bff4ebe390037&serviceCode=SVC05&sickKey={}".format(code)
#         res = requests.get(url)
#         soup = BeautifulSoup(res.content, 'html.parser')

#         symptom = soup.select('symptoms')
#         symptom = symptom[0].text
#         symptom = symptom.replace('<br/>', '\n')
        
#         condition = soup.select('developmentCondition')
#         condition = condition[0].text
#         condition = condition.replace('<br/>', '\n')

#         cropname = soup.select('cropName')
#         cropname = cropname[0].text

#         sickname = soup.select('sickNameKor')
#         sickname = sickname[0].text

#         prevent = soup.select('preventionMethod')
#         prevent = prevent[0].text
#         prevent = prevent.replace('<br/>', '')

#         temp = soup.select("imageList > item")[0].text
#         image = ""
#         checkpoint = 0
#         for im in range(len(temp)):
#             if temp[im] == "h" and temp[im+1] == "t":
#                 for x in range(im, len(temp)):
#                     image += temp[x]
#                     if temp[x] == "g" and temp[x-1] == "p" and temp[x-2] == "j" and temp[x-3] == ".":
#                             checkpoint = 1
#                             break
#                 if checkpoint == 1:
#                     break
        
        
#         BugInfo.objects.create(cropname=cropname, sickname=sickname, image=image, symptom=symptom, condition=condition, prevent=prevent)