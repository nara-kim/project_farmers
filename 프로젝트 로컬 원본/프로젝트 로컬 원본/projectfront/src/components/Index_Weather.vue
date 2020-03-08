<template>
    <!-- <div class ="container"> -->
        <div class ="container">
        <div style="font-size:2.0em;">날씨</div> <hr style ="background-color: orange;height: 1.5px;">
        <div v-if="geoweatherlist.length === 0">
            <div class ="row" style="border:1px solid #EAEEF3;">
                <div class="col-12" style="border-bottom:1px solid #EAEEF3;">
                    <div class ="col-12write" style="padding-left: 15px;">
                        날씨 ({{weatherlist[0].timerelease}})
                    </div>
                </div>
                <div class="col-sm" id = "picture" >
                    <div class="today_weather">
                        <div v-if="weatherlist[0].sky === '맑음'">
                            <img src = "img/weather/sun.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '구름조금'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '구름많음'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '구름 많고 비'">
                            <img src = "img/weather/cloud-rain.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '구름 많고 눈'">
                            <img src = "img/weather/cloud-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '구름 많고 비 또는 눈'">
                            <img src = "img/weather/rain-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '흐림'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '흐리고 비'">
                            <img src = "img/weather/cloud-rain.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '흐리고 눈'">
                            <img src = "img/weather/cloud-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '흐리고 비 또는 눈'">
                            <img src = "img/weather/rain-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '흐리고 낙뢰'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '뇌우/비'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '뇌우/눈'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="weatherlist[0].sky === '뇌우/비 또는 눈'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else>
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                    </div>
                </div>
                <div class="col-sm" style="height: 150px;">
                    <div class="today_weather">
                        <div>
                            <span style="font-size:35px;">
                                {{weatherlist[0].tc}}
                            </span>
                            <span style="font-size: 27px; font-weight:bold">
                                ℃
                            </span>
                        </div>
                        <div>
                            {{weatherlist[0].sky}}
                        </div>
                        <div>
                            {{weatherlist[0].tmin}}/{{weatherlist[0].tmx}}
                        </div>
                    </div>
                </div>
                <div class="col-sm" style="height: 150px; border-left:1px solid #EAEEF3;">
                    <div class ="today_weather">
                        <div>
                            <span>
                                <img src = "img/weather/laundry.png" width="40px;"> 
                            </span>
                        </div>
                        <div>
                            {{weatherlist[0].laundryday00_comment}}
                        </div>
                        <div>
                            <span>
                                <img src = "img/weather/uv.png" width="40px;">
                            </span>
                        </div>
                        <div>
                            {{weatherlist[0].udday00_comment}}
                        </div>
                    </div>
                </div>
                <div class="col-12" style="border-top:1px solid #EAEEF3; border-bottom:1px solid #EAEEF3;">
                    <div class = "col-12write" style="text-align:center; width:100%;">
                        주간날씨    
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3" >
                    <div class="week_weather">
                        어제날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="weatherlist[0].yesterday_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].yesterday_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].yesterday_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].yesterday_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].yesterday_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].yesterday_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{weatherlist[0].yesterday_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{weatherlist[0].yesterday_tmin}}</span>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                    <div class="week_weather">
                        오늘날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="weatherlist[0].today_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].today_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].today_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].today_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].today_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].today_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{weatherlist[0].today_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{weatherlist[0].today_tmin}}</span>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                    <div class="week_weather">
                        내일날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="weatherlist[0].tomorrow_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].tomorrow_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].tomorrow_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].tomorrow_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].tomorrow_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].tomorrow_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{weatherlist[0].tomorrow_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{weatherlist[0].tomorrow_tmin}}</span>
                        </div>
                    </div>
                </div>
            <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                <div class="week_weather">
                    모레날씨
                </div>
                <div class="week_weather_content">
                        <div v-if="weatherlist[0].dayAfterTomorrow_name === '맑음'">
                        <span>
                            <img src = "img/weather/sun.png" width="30px;">
                        </span>
                        </div>
                        <div v-else-if="weatherlist[0].dayAfterTomorrow_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].dayAfterTomorrow_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].dayAfterTomorrow_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].dayAfterTomorrow_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="weatherlist[0].dayAfterTomorrow_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>

                    <div>
                        <span>최고기온:</span>
                        <span> {{weatherlist[0].dayAfterTomorrow_tmax}}</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> {{weatherlist[0].dayAfterTomorrow_tmin}}</span>
                    </div>
                </div>
            </div>

            </div>
        </div>  
        
        <div v-else>
            <div class ="row" style="border:1px solid #EAEEF3;">
                <div class="col-12" style="border-bottom:1px solid #EAEEF3;">
                    <div class ="col-12write" style="padding-left: 15px;">
                        {{geoweatherlist.loaction}}({{geoweatherlist.timerelease}})
                    </div>
                </div>
                <div class="col-sm" id = "picture" >
                    <div class="today_weather">
                        <div v-if="geoweatherlist.sky === '맑음'">
                            <img src = "img/weather/sun.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '구름조금'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '구름많음'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '구름 많고 비'">
                            <img src = "img/weather/cloud-rain.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '구름 많고 눈'">
                            <img src = "img/weather/cloud-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '구름 많고 비 또는 눈'">
                            <img src = "img/weather/rain-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '흐림'">
                            <img src = "img/weather/cloud.PNG" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '흐리고 비'">
                            <img src = "img/weather/cloud-rain.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '흐리고 눈'">
                            <img src = "img/weather/cloud-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '흐리고 비 또는 눈'">
                            <img src = "img/weather/rain-snow.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '흐리고 낙뢰'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '뇌우/비'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '뇌우/눈'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else-if="geoweatherlist.sky === '뇌우/비 또는 눈'">
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                        <div v-else>
                            <img src = "img/weather/thunder.png" class="picture" width="100px;">
                        </div>
                    </div>
                </div>
                <div class="col-sm" style="height: 150px;">
                    <div class="today_weather">
                        <div>
                            <span style="font-size:35px;">
                                {{geoweatherlist.tc}}
                            </span>
                            <span style="font-size: 27px; font-weight:bold">
                                ℃
                            </span>
                        </div>
                        <div>
                            {{geoweatherlist.sky}}
                        </div>
                        <div>
                            {{geoweatherlist.tmin}}/{{geoweatherlist.tmx}}
                        </div>
                    </div>
                </div>
                <div class="col-sm" style="height: 150px; border-left:1px solid #EAEEF3;">
                    <div class ="today_weather">
                        <div>
                            <span>
                                <img src = "img/weather/laundry.png" width="40px;">
                            </span>
                        </div>
                        <div>
                            {{geoweatherlist.laundryday00_comment}}
                        </div>
                        <div>
                            <span>
                                <img src = "img/weather/uv.png" width="40px;">
                            </span>
                        </div>
                        <div>
                            {{geoweatherlist.udday00_comment}}
                        </div>
                    </div>
                </div>
                <div class="col-12" style="border-top:1px solid #EAEEF3; border-bottom:1px solid #EAEEF3;">
                    <div class = "col-12write" style="text-align:center; width:100%;">
                        주간날씨    
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3" >
                    <div class="week_weather">
                        어제날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="geoweatherlist.yesterday_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.yesterday_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.yesterday_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.yesterday_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.yesterday_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.yesterday_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{geoweatherlist.yesterday_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{geoweatherlist.yesterday_tmin}}</span>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                    <div class="week_weather">
                        오늘날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="geoweatherlist.today_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.today_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.today_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.today_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.today_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.today_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{geoweatherlist.today_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{geoweatherlist.today_tmin}}</span>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                    <div class="week_weather">
                        내일날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="geoweatherlist.tomorrow_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.tomorrow_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.tomorrow_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.tomorrow_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.tomorrow_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.tomorrow_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                        <div>
                            <span>최고기온:</span>
                            <span> {{geoweatherlist.tomorrow_tmax}}</span>
                        </div>
                        <div>
                            <span>최저기온:</span>
                            <span> {{geoweatherlist.tomorrow_tmin}}</span>
                        </div>
                    </div>
                </div>
                <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                     <div class="week_weather">
                        모레날씨
                    </div>
                    <div class="week_weather_content">
                        <div v-if="geoweatherlist.dayAfterTomorrow_name === '맑음'">
                            <span>
                                <img src = "img/weather/sun.png" width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.dayAfterTomorrow_name === '구름조금'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.dayAfterTomorrow_name === '구름많음'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.dayAfterTomorrow_name === '흐림'">
                            <span>
                                <img src = "img/weather/cloud.PNG"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.dayAfterTomorrow_name === '비'">
                            <span>
                                <img src = "img/weather/rain.png"  width="30px;">
                            </span>
                        </div>
                        <div v-else-if="geoweatherlist.dayAfterTomorrow_name === '눈'">
                            <span>
                                <img src = "img/weather/snow.png" width="30px;">
                            </span>
                        </div>
                        <div v-else>
                            <span>
                                <img src = "img/weather/rain-snow.png" width="30px;">
                            </span>
                        </div>
                    <div>
                        <span>최고기온:</span>
                        <span> {{geoweatherlist.dayAfterTomorrow_tmax}}</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> {{geoweatherlist.dayAfterTomorrow_tmin}}</span>
                    </div>
                    </div>
                </div>
            </div>
        </div>
    
         <!-- 여기서부터 통보문 -->
            <div class="row">
              <div class="col-lg-12">
                  <nav class="blog-pagination justify-content-center d-flex">
                      <ul>
                        <!-- Button trigger modal -->
                            <button type="button" class="btn btn-info" data-toggle="modal" data-target="#exampleModal2">
                                날씨해설
                            </button>
                        <!-- Modal -->
                            <div class="modal fade" id="exampleModal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                <div class="modal-header">
                                    <h5 class="modal-title" id="exampleModalLabel">{{date[0].year}}년 {{date[0].month}}월 {{date[0].day}}일 {{date[0].time}}시 발효</h5>
                                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                    <span aria-hidden="true">&times;</span>
                                    </button>
                                </div>
                                <div class="modal-body">
                                    <div v-html="notice"></div>
                                </div>
                                <div class="modal-footer">
                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                </div>
                                </div>
                            </div>
                            </div>
                      </ul>
                  </nav>
              </div>
            </div>
            <!-- 여기까지 -->


        
    </div>  

