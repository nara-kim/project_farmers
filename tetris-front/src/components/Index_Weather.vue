<template>
    <div class ="container">
        <div class ="row" style="border:1px solid #EAEEF3;">
            <div class="col-12" style="border-bottom:1px solid #EAEEF3;">
                <div class ="col-12write" style="padding-left: 15px;">
                    광주광역시 엔젤리너스 (2020-02-17 21:00:00)
                </div>
            </div>

            <div class="col-sm" id = "picture" >
                <div class="today_weather">
                    <img src = "img/sun.png" class="picture" width="100px;">
                </div>
            </div>

            <div class="col-sm" style="height: 150px;">
                <div class="today_weather">
                    <div>
                        <span style="font-size:35px;">
                            1
                        </span>
                        <span style="font-size: 27px; font-weight:bold">
                            ℃
                        </span>
                    </div>
                    <div>
                        흐리고 눈
                    </div>
                    <div>
                    1도/-18도

                    </div>
                </div>
            </div>

            <div class="col-sm" style="height: 150px; border-left:1px solid #EAEEF3;">
                <div class ="today_weather">
                    <div>
                        <span>
                            <img src = "img/sun.png" width="40px;">
                        </span>
                    </div>
                    <div>
                        빨래가 잘 마르지 않아요
                    </div>
                    <div>
                        <img src = "img/sun.png" width="40px;">
                    </div>
                    <div>
                        자외선 노출 대비하세요
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
                    <div>눈</div>
                    <div>
                        <span>최고기온:</span>
                        <span> 6.4</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> -0.8</span>
                    </div>
                </div>
            </div>

            <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                <div class="week_weather">
                    오늘날씨
                </div>
                <div class="week_weather_content">
                    <div>
                        <span>

                        <img src = "img/sun.png" width="30px;">
                        </span>

                    </div>
                    <div>
                        <span>최고기온:</span>
                        <span> 1.0</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> -2.0</span>
                    </div>
                </div>
            </div>

            <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                <div class="week_weather">
                    내일날씨
                </div>
                <div class="week_weather_content">
                    <div>눈</div>

                    <div>
                        <span>최고기온:</span>
                        <span> 1.0</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> -1.0</span>
                    </div>
                </div>
            </div>

            <div class="col-6 col-md-3" style="height: 150px; border-left:1px solid #EAEEF3">
                <div class="week_weather">
                    모레
                </div>
                <div class="week_weather_content">
                    <div>구름많음</div>

                    <div>
                        <span>최고기온:</span>
                        <span> 6.0</span>
                    </div>
                    <div>
                        <span>최저기온:</span>
                        <span> -1.0</span>
                    </div>
                </div>
            </div>

        </div>
    </div>
</template>

<style scoped>
.col-12{
    height: 50px;
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