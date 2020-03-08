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
          <Index_Info/>

        </div>
      </div>
     </section>
  </div>
</template>

<script>
import Index_News from '@/components/Index_News.vue'
import Index_Finedust from '@/components/Index_Finedust.vue'
import Index_Weather from '@/components/Index_Weather.vue'
import Index_Info from '@/components/Index_Info.vue'
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
    Index_Info,
    Index_Radar,
    Index_Banner,
    Index_Disease,
    Index_Plant,
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
</style>