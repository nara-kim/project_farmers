<template>
  <div class="col-lg-8" >
    <div class="thumb" v-for="weather of weatherlist" v-bind:key="weather.id">      
      <div class="bigwetherinfo">
        <span class = "weatherinfo">{{weather.loaction}}</span>
      </div>
      <hr>
      <div class = "left">
        <div v-if="weather.sky === '맑음'">
          <img src="img/sun.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '구름조금'">
          <img src="img/cloud.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '구름많음'">
          <img src="img/cloud.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '구름많고 비'">
          <img src="img/rain.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '구름많고 눈'">
          <img src="img/snow.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '구름많고 비 또는 눈'">
          <img src="img/rain.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '흐림'">
          <img src="img/cloud.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '흐리고 비'">
          <img src="img/rain.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '흐리고 눈'">
          <img src="img/snow.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '흐리고 비 또는 눈'">
          <img src="img/rain.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '흐리고 낙뢰'">
          <img src="img/power.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '뇌우/비'">
          <img src="img/뇌우.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '뇌우/눈'">
          <img src="img/뇌우.png" class="imgweather">
        </div>
        <div v-else-if="weather.sky === '뇌우/비 또는 눈'">
          <img src="img/뇌우.png" class="imgweather">
        </div>
      </div>

      <div class = "right">
        <div class ="inindex">
          <div class ="temp">
            <div class = "tempdiv">
            <span class = "tc">
              {{weather.tc}}
            </span>
            <span class="c">
              °C
            </span>
            <div class ="sky">{{weather.sky}}</div>
            <div class="maxmin">
              <span class = "tmx">{{weather.tmx}}</span>
              <span class="slash">/</span>
              <span class = "tmin">{{weather.tmin}}</span>
            </div>
          </div>
          </div>

          <div class="temp2">풍속자리</div>
        </div>

      </div>
    

    <div class = "bottom">
      <div class = "iam">진짜이거 왜이래?</div>
      <div class = "gh">주간날씨자리</div>
    </div>

    <div class="parent" style="width: 100%; height: 300px; background: #585858;">
      <div class="child" style="background: #2E9AFE;">
      </div>
      <div class="child" style="background: #FA5858;">
      </div>
      <div class="child" style="background: #81F781;">
      </div>
      <div class="child" style="background: green;">
      </div>
      <div class="child" style="background: orange;">
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
      weatherlist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/weatherinfo/')
        .then( response => {
                    this.weatherlist = response.data
      });
    }
  },
}
</script>

<style scoped>
/* 선 css */
.li{
  height: 50px;
  width : 0px;
  border-right: 0px;
}
.tempdiv{
  margin-top: 15px;
  padding-left: 10%;
}

/* 글씨위주 css */
.tmx{
  color: blue;
}
.tmin{
  color: red;
}
.tc{
  display:inline-block; 
  font-size:40px; 
  font-weight:400;
}
.c{
  display:inline-block;
  font-size:30px;
}
.sky{
  text-align: left;
  font-size: 15px;
}
.maxmin{
  width:100%;
  font-weight: 600;
  text-align: left;
}

/* img css */
.imgweather{
  width:100%;
  height: 183px;
  float:left;
  padding-right: 10%;
}



/* div css */
.big{
  width: 100%;
}
.left{
  float:left;
  width:30%;
}
.right{
  float:right;
  width: 70%;
}
.weatherinfo{
  font-size: 20px;
  font-weight: 700;
  /* background:skyblue; */
}
.inindex{
  float:left;
  width: 100%;
  padding-top: 4%;
}
.temp{
  height: 130px;
  width:45%;
  float:left;
  padding-left: 2%;
  border-right: 1px solid #e4e4e4;
}
.temp2{
  float: right;
  height: 130px;
  width: 35%;
}
.iam{
  height: 250px;
  color: white;
  background-color: white;
}
.gh{
  background-color: pink;
}
.parent {
    display: flex;
}
.child {
    flex: 1;
}
</style>