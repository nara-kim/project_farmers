from django.shortcuts import render
from .models import NewsInfo, WeatherInfo, DustInfo, WeatherNoticeInfo, BugInfo
from .serializers import NewsSerializer, WeatherSerializer, DustSerializer, WeatherNoticeSerializer
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



day = (datetime.datetime.now()).strftime('%d')
month = (datetime.datetime.now()).strftime('%m')

# 뉴스 뿌리기
class NewsList(generics.ListCreateAPIView):
    queryset = NewsInfo.objects.all().order_by('-id')[:6]
    serializer_class = NewsSerializer

# 뉴스 실시간으로 받아오기
@api_view(['GET'])
def newsinfoList(request):
    url = "http://www.newsfarm.co.kr/news/articleList.html?view_type=sm"
    page = requests.get(url)
    for i in range(1, 7):
        soup = BeautifulSoup(page.content, 'html.parser')
        
        title = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-titles > a > strong'.format(i))[0].get_text().strip()
        title = title.encode('euc-kr','ignore').decode('euc-kr')
        
        discription = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > p > a'.format(i))[0].get_text().strip()        
        discription = discription.encode('euc-kr','ignore').decode('euc-kr')
        
        created_date = soup.select('#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-dated'.format(i))[0].get_text().strip()
        created_date = created_date.encode('euc-kr','ignore').decode('euc-kr')
        
        temp = str(soup.select("#user-container > div.posi-re.float-center.width-1080 > div > div.user-content > section > article > div.article-list > section > div:nth-child({}) > div.list-titles > a".format(i))[0])
        temp = temp.encode('euc-kr','ignore').decode('euc-kr')
        temp_length = len(temp)
        link = "http://www.newsfarm.co.kr"
        break_point = 0
        for i in range(temp_length):
            if temp[i] == '/' and temp[i+1] == 'n':
                for t in range(i, temp_length):
                    link += temp[t]
                    if temp[t+1] == '"' and temp[t+2] == ' ':
                        break_point = 1
                        break
                if break_point == 1:
                    break

        img = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=" + title
        img = requests.get(img)
        img = BeautifulSoup(img.content, 'html.parser')
        if len(img.select('#sp_nws1 > div > a > img')) == 1:
            tmp = str(img.select('#sp_nws1 > div > a > img')[0])
            length = len(tmp)
            img = ""
            checkpoint = 0
            for j in range(length):
                if tmp[j] == "h" and tmp[j+1] == "t" and tmp[j+2] == "t":
                    for x in range(j, length):
                        img += tmp[x]
                        if tmp[x] == "g" and tmp[x-1] =="p" and tmp[x-2] == "j" and tmp[x-3] == ".": 
                            checkpoint = 1
                            break
                    if checkpoint == 1:
                        break
        else:
            img = "https://previews.123rf.com/images/ittipol/ittipol1607/ittipol160700133/60202028-%EC%8C%80-%EB%86%8D%EC%82%AC-%EC%9E%91%EC%97%85.jpg"

        NewsInfo.objects.create(title=title, discription=discription, created_date=created_date, newslink=link, newsimg=img)
    return JsonResponse({"ASDF":"ASDf"})


# 미세먼지 DB데이터 뿌리기
class DustList(generics.ListAPIView):  
    queryset = DustInfo.objects.all().order_by('-id')[:1]
    serializer_class = DustSerializer

# 미세먼지 시간마다 만들기
@api_view(['GET'])
def dustinfoList(request):
    stationname= "오선동"
    # 나머지 데이터
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={}&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&ver=1.3&_returnType=json".format(stationname)
    r = requests.get(url)
    response_body = r.json()

    dataTime  = response_body['list'][0]["dataTime"]
    pm25Value  = response_body['list'][0]["pm25Value"]
    pm25Value24  = response_body['list'][0]["pm25Value24"]
    pm10Value  = response_body['list'][0]["pm10Value"]
    pm10Value24  = response_body['list'][0]["pm10Value24"]
    o3Value  = response_body['list'][0]["o3Value"]
    no2Value  = response_body['list'][0]["no2Value"]
    so2Value  = response_body['list'][0]["so2Value"]
    khaiValue  = response_body['list'][0]["khaiValue"]

    DustInfo.objects.create(stationname=stationname, dataTime=dataTime, pm25Value=pm25Value, pm25Value24=pm25Value24, pm10Value=pm10Value, pm10Value24=pm10Value24,
                            o3Value=o3Value, no2Value=no2Value, so2Value=so2Value, khaiValue=khaiValue)
    return JsonResponse({"dust":"go"})


