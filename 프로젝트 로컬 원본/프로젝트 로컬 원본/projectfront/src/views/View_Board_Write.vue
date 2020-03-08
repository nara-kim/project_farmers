<template>
    <section class="blog-post-area section-margin mt-4">
      <div class ="container">
        <div class = "row">
          <Detail_Board_Write/>
        </div>
      </div>
     </section>
</template>

<script>
import Detail_Board_Write from '@/components/Detail_Board_Write.vue'

export default {
  name: 'detail_board_write',
  components: {
    Detail_Board_Write,
  }
}
</script>