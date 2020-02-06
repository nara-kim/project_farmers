<template>
  <div class="container">
     <br><p class="text-center">More bootstrap 4 components on <a href="http://bootstrap-ecommerce.com/"> Bootstrap-ecommerce.com</a></p>
      <hr>
    <div class="row" style="">
      <aside class="col-md-8" style="padding:0;">
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
              <article class="carousel-caption" style="padding:0 30px; background-color: rgba(0,0,0,0.5); width:100%; height:100px; padding-top: 26px;">
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
      <aside class="col-md-4" style="padding:0">
        <div class="news_title_box" style="border: 1px solid #ddd;" v-for="news of newslist" v-bind:key="news.id">
          <a class="news_title_txt" v-bind:href="news.newslink">{{news.title}}</a>
        </div>
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
  height: 330px; 
}
.carousel-caption{
  bottom: 0;
  left: 0;
}
.carousel-text{
  color: white;
  font-size: 17px;
  font-weight: 700;
}
.news_title_box{
  line-height: 52px;
  font-weight: bold;

}
.news_title_box:hover {
  background-color: #eee;
}
.news_title_txt{
  color: black;
  font-size:17px;
  white-space: nowrap;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  display: inline-block;
  padding: 16px 0 0 15px;

}

</style>