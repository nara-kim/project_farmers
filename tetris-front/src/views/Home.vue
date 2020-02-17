<template>
  <div class="home">
    <!-- <Index_Banner/> -->
    <Index_Banner/>
    <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
             <div class="col-lg-8" style="margin-top:60px; font-family: 'Jua', sans-serif; ">
              <Index_News/>                    
              <Index_Weather/>
            </div>
          <div class="col-lg-4 sidebar-widgets">
            <Index_Finedust/>
            <Index_Radar/>
            <Index_Disease/>
            <Index_Plant/>
          </div>
        </div>
      </div>
    </section>
     <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
          <Index_Price/>

        </div>
      </div>
     </section>
        <button @click="fnMove('1')">div1로 이동</button>
        <button @click="fnMove('2')">div2로 이동</button>
        <button @click="fnMove('3')">div3로 이동</button>
        <div id="div1" class="move">div1</div>
        <div id="div2" class="move">div2</div>
        <div id="div3" class="move">div3</div>
  </div>
</template>
<script src="https://code.jquery.com/jquery-3.2.1.js" 
integrity="sha256-DZAnKJ/6XZ9si04Hgrsxu/8s717jcIzLy3oi35EouyE=" 
crossorigin="anonymous"></script>

<script>
    // function fnMove(seq){
    //     var offset = $("#div" + seq).offset();
    //     $('html, body').animate({scrollTop : offset.top}, 400);
    // }
</script>
<script>
// @ is an alias to /src
import Index_News from '@/components/Index_News.vue'
import Index_Finedust from '@/components/Index_Finedust.vue'
import Index_Weather from '@/components/Index_Weather.vue'
import Index_Price from '@/components/Index_Price.vue'
import Index_Radar from '@/components/Index_Radar.vue'
import Index_Banner from '@/components/Index_Banner.vue'
import Index_Disease from '@/components/Index_Disease.vue'
import Index_Plant from '@/components/Index_Plant.vue'

export default {
  name: 'home',
  components: {
    Index_News,
    Index_Weather,
    Index_Finedust,
    Index_Price,
    Index_Radar,
    Index_Banner,
    Index_Disease,
    Index_Plant,
  },
  methods: {
    fnMove(seq){
        var offset = $("#div" + seq).offset();
        $('html, body').animate({scrollTop : offset.top}, 400);
    }
  },
  updated() {
    this.$nextTick(function(){

    })
  }
}
</script>

<style scoped>
.right1{
  background-color: pink;
}
.move {margin-bottom:1000px;}
</style>