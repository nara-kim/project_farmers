<template>
<div class="container">
    <div class="card">
        <div class="row">
    <aside class="col-sm-12">
    <article class="card-body p-5">
        <h3 class="title mb-3">{{detail.title}}</h3>
 
    <dl class="item-property">
    <dt>내용</dt>
    <dd><p>{{detail.content}}</p></dd>
    </dl>
    <dl class="param param-feature">
    <dt>지역</dt>
    <dd>{{detail.location1}} {{detail.location2}}</dd>
    </dl>  
    <dl class="param param-feature">
    <dt>날짜</dt>
    <dd>{{detail.help_date}}</dd>
    </dl>  
    <dl class="param param-feature">
    <dt>인원</dt>
    <dd>{{detail.people}}</dd>
    </dl> 

    <hr>

    <a href="#" class="btn btn-lg btn-primary text-uppercase"> 수정 </a>
    <a href="#" class="btn btn-lg btn-outline-primary text-uppercase"> 삭제 </a>
    </article>
    </aside> 
    </div> 
    </div> 


</div>
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return{
            filterlist:'',
            detail:'',
        }
    },

    props: {

  },

    methods:{
        getMovie(filterlist) {
        axios
            .get(`http://15.165.77.204:8000/helppage/helpdetail/${filterlist}/`)
            .then(res => {
                const {data} = res
                this.detail = data
            })
            .catch(err => console.log(err));
        },

    },
    mounted(){
        this.filterlist = this.$route.params.filterlist
        this.getMovie(this.filterlist)

    }
}
</script>
<style scoped>
.gallery-wrap .img-big-wrap img {
    height: 450px;
    width: auto;
    display: inline-block;
    cursor: zoom-in;
}


.gallery-wrap .img-small-wrap .item-gallery {
    width: 60px;
    height: 60px;
    border: 1px solid #ddd;
    margin: 7px 2px;
    display: inline-block;
    overflow: hidden;
}

.gallery-wrap .img-small-wrap {
    text-align: center;
}
.gallery-wrap .img-small-wrap img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;
    border-radius: 4px;
    cursor: zoom-in;
}
</style>