<template>

        <div class="widget-wrap" style="margin-top:40px; font-family: 'Nanum Gothic', sans-serif; font-weight:bold;">
          레이더<hr>

            <!-- <div class="single-sidebar-widget newsletter-widget"> -->
                <div id = "scroll2">
                <img src="img/rainrader.gif" alt="" style="width:350px;">
                
                <div id = "scroll4">
                  
                </div>
            <!-- </div> -->
        </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      raderlist: []
    }
  },
    mounted() {
    this.interval = setInterval(() => {
        axios
            .get('http://127.0.0.1:8000/api/rainraderinfo/')
            .then(
                response => (this.raderlist = response.data)
                );
    }, 30000000);

}
}
</script>

<style scoped>
.ra{
    background-color: blue;
    height: 420px;
}
</style>