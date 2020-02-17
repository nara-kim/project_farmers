<template>
    <div style="font-family: 'Nanum Gothic', sans-serif; font-weight:bold; margin-top:40px;">
      가축질병 위기단계 <hr>
        <div class="thumb" v-for="(key, val) of Object.entries(sick)" v-bind:key="val">
          <a href="http://www.mafra.go.kr/FMD-AI/" target="_blank">
            <img v-bind:src="`${key[1]}`" alt="" style="width:100%">
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
    .get('http://127.0.0.1:8000/api/sickinfo/')
    .then(res=>{
        console.log(res.data)
        this.sick = res.data
        console.log(this.sick)
    })

}
}
</script>