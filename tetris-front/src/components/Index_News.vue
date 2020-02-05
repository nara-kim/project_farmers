<template>
  <div class="container">
     <br><p class="text-center">More bootstrap 4 components on <a href="http://bootstrap-ecommerce.com/"> Bootstrap-ecommerce.com</a></p>
    <hr>
   <div class="row">
<aside class="col-md-6">
  <h3 style="font-weight:bold">실시간뉴스</h3>
<!-- ================== 1-carousel bootstrap  ==================  -->
  <div id="carousel1_indicator" class="carousel slide" data-ride="carousel">
    <ol class="carousel-indicators">
      <li data-target="#carousel1_indicator" data-slide-to="0" class="active"></li>
      <li data-target="#carousel1_indicator" data-slide-to="1"></li>
      <li data-target="#carousel1_indicator" data-slide-to="2"></li>
      <li data-target="#carousel1_indicator" data-slide-to="3"></li>
      <li data-target="#carousel1_indicator" data-slide-to="4"></li>
    </ol>  

  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide2.jpg" alt="Second slide">
    </div>

    <div class="carousel-item" v-for="news of newslist" v-bind:key="news.id">
      <img class="d-block w-100" v-bind:src="news.newsimg" alt="First slide"> 
      <article class="carousel-caption" style="block">
        <p class="carousel-text">{{news.title}}</p>
      </article> <!-- carousel-caption .// -->
    </div>

  </div>
  <a class="carousel-control-prev" href="#carousel1_indicator" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carousel1_indicator" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div> 
<!-- ==================  1-carousel bootstrap ==================  .// -->      
   </aside> <!-- col.// -->
   <aside class="col-md-6">
     <h3 style="font-weight:bold; margin-bottom:10px;">농민신문</h3>
     <div class="news_title_box" v-for="news of newslist" v-bind:key="news.id">
       <a class="news_title_txt" v-bind:href="news.newslink">{{news.title}}</a>
     </div>
<!-- 2-carousel bootstrap -->
<!-- <div id="carousel2_indicator" class="carousel slide carousel-fade" data-ride="carousel">
  <div class="carousel-inner">

    <div class="carousel-item active">
      <img class="d-block w-100 news-carousel-image" src="https://search.pstatic.net/common/?src=https%3A%2F%2Fimgnews.pstatic.net%2Fimage%2Forigin%2F468%2F2020%2F02%2F03%2F622228.jpg" alt="여기도 뭔가 작성과 사진을 넣을 수 있네요">
      <article class="carousel-caption d-none d-md-block"><img src="" alt="" >
        <h5>Title 자리 </h5>
        <p class="carousel-text">내용을 여기에다가 적으면 어떻게 되는지 한번 테스트 하려고 무작정 적는 말들 입니다. ~~ 신경쓰지 마시라우</p>
        </article>
    </div>
  
    <div class="carousel-item" v-for="news of newslist" v-bind:key="news.id">
      <img class="d-block w-100" v-bind:src="news.newsimg" alt="Second slide">

        <article class="carousel-caption" style="block">
        <p class="carousel-text">{{news.title}}</p>
        </article>
    </div>


  </div>
  <a class="carousel-control-prev" href="#carousel2_indicator" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carousel2_indicator" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>  -->
<!-- ==================  2-carousel bootstrap.// ==================  -->   
   </aside>
   </div>
</div>
<!--container end.//-->
</template>
 
<script>
import axios from 'axios';

export default {
  data() {
    return {
      newslist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/newsinfo/')
        .then( response => {
                    this.newslist = response.data
      });
    }


    
  },
}
</script>

<style scoped>
.carousel-item{min-height:300px; background:#ccc; }

.d-block{
  height: 300px; 
  width:100%;
}
.carousel-text{
  color: white;
  font-size: 19px;
  font-weight: 700;
}
.news_title_box{
  line-height: 55px;
  font-weight: bold;

}
.news_title_txt{
  color: black;
  font-size:19px;
  white-space: nowrap;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  display: inline-block;

}

</style>