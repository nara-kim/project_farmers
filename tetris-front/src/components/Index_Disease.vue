<template>
    <div>
        <div class="thumb" v-for="(key, val) of Object.entries(sick)" v-bind:key="val">
          <img v-bind:src="`${key[1]}`" alt="" style="margin-top:20px;">
                <a href="http://www.mafra.go.kr/FMD-AI/" target="_blank">
                  <img v-bind:src="`${key[1]}`" alt="">
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