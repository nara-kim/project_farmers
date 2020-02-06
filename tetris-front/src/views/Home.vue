<template>
  <div class="home">
    <Index_News/>
     <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
          <Index_Weather/>
          <Index_Radar/>
          <Index_Finedust/>
        </div>
      </div>
     </section>
     <Index_Price/>
  </div>
</template>

<script>
// @ is an alias to /src
import Index_News from '@/components/Index_News.vue'
import Index_Finedust from '@/components/Index_Finedust.vue'
import Index_Weather from '@/components/Index_Weather.vue'
import Index_Price from '@/components/Index_Price.vue'
import Index_Radar from '@/components/Index_Radar.vue'

export default {
  name: 'home',
  components: {
    Index_News,
    Index_Weather,
    Index_Finedust,
    Index_Price,
    Index_Radar
  },
  updated() {
    this.$nextTick(function(){

    })
  }
}
</script>
