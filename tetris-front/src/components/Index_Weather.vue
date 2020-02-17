<template>
<!--================ Start Blog Post Area =================-->


    <!-- <div class="col-lg-8" style=" font-family: 'Jua', sans-serif;"> -->

            <!-- 여기부터 -->
    <div class="page-content page-container" id="page-content" style=" font-family: 'Nanum Gothic', sans-serif; font-weight:bold;">
        날씨 <hr>
    <div>
        <div class="thumb" v-for="weather of weatherlist" v-bind:key="weather.id">      
                <div class="card card-weather">
                    
                    <div v-if="weather.sky === '맑음'">
                    <div class="card-body" style="background-image:url('img/sun.png'); background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '구름조금'">
                    <div class="card-body" style="background-image:url('img/cloud.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '구름많음'">
                    <div class="card-body" style="background-image:url('img/cloud.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '구름 많고 비'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '구름 많고 눈'">
                    <div class="card-body" style="background-image:url('img/snow.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '구름많고 비 또는 눈'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '흐림'">
                    <div class="card-body" style="background-image:url('img/cloud.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '흐리고 비'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '흐리고 눈'">
                    <div class="card-body" style="background-image:url('img/snow.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '흐리고 비 또는 눈'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '흐리고 낙뢰'">
                    <div class="card-body" style="background-image:url('img/cloud.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '뇌우/비'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '뇌우/눈'">
                    <div class="card-body" style="background-image:url('img/snow.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div v-if="weather.sky === '뇌우/비 또는 눈'">
                    <div class="card-body" style="background-image:url('img/rain.png') background-repeat: no-repeat; background-size: cover; background-position: center;">
                        <div class="weather-date-location">
                            <h3>{{weather.loaction }}</h3>
                            <p class="text-gray"> <span class="weather-date"></span> <span class="weather-location">{{weather.timerelease}}</span> </p>
                        </div>
                        <div class="weather-data d-flex">
                            <div class="mr-auto">
                                <h4 class="display-3">{{weather.tc}} <span class="symbol">°</span>C</h4>
                                <p> {{weather.sky}} </p>
                            </div>
                        </div>
                    </div>
                    </div>

                    <div class="card-body p-0">
                        <div class="d-flex weakly-weather">
                            <div class="weakly-weather-item">
                                <p class="mb-0"> Sun </p> <i class="mdi mdi-weather-cloudy"></i>
                                <p class="mb-0"> 30° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Mon </p> <i class="mdi mdi-weather-hail"></i>
                                <p class="mb-0"> 31° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Tue </p> <i class="mdi mdi-weather-partlycloudy"></i>
                                <p class="mb-0"> 28° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Wed </p> <i class="mdi mdi-weather-pouring"></i>
                                <p class="mb-0"> 30° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Thu </p> <i class="mdi mdi-weather-pouring"></i>
                                <p class="mb-0"> 29° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Fri </p> <i class="mdi mdi-weather-snowy-rainy"></i>
                                <p class="mb-0"> 31° </p>
                            </div>
                            <div class="weakly-weather-item">
                                <p class="mb-1"> Sat </p> <i class="mdi mdi-weather-snowy"></i>
                                <p class="mb-0"> 32° </p>
                            </div>
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
    <!-- </div> -->
    <!--================ End Blog Post Area =================-->
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
        // weatherlist: [],
        weatherlist: [],
        notice : [],
        date : [],
        lat:'',
        lon:'',
        }  
    },
    mounted(){
        // const temp = this
        navigator.geolocation.getCurrentPosition(function(position){
            const formdata = new FormData()
            this.lat = position.coords.latitude
            this.lon = position.coords.longitude
            console.log(this.lat)
            console.log(this.lon)
            formdata.append('lat', this.lat) //위도
            formdata.append('lon', this.lon) // 경도
            formdata.appent('test', 'testtest')
            axios.post('http://127.0.0.1:8000/api/weatherinfo/', formdata)
            .then(res=>{
                this.weatherlist = res.data
                console.log(this.weatherlist)
            })});
            this.interval = setInterval(()=>{
                axios.get('http://127.0.0.1:8000/api/WeathernoticeList/')
                .then(res=>{
                    res.data
                    })
            }, 21600000);
            axios.get('http://127.0.0.1:8000/api/WeatherNotice/')
            .then(res=>{
                this.notice = res.data
                this.date = res.data
                this.notice = this.notice[0].content.replace(/(?:\r\n|\r|\n)/g, '<br />') 
            });

        }
}
</script>



<style scoped>
/* 여기 */
.stretch-card>.cards {
     width: 100%;
     min-width: 100%
 }

 body {
     background-color: #f9f9fa
 }

 .flex {
     -webkit-box-flex: 1;
     -ms-flex: 1 1 auto;
     flex: 1 1 auto
 }

 @media (max-width:991.98px) {
     .padding {
         padding: 1.5rem
     }
 }

 @media (max-width:767.98px) {
     .padding {
         padding: 1rem
     }
 }

 .padding {
     padding: 5rem
 }

 .grid-margin,
 .purchace-popup>div {
     margin-bottom: 25px
 }

 .card {
     border: 0;
     border-radius: 2px
 }

 .card-weather {
     background: #e1ecff;
     background-image: linear-gradient(to left bottom, #d6eef6, #dff0fa, #e7f3fc, #eff6fe, #f6f9ff)
 }

 .card {
     position: relative;
     display: flex;
     flex-direction: column;
     min-width: 0;
     word-wrap: break-word;
     background-color: #fff;
     background-clip: border-box;
     border: 1px solid rgba(0, 0, 0, 0.125);
     border-radius: 0.25rem
 }

 /* .card-weather .card-body:first-child {
     background: url(https://res.cloudinary.com/dxfq3iotg/image/upload/v1557323760/weather.svg) no-repeat center;
     background-size: cover
 } */

 .card .card-body {
     padding: 1.88rem 1.81rem
 }

 .card-body {
     flex: 1 1 auto;
     padding: 1.25rem;
 }

 .card-weather .weather-date-location {
     padding: 0 0 38px
 }

 .h3,
 h3 {
     font-size: 1.56rem
 }

 .h1,
 .h2,
 .h3,
 .h4,
 .h5,
 .h6,
 h1,
 h2,
 h3,
 h4,
 h5,
 h6 {
     font-family: "Poppins", sans-serif;
     font-weight: 500
 }

 .text-gray,
 .card-subtitle,
 .new-accounts ul.chats li.chat-persons a p.joined-date {
     color: #969696
 }

 p {
     font-size: 13px
 }

 .text-gray,
 .card-subtitle,
 .new-accounts ul.chats li.chat-persons a p.joined-date {
     color: #969696
 }

 .card-weather .weather-data {
     padding: 0 0 4.75rem
 }

 .mr-auto,
 .mx-auto {
     margin-right: auto !important
 }

 .display-3 {
     font-size: 2.5rem
 }

 .card-weather .card-body {
     background: #ffffff
 }

 .card-weather .weakly-weather {
     background: #ffffff;
     overflow-x: auto
 }

 .card-weather .weakly-weather .weakly-weather-item {
     flex: 0 0 14.28%;
     border-right: 1px solid #f2f2f2;
     padding: 1rem;
     text-align: center
 }

 .mb-0,
 .my-0 {
     margin-bottom: 0 !important
 }

 .card-weather .weakly-weather .weakly-weather-item i {
     font-size: 1.2rem
 }

 
</style>