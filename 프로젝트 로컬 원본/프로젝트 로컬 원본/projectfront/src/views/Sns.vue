<template>
  <div class="SNS">
    <section class="blog-post-area">
      <div>
        <img src="img/snsmain.png" style="width:100%;">
    </div>
      <div class ="container">
        <div class = "row">
          <div class="col-lg-8" style="margin-top:60px; font-family: 'Jua', sans-serif;">
            <Com_Sns_Right/>
            <Com_Sns_Left/>

        </div>
        <div class="col-lg-4 sidebar-widgets" style="margin-top:108px;">
            <Com_Sns_Rank/>
        </div>
      </div>
      </div>
    </section>
  </div>
</template>

<script>
import Com_Sns_Left from '@/components/Com_Sns_Left.vue'
import Com_Sns_Right from '@/components/Com_Sns_Right.vue'
import Com_Sns_Rank from '@/components/Com_Sns_Rank.vue'

export default {
  name: 'SNS',
  components: {
    Com_Sns_Left,
    Com_Sns_Right,
    Com_Sns_Rank,
  }
}
</script>