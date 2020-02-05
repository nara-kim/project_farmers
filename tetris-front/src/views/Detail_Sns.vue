<template>
    <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
          <Detail_Sns_Left/>
          <Detail_Sns_Right/>
        </div>
      </div>
     </section>
</template>

<script>
// @ is an alias to /src
import Detail_Sns_Left from '@/components/Detail_Sns_Left.vue'
import Detail_Sns_Right from '@/components/Detail_Sns_Right.vue'

export default {
  name: 'detail_sns',
  components: {
    Detail_Sns_Left,
    Detail_Sns_Right
  }
}
</script>