<template>
<div>
  <div v-for="price of pricelist" v-bind:key="price.id">
      {{price.test.split('/')[1].split(',')[1].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[2].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[3].split("'")[1]}}
      가격
  </div>

<div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="img/vv.jpg" alt="First slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="img/vvv.jpg" alt="Second slide">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="img/vvvv.jpg" alt="Third slide">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>



  <h1>asdasd</h1>
</div>

</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      pricelist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/priceinfo/')
        .then( response => {
                    this.pricelist = response.data
        })
        .catch( err => {
                    console.log(err)
      });
    }


    
  },
}
</script>




<style scoped>
.main-text
{
    position: absolute;
    top: 50px;
    width: 96.66666666666666%;
    color: #FFF;
}
.btn-min-block
{
    min-width: 170px;
    line-height: 26px;
}
.btn-clear
{
    color: #FFF;
    background-color: transparent;
    border-color: #FFF;
    margin-right: 15px;
}
.btn-clear:hover
{
    color: #000;
    background-color: #FFF;
}


</style>