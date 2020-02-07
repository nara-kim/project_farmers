<template>
<div>
    <!-- <div v-for="price of pricelist" v-bind:key="price.id">
      {{price.test.split('/')[1].split(',')[1].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[2].split("'")[1]}}
      {{price.test.split('/')[1].split(',')[3].split("'")[1]}}
      가격
  </div> -->





    <div class="col-lg-12">

        <div class="menu-block">
            <h3 class="menu-title">소매 시세</h3>
            <div class="row">
                 <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12 mb40">

                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">당근</h5>
                                    <span class="dish-meta">100g  /  540원</span>
                                    <div class="dish-price">
                                    <!-- <p>$10</p>   -->
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">양배추</h5>
                                    <span class="dish-meta">100g  /  980원  </span>
                                    <div class="dish-price">
                                    <!-- <p>$8</p> -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">시금치</h5>
                                    <span class="dish-meta">100g / 450원 </span>
                                    <div class="dish-price">
                                    <!-- <p>$12</p>  -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                 </div>




                <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12 mb40">

                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">당근</h5>
                                    <span class="dish-meta">100g  /  540원</span>
                                    <div class="dish-price">
                                    <!-- <p>$10</p>   -->
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">양배추</h5>
                                    <span class="dish-meta">100g  /  980원  </span>
                                    <div class="dish-price">
                                    <!-- <p>$8</p> -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">시금치</h5>
                                    <span class="dish-meta">100g / 450원 </span>
                                    <div class="dish-price">
                                    <!-- <p>$12</p>  -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                 </div>


                 <div class="col-lg-4 col-md-6 col-sm-6 col-xs-12 mb40">

                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">당근</h5>
                                    <span class="dish-meta">100g  /  540원</span>
                                    <div class="dish-price">
                                    <!-- <p>$10</p>   -->
                                </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">양배추</h5>
                                    <span class="dish-meta">100g  /  980원  </span>
                                    <div class="dish-price">
                                    <!-- <p>$8</p> -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                    <div class="menu-content">
                        <div class="row">
                            <div class="col-lg-9 col-md-9 col-sm-9 col-xs-12">
                                <div class="dish-content">
                                    <h5 class="dish-title">시금치</h5>
                                    <span class="dish-meta">100g / 450원 </span>
                                    <div class="dish-price">
                                    <!-- <p>$12</p>  -->
                                </div>
                                </div>
                                
                            </div>
                        </div>
                    </div>
                 </div>

            </div>
        </div>

    </div>
    <!--================ End Blog Post Area =================-->

    </div>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      weatherlist: []
    }
  },
  created() {
    this.all();
  },
  methods: {
    all: function () {
      axios.get('http://127.0.0.1:8000/api/weatherinfo/')
        .then( response => {
                    this.weatherlist = response.data
        })
        .catch( err => {
                    console.log(err)
      });
    }


    
  },
}
</script>



<style scoped>

.menu-block { margin-bottom: 30px; }
.menu-title { border-bottom: 3px solid #e0e6e3; margin-bottom: 36px; padding-bottom: 10px; }
.menu-content { border-bottom: 1px solid #e0e6e3; margin-bottom: 30px; }
.dish-img { }
.dish-content { margin-top: 12px; margin-bottom: 40px; }
.dish-meta { font-size: 20px; text-transform: uppercase; display: block; width: 210px; line-height: 1.7; }
.dish-title { margin-bottom: 6px; font-size: 25px; text-transform: uppercase; font-weight: 500; position: relative; }
.dish-price { position: absolute; right: 16px; top: 0px; font-size: 26px; color: #e03c23; font-weight: 500; font-family: 'Zilla Slab', serif; }
.well-block .dish-meta { width: 100%; }
.well-block .dish-price { font-size: 26px; color: #e03c23; font-weight: 500; font-family: 'Zilla Slab', serif; position: inherit; }

.img-circle{
  width: 100%;
  height: 100%;
}
</style>