</template>




<script>
import axios from 'axios';

export default {
  data() {
    return {
        weatherlist: [],
        notice : [],
        date : [],
        geoweatherlist: []
        }  
    },
    mounted(){
        const temp = this
        navigator.geolocation.getCurrentPosition(function(position){
            const lat = position.coords.latitude //위도
            const lon = position.coords.longitude // 경도
            axios.get('http://127.0.0.1:8000/api/weatherliveinfo/', {
                params: {
                    Lat: lat,
                    Lon: lon,
            }})
            .then(res=>{
                temp.geoweatherlist = res.data
            })});
            this.interval = setInterval(()=>{
                axios.get('http://127.0.0.1:8000/api/weatherinfoList/')
                .then(res=>{
                    res.data
                    })
            }, 3000000);
            axios.get('http://127.0.0.1:8000/api/weatherinfo/')
            .then( response => {
                    temp.weatherlist = response.data
            });
            this.interval = setInterval(()=>{
                axios.get('http://127.0.0.1:8000/api/WeathernoticeList/')
                .then(res=>{
                    res.data
                    })
            }, 3000000);
            axios.get('http://127.0.0.1:8000/api/WeatherNotice/')
            .then(res=>{
                temp.notice = res.data
                temp.date = res.data
                temp.notice = temp.notice[0].content.replace(/(?:\r\n|\r|\n)/g, '<br />') 
            });

        }
}
</script>



<style scoped>
.col-12{
    height: 50px;
    background-color : rgb(248, 238, 225);
}

.col-6.col-md-3{
  background-color: rgb(250, 248, 242);
} 

.col-12write{
    position: absolute;
    top: 50%;
    transform: translate(0%, -50%)
}

.today_weather{
    text-align: center;
    position: relative;
    top: 15%;
}
.week_weather{
    text-align: center;
    position: relative;
    top: 5%;

}
.week_weather_content{
    text-align: center;
    position: relative;
    top: 20%;

}
</style>
