<template>
  <div class="col-lg-4 sidebar-widgets">
    <div v-for="dust of dustlist" v-bind:key="dust.id">
      <div class="widget-wrap">
        <div class="single-sidebar-widget post-category-widget">
          <h4 class="single-sidebar-widget__title" style="letter-spacing:3px">미세먼지</h4>

          <div>
            <div>
                <div>
                  <div class="weather">
                      <div class="current">
                        <div class="location_time">
                          <h5>현재위치</h5>
                          <span>
                            <h5>{{dust.stationname}}</h5>
                          </span>
                          <span>
                            {{dust.dataTime}}
                          </span>
                        </div>
                        <div class="future">
                          <div class="finedust_left">
                            <div>미세먼지</div>
                            <div v-if="dust.pm10Value<=30">
                              <img class="finedust_img" src="img/finedust1.png">
                            </div>
                            <div v-else-if="30<dust.pm10Value<=80">
                              <img class="finedust_img" src="img/finedust2.png">
                            </div>
                            <div v-else-if="80<dust.pm10Value<=150">
                              <img class="finedust_img" src="img/finedust3.png">
                            </div>
                            <div v-else-if="150<dust.pm10Value">
                              <img class="finedust_img" src="img/finedust4.png">
                            </div>
                            <h2>{{dust.pm10Value}}</h2>
                          </div>
                          <div class="finedust_right">
                            <div>초미세먼지</div>
                            <div v-if="dust.pm25Value<=15">
                              <img class="finedust_img" src="img/finedust1.png">
                            </div>
                            <div v-else-if="15<dust.pm25Value<=35">
                              <img class="finedust_img" src="img/finedust2.png">
                            </div>
                            <div v-else-if="35<dust.pm25Value<=75">
                              <img class="finedust_img" src="img/finedust3.png">
                            </div>
                            <div v-else-if="75<dust.pm25Value">
                              <img class="finedust_img" src="img/finedust4.png">
                            </div>
                            <h2>{{dust.pm25Value}}</h2>
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
      dustlist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/dustinfo/')
        .then( response => {
                    this.dustlist = response.data
      });
    }
  },
}
</script>


<style scoped>
.single-sidebar-widget__title{
  font-size: 180%;
}
.single-sidebar-widget{
  /* background-color: #def0fa; */
  background-image: url("/img/vvvvvvv.jpg");
  background-repeat: no-repeat;
  background-size: cover;
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
    /* background-image: url("/img/london.jpg"); */
    background-repeat: repeat-x;
    color: white;
    padding: 20px;
    text-shadow: 1px 1px #F68D2E;
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
