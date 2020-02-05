<template>
  <div class="col-lg-4 sidebar-widgets" style="font-family: 'Jua', sans-serif;">
    <div v-for="dust of dustlist" v-bind:key="dust.id">
              <div class="widget-wrap">

                <div class="single-sidebar-widget post-category-widget">
                  <h4 class="single-sidebar-widget__title" style="letter-spacing:3px">미세먼지</h4>
                  <div class="location_time">
                    <h5>현재위치</h5>
                    <span>
                      <h5> ( {{dust.stationname}} ) </h5>
                    </span>
                    <span>
                      {{dust.dataTime}}
                    </span>
                  </div>
                  <br>
                  <div class="finedust_div" style="height:120px;">

                    <div class="finedust_left">
                      <span style="font-size:20px;">미세먼지</span>
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
                      <span style="font-size:20px">초미세먼지</span>
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

                <div class="single-sidebar-widget popular-post-widget">
                  <h4 class="single-sidebar-widget__title">Popular Post</h4>
                  <div class="popular-post-list">
                    <div class="single-post-list">
                      <div class="thumb">
                        <img class="card-img rounded-0" src="img/blog/thumb/thumb1.png" alt="">
                        <ul class="thumb-info">
                          <li><a href="#">Adam Colinge</a></li>
                          <li><a href="#">Dec 15</a></li>
                        </ul>
                      </div>
                      <div class="details mt-20">
                        <a href="blog-single.html">
                          <h6>Accused of assaulting flight attendant miktake alaways</h6>
                        </a>
                      </div>
                    </div>
                    <div class="single-post-list">
                      <div class="thumb">
                        <img class="card-img rounded-0" src="img/blog/thumb/thumb2.png" alt="">
                        <ul class="thumb-info">
                          <li><a href="#">Adam Colinge</a></li>
                          <li><a href="#">Dec 15</a></li>
                        </ul>
                      </div>
                      <div class="details mt-20">
                        <a href="blog-single.html">
                          <h6>Tennessee outback steakhouse the
                            worker diagnosed</h6>
                        </a>
                      </div>
                    </div>
                    <div class="single-post-list">
                      <div class="thumb">
                        <img class="card-img rounded-0" src="img/blog/thumb/thumb3.png" alt="">
                        <ul class="thumb-info">
                          <li><a href="#">Adam Colinge</a></li>
                          <li><a href="#">Dec 15</a></li>
                        </ul>
                      </div>
                      <div class="details mt-20">
                        <a href="blog-single.html">
                          <h6>Tennessee outback steakhouse the
                            worker diagnosed</h6>
                        </a>
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
.finedust_img{
  width: 40%;
  margin-top: 10px;
}
.single-sidebar-widget__title{
  font-size: 180%;
}
.location_time{
  text-align: center;
}
.single-sidebar-widget{
  background-color: white;
  border: 1px solid #e4e4e4;
}
template {
  font-family: "Jua", sans-serif;
}
</style>
