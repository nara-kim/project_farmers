<template>
<div class="container">
    <div class="card">
        <div class="row">
            <!-- <aside class="col-sm-5 border-right">
                <article class="gallery-wrap">  -->
                <!-- <div class="img-big-wrap">
                <div><img src="img/vvvvv.jpg"></div>
                </div> -->
                <!-- <div class="img-small-wrap">
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                    <div class="item-gallery"> <img src="https://s9.postimg.org/tupxkvfj3/image.jpg"> </div>
                </div> -->
                <!-- </article>
            </aside> -->
    <aside class="col-sm-12">
    <article class="card-body p-5">
        <h3 class="title mb-3">{{detail.title}}</h3>

    <!-- <p class="price-detail-wrap"> 
        <span class="price h3 text-warning"> 
            <span class="currency">일당!!</span><span class="num">시급 10,000</span>
        </span> 
        <span>원</span> 
    </p> -->
    <dl class="item-property">
    <dt>내용</dt>
    <dd><p>{{detail.content}}</p></dd>
    </dl>
    <dl class="param param-feature">
    <dt>지역</dt>
    <dd>{{detail.location1}} {{detail.location2}}</dd>
    </dl>  <!-- item-property-hor .// -->
    <dl class="param param-feature">
    <dt>날짜</dt>
    <dd>{{detail.help_date}}</dd>
    </dl>  <!-- item-property-hor .// -->
    <dl class="param param-feature">
    <dt>인원</dt>
    <dd>{{detail.people}}</dd>
    </dl>  <!-- item-property-hor .// -->

    <hr>

    <a href="#" class="btn btn-lg btn-primary text-uppercase"> 수정 </a>

    
    <a href="#" class="btn btn-lg btn-outline-primary text-uppercase" @click="removeCheck"> 삭제 </a>

    </article> <!-- card-body.// -->
    </aside> <!-- col.// -->
    </div> <!-- row.// -->
    </div> <!-- card.// -->


</div>
<!--container.//-->
</template>

<script>
import axios from 'axios';
export default {
    data() {
        return{
            helpid:'',
            detail:'',
        }
    },

    props: {
    // helpid: {
    //   type: String
    // }
  },

    methods:{
        gethelp(helpid) {
        axios
            .get(`http://127.0.0.1:8000/helppage/helpdetail/${helpid}/`)
            .then(res => {
                const {data} = res
                this.detail = data
            })
            .catch(err => console.log(err));
        },
        deletehelp(){
            console.log('ggggg')
            axios
                .delete(`http://127.0.0.1:8000/helppage/helpdelete/${this.detail.id}/`)
                .then( ()=> {
                    this.$router.push('/board')
                })
                .catch(err => console.log(err))
        },
        removeCheck() {
            if (confirm("정말 삭제하시겠습니까??") == true){
                this.deletehelp()
            }else{ 
                return false;
            }
        },
    },
    mounted(){
        this.helpid = this.$route.params.filterlist
        this.gethelp(this.helpid)

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