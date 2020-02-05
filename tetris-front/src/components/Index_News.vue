<template>
  <div class="container">
     <br><p class="text-center">More bootstrap 4 components on <a href="http://bootstrap-ecommerce.com/"> Bootstrap-ecommerce.com</a></p>
    <hr>
   <div class="row">
<aside class="col-md-6">
  <p>Slider with pagination</p>
<!-- ================== 1-carousel bootstrap  ==================  -->
<div id="carousel1_indicator" class="carousel slide" data-ride="carousel">
  <ol class="carousel-indicators">
    <li data-target="#carousel1_indicator" data-slide-to="0" class="active"></li>
    <li data-target="#carousel1_indicator" data-slide-to="1"></li>
    <li data-target="#carousel1_indicator" data-slide-to="2"></li>
  </ol>  
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide1.jpg" alt="First slide"> 
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide2.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide3.jpg" alt="Third slide">
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
    <p>Slider with caption</p>
<!-- 2-carousel bootstrap -->
<div id="carousel2_indicator" class="carousel slide carousel-fade" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="/img/loginlogo.png" alt="여기도 뭔가 작성과 사진을 넣을 수 있네요">
      <article class="carousel-caption d-none d-md-block"><img src="" alt="" >
        <h5>Title 자리 </h5>
        <p>내용을 여기에다가 적으면 어떻게 되는지 한번 테스트 하려고 무작정 적는 말들 입니다. ~~ 신경쓰지 마시라우</p>
        </article> <!-- carousel-caption .// -->
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide2.jpg" alt="Second slide">
      <article class="carousel-caption d-none d-md-block">
        <h5>Second slide label</h5>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt.</p>
        </article> <!-- carousel-caption .// -->
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="http://bootstrap-ecommerce.com/main/images/banners/slide3.jpg" alt="Third slide">
      <article class="carousel-caption d-none d-md-block">
        <h5>Third slide label</h5>
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmodtempor incididunt</p>
        </article> <!-- carousel-caption .// -->
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
</div> 
<!-- ==================  2-carousel bootstrap.// ==================  -->   
   </aside>
   </div>
</div>
<!--container end.//-->
</template>

<script>
export default {
  name: 'News',
  props: {
    msg: String
  }
}
</script>

<style scoped>
.carousel-item{min-height:300px; background:#ccc; }

.d-block.w-100{
  height: 200px; 
  width:10px;
}

</style>