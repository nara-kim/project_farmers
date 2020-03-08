<template>
     <div style="font-family: 'Jua', sans-serif; margin-top:40px;font-size:2.0em; ">
      가축질병 위기단계 <hr style="background-color: orange;height: 1.5px;">
        <div class="thumb" v-for="(key, val) of Object.entries(sick)" v-bind:key="val">
          <a href="http://www.mafra.go.kr/FMD-AI/" target="_blank" >
            <!-- <img v-bind:src="`${key[1]}`" style="width:100%;"> -->
            <img src="img/sickinfo.JPG" style="width:100%;" alt="">
          </a>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      sick: []
    }
  },
    mounted() {
    axios
    .get('http://15.165.77.204:8000/api/sickinfo/')
    .then(res=>{
        this.sick = res.data
    })

}
}
</script>