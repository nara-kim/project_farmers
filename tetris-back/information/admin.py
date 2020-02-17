from django.contrib import admin
from .models import WeatherInfo, NewsInfo, DustInfo, PriceInfo, WeatherNoticeInfo

# Register your models here.

admin.site.register(WeatherInfo)
admin.site.register(NewsInfo)
admin.site.register(DustInfo)
admin.site.register(PriceInfo)
admin.site.register(WeatherNoticeInfo)
# admin.site.register(MapInfo)