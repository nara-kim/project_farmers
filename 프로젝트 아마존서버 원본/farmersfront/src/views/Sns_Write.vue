<template>
  <div class="Write">
    <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
            <Com_Sns_Write/>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Com_Sns_Write from '@/components/Com_Sns_Write.vue'

export default {
  name: 'Write',
  components: {
    Com_Sns_Write,
  }
}
</script>