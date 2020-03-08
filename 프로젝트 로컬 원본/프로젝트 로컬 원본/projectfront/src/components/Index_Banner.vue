<template>
<div class="container" style=" font-family: 'Jua', sans-serif; font-size:1.3125em;">
      <!-- ================== 1-carousel bootstrap  ==================  -->
    <div class="row">
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
              <img class="d-block w-100" src="img/dustfarmer.PNG" style="height:350px;"> 
            </div>
            <div class="carousel-item">
              <img class="d-block w-100" src="img/winter.png" style="height:350px;"> 
            </div>
              <div class="carousel-item">
              <img class="d-block w-100" src="img/corona.png"  style="height:350px;">
            </div>
             <div class="carousel-item">
              <img class="d-block w-100" src="img/animal.png" style="height:350px;"> 
            </div>
             <div class="carousel-item">
              <img class="d-block w-100" src="img/2020.png" style="height: 350px;"> 
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
        <div class="news_title_box" style="border:1px solid rgb(182, 180, 180);">
          <div class="news_title_txt1" onclick="fnMove('1')">
            <img src="img/news1.png" style="width:40%; margin-left: 35px; margin-top: 20px; ">
              <div style="text-align:center; color: gray; margin-top:5px;">
                뉴스
              </div>
          </div>
          <div class="news_title_txt2" onclick="fnMove('3')"> 
            <img src="img/cloudy1.png" style="width:40%; margin-left:35px; margin-top:15px;">
            <div style="text-align:center; color: gray; margin-top:6px;">
                날씨
              </div>
            </div>
          <div class="news_title_txt3" onclick="fnMove('2')">
            <img src="img/bacteria.png" style="width:38%; margin-left:35px; margin-top:20px; ">
            <div style="text-align:center; color: gray; margin-top:6px;">
                가축질병
              </div>
          </div>
        </div>

        <div class="news_title_box" style="border-left:1px solid rgb(182, 180, 180); border-right:1px solid rgb(182, 180, 180); border-bottom:1px solid rgb(182, 180, 180); height:115.5px;">
          <div class = "news_title_txt1" onclick="fnMove('4')">
            <img src="img/bug.png" style="width:40%; margin-left:38px; margin-top:20px; ">
              <div style="text-align:center; color: gray; margin-top:6px;">
                병해충
              </div>
          </div>
          <div class="news_title_txt2" onclick="fnMove('5')"> 
              <img src="img/dust.png" style="width:40%; margin-left:38px; margin-top:20px; ">
                <div style="text-align:center; color: gray; margin-top:6px;">
                  미세먼지
                </div>
          </div>
          <div class="news_title_txt3" onclick="fnMove('6')">
              <img src="img/radar.png" style="width:40%; margin-left:38px; margin-top:20px;">
                <div style="text-align:center; color: gray; margin-top:6px;">
                강수실황
                </div>
          </div>
          
        </div>

        <div class="news_title_box" style="border-left:1px solid rgb(182, 180, 180); border-right:1px solid rgb(182, 180, 180); border-bottom:1px solid rgb(182, 180, 180); height:115px">
          <div class="news_title_txt1" onclick="fnMove('7')">
             <img src="img/information.png" style="width:40%; margin-left:38px; margin-top:20px;">
                <div style="text-align:center; color: gray; margin-top:6px;">
                이달의기술
                </div>
          </div>
          <div class="news_title_txt2">
              <router-link to="/board" style="text-decoration:none; color : gray; font-size:1.0em;font-family: 'Jua', sans-serif; ">

             <img src="img/help.png" style="width:40%; margin-left:38px; margin-top:20px;">
                <div style="text-align:center; color: gray; margin-top:6px;">
                일손
                </div>
               </router-link>

          </div>
          <div class="news_title_txt3">
            <div id = "scroll1">
              <router-link to="/sns" style="text-decoration:none; color : gray; font-size:1.0em;font-family: 'Jua', sans-serif; ">

             <img src="img/SNS.png" style="width:40%; margin-left:38px; margin-top:20px; ">
                <div style="text-align:center; color: gray; margin-top:6px;">
                오늘의땀
                </div>
               </router-link>

            </div>
          </div>
        
        </div>

      </aside>
         <!-- </div> -->

      </div>
</div>
</template>

<style scoped> 
.news_title_txt1:hover{
  /* background-color: black; */
  opacity: 0.5;
}
.news_title_txt2:hover{
  /* background-color: black; */
  opacity: 0.5;
}
.news_title_txt3:hover{
  /* background-color: black; */
  opacity: 0.5;
}
.carousel-item{min-height:350px; background:#ccc; }
.container{
    margin-top: 3%;
}
.news_title_box{
    /* border: 1px solid black;  */
    height: 33.3%;
}
.news_title_txt1{
  float:left;
  height:114.55px; 
  width:33%; 
  background-color: rgb(248, 238, 225); 
  border-right :1px solid rgb(182, 180, 180);
}
.news_title_txt2{
  float: right;
  height:114.55px; 
  width:33%;
  background-color: rgb(248, 238, 225); 
  /* border-right :1px solid black; */

}
.news_title_txt3{
  float: right;
  height:114.55px; 
  width:34%;
  background-color: rgb(248, 238, 225); 
  border-right :1px solid rgb(182, 180, 180);

}
</style>

<script type="text/javascript" src="http://code.jquery.com/jquery-latest.js"></script>
<script>
function fnMove(seq){
        var offset = $("#div" + seq).offset();
        $('html, body').animate({scrollTop : offset.top}, 400);
    }
</script>
