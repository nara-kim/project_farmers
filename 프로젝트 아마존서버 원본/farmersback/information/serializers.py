from rest_framework import serializers
from .models import NewsInfo, WeatherInfo, DustInfo, WeatherNoticeInfo
class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsInfo
        fields = ('id', 'title', 'discription', 'created_date', 
                    'newsimg', 'newslink')
                    
class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherInfo
        fields = ('id', 'loaction', 'sky', 'tc', 'tmin', 'tmx', 'timerelease', 'laundryday00_value', 'laundryday00_comment'
                  ,'laundryday01_value', 'laundryday01_comment', 'laundryday02_value', 'laundryday02_comment'
                 ,'udday00_value' ,'udday00_comment' ,'udday01_value' ,'udday01_comment' ,'udday02_value','udday02_comment'
                 ,'yesterday_name' ,'yesterday_tmax' ,'yesterday_tmin','today_name' ,'today_tmax','today_tmin'
                    ,'tomorrow_name','tomorrow_tmax','tomorrow_tmin','dayAfterTomorrow_name' ,'dayAfterTomorrow_tmax','dayAfterTomorrow_tmin'
                )

class WeatherNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherNoticeInfo
        fields = ('id', 'content', 'year', 'day', 'month', 'time')

class DustSerializer(serializers.ModelSerializer):
    class Meta:
        model = DustInfo
        fields = ('id', 'stationname', 'dataTime', 'pm25Value', 'pm25Value24', 'pm10Value', 'pm10Value24', 'o3Value',
                    'no2Value', 'so2Value', 'khaiValue')


