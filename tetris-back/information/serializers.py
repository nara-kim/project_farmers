from rest_framework import serializers
from .models import NewsInfo, WeatherInfo, DustInfo, PriceInfo
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = ('id', 'title', 'discription', 'created_date', 
                    'newsimg', 'newslink')
                    
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ('id', 'loaction', 'sky', 'tc', 'tmin', 'tmx', 'timerelease')

class DustSerializer(serializers.ModelSerializer):
    class Meta:
        model = DustInfo
        fields = ('id', 'stationname', 'dataTime', 'pm25Value', 'pm25Value24', 'pm10Value', 'pm10Value24', 'o3Value',
                    'no2Value', 'so2Value', 'khaiValue')

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceInfo
        fields = ('id', 'test')
        # fields = ('id', 'itemname', 'kindname', 'rank', 'unit', 'day1', 'dpr1' ,'day2' ,'dpr2' ,'day3' 
        #          ,'dpr3' ,'day4' ,'dpr4' ,'day5' ,'dpr5' ,'day6' ,'dpr6' ,'day7' ,'dpr7')


# class MapSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MapInfo
#         fields = ('id', 'location')