# 미세먼지 실시간 뿌리기
def dustliveinfo(request):
    lat = request.GET.get('Lat')
    lon = request.GET.get('Lon')

    url = 'https://dapi.kakao.com//v2/local/geo/transcoord.json?x={}&y={}&input_coord=WGS84&output_coord=TM'.format(lon, lat)
    apikey = "4e7767db576da0ec7a9b59be17992e14"
    r = requests.get( url, headers={'Authorization' : 'KakaoAK ' + apikey })
    response_body = r.json()
    tmx = int(response_body["documents"][0]["y"])
    tmyy = int(response_body["documents"][0]["x"])
 
    # 측정소 이름
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/MsrstnInfoInqireSvc/getNearbyMsrstnList?tmX={}&tmY={}&ServiceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&_returnType=json".format(tmyy, tmx)
    r = requests.get(url)
    response_body = r.json()
    stationname= response_body["list"][0]["stationName"]

    # 나머지 데이터
    url = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?stationName={}&dataTerm=month&pageNo=1&numOfRows=10&ServiceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&ver=1.3&_returnType=json".format(stationname)
    r = requests.get(url)
    response_body = r.json()

    dataTime  = response_body['list'][0]["dataTime"]
    pm25Value  = response_body['list'][0]["pm25Value"]
    pm25Value24  = response_body['list'][0]["pm25Value24"]
    pm10Value  = response_body['list'][0]["pm10Value"]
    pm10Value24  = response_body['list'][0]["pm10Value24"]
    o3Value  = response_body['list'][0]["o3Value"]
    no2Value  = response_body['list'][0]["no2Value"]
    so2Value  = response_body['list'][0]["so2Value"]
    khaiValue  = response_body['list'][0]["khaiValue"]

    return JsonResponse({"dataTime":dataTime, "stationname":stationname, "pm25Value": pm25Value, "pm25Value24": pm25Value24, "pm10Value": pm10Value,
                        "pm10Value24": pm10Value24, "o3Value":o3Value, "no2Value": no2Value, "so2Value": so2Value, "khaiValue": khaiValue
                            })


# 만든 날씨 뿌리기
class WeatherList(generics.ListAPIView):
    queryset = WeatherInfo.objects.all().order_by('-id')[:1]
    serializer_class = WeatherSerializer


