<template>
<div>
   <section id="team" class="pb-5"  style=" font-family: 'Jua', sans-serif;">
       <div style="font-size:2.0em; ">뉴스</div> <hr class ="hr1">
    <div class="container">
        <div class="row" >           
            <div class="col-xs-12 col-sm-6 col-md-4" v-for="news of newslist" v-bind:key="news.id">
                <div class="image-flip" ontouchstart="this.classList.toggle('hover');">
                    <div class="mainflip">
                        <div class="frontside">
                            <div class="card">
                                <div class="card-body text-center" style="margin-top: 20px;">
                                    <p><img class=" img-fluid" v-bind:src="news.newsimg" alt="card image"></p>
                                    <h4 class="card-title">{{news.title}}</h4>
                                </div>
                            </div>
                        </div>
                        <div class="backside">
                            <div class="card">
                                <div class="card-body text-center mt-4">
                                    <h4 class="card-title">{{news.title}}</h4>
                                    <a class="card-text" v-bind:href="news.newslink" target="_blank">{{news.discription}}</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
            
        
        <div id="scroll3">
        </div>            

        </div>
    </div>
</section>
</div>
</template>
 
<script>
import axios from 'axios';

export default {
  data() {
    return {
      newslist: []
    }
  },
  mounted(){
            this.interval = setInterval(()=>{
                axios.get('http://15.165.77.204:8000/api/newsinfoList/')
                .then(res=>{
                    res.data
                    })
            }, 3600000);
            axios.get('http://15.165.77.204:8000/api/newsinfo/')
            .then( response => {
                    this.newslist = response.data
            });

        }
}
</script>

<style scoped>
.hr1{
    background-color: orange;
    height: 1.3px;
}
/* FontAwesome for working BootSnippet :> */

@import url('https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css');
.newsdiv{
    margin-top: 3%;
    margin-bottom: 3%;
}
#team {
    background:none !important;
}

.btn-primary:hover,
.btn-primary:focus {
    background-color: #108d6f;
    border-color: #108d6f;
    box-shadow: none;
    outline: none;
}

.btn-primary {
    color: #fff;
    background-color: #007b5e;
    border-color: #007b5e;
}

/* section {
    padding: 60px 0;
} */

section .section-title {
    text-align: center;
    color: #007b5e;
    margin-bottom: 50px;
    text-transform: uppercase;
}

#team .card {
    border: none;
    background: #eeeeee;
}

.image-flip:hover .backside,
.image-flip.hover .backside {
    -webkit-transform: rotateY(0deg);
    -moz-transform: rotateY(0deg);
    -o-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    transform: rotateY(0deg);
    border-radius: .25rem;
}

.image-flip:hover .frontside,
.image-flip.hover .frontside {
    -webkit-transform: rotateY(180deg);
    -moz-transform: rotateY(180deg);
    -o-transform: rotateY(180deg);
    transform: rotateY(180deg);
}

.mainflip {
    -webkit-transition: 1s;
    -webkit-transform-style: preserve-3d;
    -ms-transition: 1s;
    -moz-transition: 1s;
    -moz-transform: perspective(1000px);
    -moz-transform-style: preserve-3d;
    -ms-transform-style: preserve-3d;
    transition: 1s;
    transform-style: preserve-3d;
    position: relative;
}

.frontside {
    position: relative;
    -webkit-transform: rotateY(0deg);
    -ms-transform: rotateY(0deg);
    z-index: 2;
    margin-bottom: 30px;
}

.backside {
    position: absolute;
    top: 0;
    left: 0;
    background: white;
    -webkit-transform: rotateY(-180deg);
    -moz-transform: rotateY(-180deg);
    -o-transform: rotateY(-180deg);
    -ms-transform: rotateY(-180deg);
    transform: rotateY(-180deg);
    -webkit-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
    -moz-box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
    box-shadow: 5px 7px 9px -4px rgb(158, 158, 158);
}

.frontside,
.backside {
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    -ms-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-transition: 1s;
    -webkit-transform-style: preserve-3d;
    -moz-transition: 1s;
    -moz-transform-style: preserve-3d;
    -o-transition: 1s;
    -o-transform-style: preserve-3d;
    -ms-transition: 1s;
    -ms-transform-style: preserve-3d;
    transition: 1s;
    transform-style: preserve-3d;
}

.frontside .card,
.backside .card {
    min-height: 212px;
}

.backside .card a {
    font-size: 15.5px;
    color: #007b5e !important;
}

.frontside .card .card-title,
.backside .card .card-title {
    color: #007b5e !important;
}

.frontside .card .card-body img {
    width: 120px;
    height: 120px;
    border-radius: 50%;
}

.card-text{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 5; 
    -webkit-box-orient: vertical;
        
}

.card-title{
    overflow: hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-line-clamp: 2; 
    -webkit-box-orient: vertical;
    font-family: 'Jua', sans-serif;
}
</style>