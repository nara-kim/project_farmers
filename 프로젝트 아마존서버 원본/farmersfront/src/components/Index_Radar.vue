<template>

        <div class="widget-wrap" style="margin-top:40px; font-family: 'Jua', sans-serif; font-size:2.0em" >
          강수 레이더영상<hr style="background-color: orange;height: 1.5px;">
                <div id = "scroll2">
                  <img src="http://15.165.77.204:8000/rainrader.gif/" style="width:100%">
                <div id = "scroll4">
                </div>
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
            .get('http://15.165.77.204:8000/api/rainraderinfo/')
            .then(
                response => (this.raderlist = response.data)
                );
    }, 300000);

}
}
</script>
<style scoped>
.ra{
    background-color: blue;
    height: 420px;
}
</style>