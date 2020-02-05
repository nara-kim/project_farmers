<template>
  <div class="home">
    <h1>에이스</h1>
    <Index_News/>
     <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
          <Index_Weather/>
          <Index_Finedust/>
        </div>
      </div>
     </section>
  </div>
</template>

<script>
// @ is an alias to /src
import Index_News from '@/components/Index_News.vue'
import Index_Finedust from '@/components/Index_Finedust.vue'
import Index_Weather from '@/components/Index_Weather.vue'

export default {
  name: 'home',
  components: {
    Index_News,
    Index_Weather,
    Index_Finedust,
  },
  updated() {
    this.$nextTick(function(){

    })
  }
}
</script>
