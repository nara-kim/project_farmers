<template>
  <div class="SNS">
    <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
            <Com_Sns_Right/>
            <Com_Sns_Left/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
// @ is an alias to /src
// import One from '@/components/One.vue'
import Com_Sns_Left from '@/components/Com_Sns_Left.vue'
import Com_Sns_Right from '@/components/Com_Sns_Right.vue'

export default {
  name: 'SNS',
  components: {
    Com_Sns_Left,
    Com_Sns_Right,
  }
}
</script>