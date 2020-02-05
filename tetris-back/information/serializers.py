from rest_framework import serializers
from .models import NewsInfo, WeatherInfo, DustInfo, MapInfo
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


class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapInfo
        fields = ('id', 'location')