#시간마다 날씨정보 만들기 
def weatherinfoList(request):
    response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
    response_body = response.json()

    # 날씨데이터
    loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    sky = response_body['weather']['hourly'][0]['sky']['name']
    tc = response_body['weather']['hourly'][0]['temperature']['tc']
    tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # 빨래지수
    laundry = requests.get('https://apis.openapi.sk.com/weather/index/laundry?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
    laundry_body = laundry.json()
    laundryday00_value = laundry_body['weather']['wIndex']['laundry'][0]['day00']['index']
    laundryday00_comment = laundry_body['weather']['wIndex']['laundry'][0]['day00']['comment']
    laundryday01_value = laundry_body['weather']['wIndex']['laundry'][0]['day01']['index']
    laundryday01_comment = laundry_body['weather']['wIndex']['laundry'][0]['day01']['comment']
    laundryday02_value = laundry_body['weather']['wIndex']['laundry'][0]['day02']['index']
    laundryday02_comment = laundry_body['weather']['wIndex']['laundry'][0]['day02']['comment']
    
    # 자외선지수
    uv = requests.get('https://apis.openapi.sk.com/weather/index/uv?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
    uv_body = uv.json()
    udday00_value = uv_body['weather']['wIndex']['uvindex'][0]['day00']['index']
    udday00_comment = uv_body['weather']['wIndex']['uvindex'][0]['day00']['comment']
    udday01_value = uv_body['weather']['wIndex']['uvindex'][0]['day01']['index']
    udday01_comment = uv_body['weather']['wIndex']['uvindex'][0]['day01']['comment']
    udday02_value = uv_body['weather']['wIndex']['uvindex'][0]['day02']['index']
    udday02_comment = uv_body['weather']['wIndex']['uvindex'][0]['day02']['comment']


    # 간편날씨(어제, 오늘, 내일, 모레)
    summary = requests.get('https://apis.openapi.sk.com/weather/summary?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat=35.205529&lon=126.811509')
    summary_body = summary.json()
    yesterday_name = summary_body['weather']['summary'][0]['yesterday']['sky']['name']
    yesterday_tmax = summary_body['weather']['summary'][0]['yesterday']['temperature']['tmax']
    yesterday_tmin = summary_body['weather']['summary'][0]['yesterday']['temperature']['tmin']
    today_name = summary_body['weather']['summary'][0]['today']['sky']['name']
    today_tmax = summary_body['weather']['summary'][0]['today']['temperature']['tmax']
    today_tmin = summary_body['weather']['summary'][0]['today']['temperature']['tmin']
    tomorrow_name = summary_body['weather']['summary'][0]['tomorrow']['sky']['name']
    tomorrow_tmax = summary_body['weather']['summary'][0]['tomorrow']['temperature']['tmax']
    tomorrow_tmin = summary_body['weather']['summary'][0]['tomorrow']['temperature']['tmin']
    dayAfterTomorrow_name = summary_body['weather']['summary'][0]['dayAfterTomorrow']['sky']['name']
    dayAfterTomorrow_tmax = summary_body['weather']['summary'][0]['dayAfterTomorrow']['temperature']['tmax']
    dayAfterTomorrow_tmin = summary_body['weather']['summary'][0]['dayAfterTomorrow']['temperature']['tmin']

    WeatherInfo.objects.create(loaction=loaction, sky=sky, tc=tc, tmin=tmin, tmx=tmx, timerelease=timerelease, 
                                laundryday00_value=laundryday00_value, laundryday00_comment=laundryday00_comment, 
                                laundryday01_value=laundryday01_value, laundryday01_comment=laundryday01_comment,
                                laundryday02_value=laundryday02_value, laundryday02_comment=laundryday02_comment,
                                udday00_value=udday00_value, udday00_comment=udday00_comment,
                                udday01_value=udday01_value, udday01_comment=udday01_comment,
                                udday02_value=udday02_value, udday02_comment=udday02_comment,
                                yesterday_name=yesterday_name, yesterday_tmax=yesterday_tmax, yesterday_tmin=yesterday_tmin,
                                today_name=today_name, today_tmax=today_tmax, today_tmin=today_tmin,
                                tomorrow_name=tomorrow_name, tomorrow_tmax=tomorrow_tmax, tomorrow_tmin=tomorrow_tmin,
                                dayAfterTomorrow_name=dayAfterTomorrow_name, dayAfterTomorrow_tmax=dayAfterTomorrow_tmax, dayAfterTomorrow_tmin=dayAfterTomorrow_tmin,
                                )
    return JsonResponse({"weather":"go"})

# 위치기반 날시 뿌리기
def weatherliveinfo(request):
    lat = request.GET.get('Lat')
    lon = request.GET.get('Lon')

    # 날씨데이터
    response = requests.get('https://api2.sktelecom.com/weather/current/hourly?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(lat, lon))
    response_body = response.json()
    loaction = response_body['weather']['hourly'][0]['grid']['city'] + response_body['weather']['hourly'][0]['grid']['county'] + response_body['weather']['hourly'][0]['grid']['village']
    sky = response_body['weather']['hourly'][0]['sky']['name']
    tc = response_body['weather']['hourly'][0]['temperature']['tc']
    tmin = response_body['weather']['hourly'][0]['temperature']['tmin']
    tmx = response_body['weather']['hourly'][0]['temperature']['tmax']  
    timerelease = response_body['weather']['hourly'][0]['timeRelease']

    # 빨래지수
    laundry = requests.get('https://apis.openapi.sk.com/weather/index/laundry?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(lat, lon))
    laundry_body = laundry.json()
    laundryday00_value = laundry_body['weather']['wIndex']['laundry'][0]['day00']['index']
    laundryday00_comment = laundry_body['weather']['wIndex']['laundry'][0]['day00']['comment']
    laundryday01_value = laundry_body['weather']['wIndex']['laundry'][0]['day01']['index']
    laundryday01_comment = laundry_body['weather']['wIndex']['laundry'][0]['day01']['comment']
    laundryday02_value = laundry_body['weather']['wIndex']['laundry'][0]['day02']['index']
    laundryday02_comment = laundry_body['weather']['wIndex']['laundry'][0]['day02']['comment']
    
    # 자외선지수
    uv = requests.get('https://apis.openapi.sk.com/weather/index/uv?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(lat, lon))
    uv_body = uv.json()
    udday00_value = uv_body['weather']['wIndex']['uvindex'][0]['day00']['index']
    udday00_comment = uv_body['weather']['wIndex']['uvindex'][0]['day00']['comment']
    udday01_value = uv_body['weather']['wIndex']['uvindex'][0]['day01']['index']
    udday01_comment = uv_body['weather']['wIndex']['uvindex'][0]['day01']['comment']
    udday02_value = uv_body['weather']['wIndex']['uvindex'][0]['day02']['index']
    udday02_comment = uv_body['weather']['wIndex']['uvindex'][0]['day02']['comment']


    # 간편날씨(어제, 오늘, 내일, 모레)
    summary = requests.get('https://apis.openapi.sk.com/weather/summary?appKey=l7xx93f82b03bbea415abb503b02136a2f34&version=1&lat={}&lon={}'.format(lat, lon))
    summary_body = summary.json()
    yesterday_name = summary_body['weather']['summary'][0]['yesterday']['sky']['name']
    yesterday_tmax = summary_body['weather']['summary'][0]['yesterday']['temperature']['tmax']
    yesterday_tmin = summary_body['weather']['summary'][0]['yesterday']['temperature']['tmin']
    today_name = summary_body['weather']['summary'][0]['today']['sky']['name']
    today_tmax = summary_body['weather']['summary'][0]['today']['temperature']['tmax']
    today_tmin = summary_body['weather']['summary'][0]['today']['temperature']['tmin']
    tomorrow_name = summary_body['weather']['summary'][0]['tomorrow']['sky']['name']
    tomorrow_tmax = summary_body['weather']['summary'][0]['tomorrow']['temperature']['tmax']
    tomorrow_tmin = summary_body['weather']['summary'][0]['tomorrow']['temperature']['tmin']
    dayAfterTomorrow_name = summary_body['weather']['summary'][0]['dayAfterTomorrow']['sky']['name']
    dayAfterTomorrow_tmax = summary_body['weather']['summary'][0]['dayAfterTomorrow']['temperature']['tmax']
    dayAfterTomorrow_tmin = summary_body['weather']['summary'][0]['dayAfterTomorrow']['temperature']['tmin']

    weatherdata = {'loaction': loaction, 'sky': sky, 'tc': tc, 'tmin': tmin, 'tmx': tmx, 'timerelease':timerelease, 
                    'laundryday00_value': laundryday00_value, 'laundryday00_comment': laundryday00_comment, 
                    'laundryday01_value': laundryday01_value, 'laundryday01_comment': laundryday01_comment,
                    'laundryday02_value': laundryday02_value, 'laundryday02_comment': laundryday02_comment,
                    'udday00_value': udday00_value, 'udday00_comment': udday00_comment,
                    'udday01_value': udday01_value, 'udday01_comment': udday01_comment,
                    'udday02_value': udday02_value, 'udday02_comment': udday02_comment,
                    'yesterday_name': yesterday_name, 'yesterday_tmax': yesterday_tmax, 'yesterday_tmin': yesterday_tmin,
                    'today_name': today_name, 'today_tmax': today_tmax, 'today_tmin': today_tmin,
                    'tomorrow_name': tomorrow_name, 'tomorrow_tmax': tomorrow_tmax, 'tomorrow_tmin': tomorrow_tmin,
                    'dayAfterTomorrow_name': dayAfterTomorrow_name, 'dayAfterTomorrow_tmax': dayAfterTomorrow_tmax, 'dayAfterTomorrow_tmin': dayAfterTomorrow_tmin,
                    }
    return JsonResponse(weatherdata)


# 레이더 영상 이미지
def rainraderinfo(request):
    url = 'http://apis.data.go.kr/1360000/RadarImgInfoService/getCmpImg?serviceKey=NpK80f5ZwAD0mk%2BZjfrgUPTG3JLqubh%2FIYXSEzEou0kvKMi8ZnNIsv9ud8YF%2Bvyz4oBURYsKS09uXwASEHdr%2FA%3D%3D&pageNo=1&numOfRows=10&dataType=XML&data=CMP_WRC&time=2020{}{}'.format(month, day)
    xml_data = urlopen(url).read().decode('utf8')

    data = elemTree.fromstring(xml_data)
    item = data.find('./body/items/item')
    img_file_lst = []
   
    clock = int((datetime.datetime.now()).strftime('%H'))
    if clock == 0:
        img = Image.open('rainrader.png')
        img.save('rainrader.gif')
    else:
        for i in range(-1, -10, -1):
            img_file_lst.append(item[i].text)
        img_file_lst.sort()
        img_file_to_gif(img_file_lst, "rainrader.gif")
    return JsonResponse({"rain":"go"})

def img_file_to_gif(img_files, output_file_name):
    imgs_array = [np.array(imageio.imread(img_file)) for img_file in img_files]
    imageio.mimsave(output_file_name, imgs_array, duration=0.5)
    


@api_view(['GET'])
def SickList(request):
    html = urlopen("http://www.mafra.go.kr/FMD-AI/")
    
    # bsObject = BeautifulSoup(html, "html.parser") 
    # bsObject = bsObject.select("#menu603_obj175 > div > img")
    # for tag in bsObject:
    #     sickimg = tag.get("src")
    return JsonResponse({"sick":"아프다"})  

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
@api_view(['POST'])
def BugList(request):
    allbug = BugInfo.objects.all()
    cropName = request.POST['selected']
    sickNameKor = request.POST['selected2']

    search = BugInfo.objects.filter(cropname=cropName, sickname=sickNameKor)
    crop = search.values('cropname')[0]["cropname"]
    sick = search.values('sickname')[0]["sickname"]
    condition = search.values('condition')[0]["condition"]
    symptom = search.values('symptom')[0]["symptom"]
    prevent = search.values('prevent')[0]["prevent"]
    image = search.values('image')[0]["image"]
    return JsonResponse({"crop": crop, "sick":sick, "condition":condition, "symptom":symptom, "prevent":prevent, "image":image})

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
