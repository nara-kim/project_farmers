<template>
<div id="scroll5">
    <div v-if="geodustlist.length === 0">
      <div class ="finedust" style=" font-family: 'Jua', sans-serif; font-size:2.0em;">
          미세먼지 <hr style="background-color: orange;height: 1.3px;">
      <div id="scroll6">

        <div class="widget-wrap">
            <div>
              <div>
                  <div>
                    <div class="weather">
                        <div class="current" style="background-color:#cfcfcf; ">
                          <div class="location_time" >
                            <h5>평균 대기오염
                            </h5>
                            <span style="display:inline-block; width:220px;text-align:right; font-size:15px;">
                              {{dustlist[0].dataTime}}
                            </span>   
                            <span class = "station">
                              <br>
                            </span>
                          </div>
                          <div class="future">
                            <div class="finedust_left">
                              <div>미세먼지</div>
                              <div v-if="dustlist[0].pm10Value<=30">
                                <img class="finedust_img" src="img/finedust1.png">
                              </div>
                              <div v-else-if="30<dustlist[0].pm10Value<=80">
                                <img class="finedust_img" src="img/finedust2.png">
                              </div>
                              <div v-else-if="80<dustlist[0].pm10Value<=150">
                                <img class="finedust_img" src="img/finedust3.png">
                              </div>
                              <div v-else-if="150<dustlist[0].pm10Value">
                                <img class="finedust_img" src="img/finedust4.png">
                              </div>
                              <h2>{{dustlist[0].pm10Value}}</h2>
                            </div>
                            <div class="finedust_right">
                              <div>초미세먼지</div>
                              <div v-if="dustlist[0].pm25Value<=15">
                                <img class="finedust_img" src="img/finedust1.png">
                              </div>
                              <div v-else-if="15<dustlist[0].pm25Value<=35">
                                <img class="finedust_img" src="img/finedust2.png">
                              </div>
                              <div v-else-if="35<dustlist[0].pm25Value<=75">
                                <img class="finedust_img" src="img/finedust3.png">
                              </div>
                              <div v-else-if="75<dustlist[0].pm25Value">
                                <img class="finedust_img" src="img/finedust4.png">
                              </div>
                              <h2>{{dustlist[0].pm25Value}}</h2>
                            </div>
                          </div>
                        </div>
                    </div>
                </div>
              </div>
            </div>   
         </div>
        </div>
    </div>
    </div>

    <div v-else>
      <div class ="finedust" style=" font-family: 'Jua', sans-serif;">
      미세먼지 <hr>
        <div class="widget-wrap">
            <div>
              <div>
                  <div>
                    <div class="weather">
                        <div class="current" style="background-color:#cfcfcf; ">
                          <div class="location_time" >
                            <h5>가장가까운 관측소명 {{geodustlist.stationname}}관측소
                            </h5>
                            <span style="display:inline-block; width:220px;text-align:right; font-size:15px;">
                              {{geodustlist.dataTime}}
                            </span>   
                            <span class = "station">
                              <br>
                            </span>
                          </div>
                          <div class="future">
                            <div class="finedust_left">
                              <div>미세먼지</div>
                              <div v-if="geodustlist.pm10Value<=30">
                                <img class="finedust_img" src="img/finedust1.png">
                              </div>
                              <div v-else-if="30<geodustlist.pm10Value<=80">
                                <img class="finedust_img" src="img/finedust2.png">
                              </div>
                              <div v-else-if="80<geodustlist.pm10Value<=150">
                                <img class="finedust_img" src="img/finedust3.png">
                              </div>
                              <div v-else-if="150<geodustlist.pm10Value">
                                <img class="finedust_img" src="img/finedust4.png">
                              </div>
                              <h2>{{geodustlist.pm10Value}}</h2>
                            </div>
                            <div class="finedust_right">
                              <div>초미세먼지</div>
                              <div v-if="geodustlist.pm25Value<=15">
                                <img class="finedust_img" src="img/finedust1.png">
                              </div>
                              <div v-else-if="15<geodustlist.pm25Value<=35">
                                <img class="finedust_img" src="img/finedust2.png">
                              </div>
                              <div v-else-if="35<geodustlist.pm25Value<=75">
                                <img class="finedust_img" src="img/finedust3.png">
                              </div>
                              <div v-else-if="75<geodustlist.pm25Value">
                                <img class="finedust_img" src="img/finedust4.png">
                              </div>
                              <h2>{{geodustlist.pm25Value}}</h2>
                            </div>
                          </div>
                        </div>
                    </div>
                </div>
              </div>
            </div>   
         </div>
        </div>
      </div>
</div>

</template>

<script>
import axios from 'axios';
export default {
  data() {
    return {
      dustlist: [],
      geodustlist: [],
    }
  },
  mounted(){const temp = this
        navigator.geolocation.getCurrentPosition(function(position){
            const lat = position.coords.latitude //위도
                const lon = position.coords.longitude // 경도
            axios.get('http://15.165.77.204:8000/api/dustliveinfo/', {
                params: {
                    Lat: lat,
                    Lon: lon,
            }})
            .then(res=>{
                temp.geodustlist = res.data
            })});
            this.interval = setInterval(()=>{
                axios.get('http://15.165.77.204:8000/api/dustinfoList/')
                .then(res=>{
                    res.data
                    })
            }, 3000000);
            axios.get('http://15.165.77.204:8000/api/dustinfo/')
            .then( response => {
                    temp.dustlist = response.data
            });

        }
}
</script>


<style scoped>
.finedust{
  margin-top: 60px;
}
.single-sidebar-widget__title{
  font-size: 180%;
}
.single-sidebar-widget{
  background-position: center;
  border: 1px solid #e4e4e4;
}
.weather
    {
        display: flex;
        flex-flow: column wrap;
        box-shadow: 0px 1px 10px 0px #cfcfcf;
        overflow: hidden;
    }

.weather .current
{
    display: flex;
    flex-flow: row wrap;
    background-repeat: repeat-x;
    color: black;
    padding: 20px;
    /* text-shadow: 1px 1px rgb(253, 231, 215); */
}

.weather .current .info
{
    display: flex;
    flex-flow: column wrap;
    justify-content: space-around;
    flex-grow: 2;
}

.weather .current .info .city
{
    font-size: 26px;
}

.weather .current .info .temp
{
    font-size: 56px;
}

.weather .current .info .wind
{
    font-size: 24px;
}

.weather .current .icon
{
  text-align: center;
  font-size: 64px;
  flex-grow: 1;
}

.weather .future
{
    display: flex;
    flex-flow: row nowrap;
}

.weather .future .day
{
    flex-grow: 1;
    text-align: center;
    cursor: pointer;
}

.weather .future .day:hover
{
    color: #fff;
    background-color: #F68D2E;
}

.weather .future .day h3
{
    text-transform: uppercase;
}

.weather .future .day p
{
    font-size: 28px;
}

.finedust_img{
  width: 40%;
  margin-top: 10px;
}

.finedust_left{
  width: 50%;
  float: left;
  text-align: center;
}

.finedust_right{
  width: 50%;
  float: right;
  text-align: center;
}

.current{
  background-color: rgba(0,0,0,0.5);
}
</style>

