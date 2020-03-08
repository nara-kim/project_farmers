<template>
  <div class="Board">
    <Board_Map/>
    <Board_Write/>
  </div>
</template>

<script>
// @ is an alias to /src
// import One from '@/components/One.vue'
import Board_Write from '@/components/Board_Write.vue'
import Board_Map from '@/components/Board_Map.vue'

export default {
  name: 'Board',
  components: {
    Board_Write,
    Board_Map,
  }
}
</script>