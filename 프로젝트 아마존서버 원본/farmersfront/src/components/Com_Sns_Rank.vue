<template>
  <div id="outer_btn_right">
      <div class="card" style="height: 30rem;">
        <img src="img/rank.png" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title" style="text-align:center; font-family:'Jua', sans-serif;">게시글</h5>
                    <div style="font-family:'Jua', sans-serif;">
                        <div class="mb-1">
                            <span>
                                <img src="img/first.png" style="width:23px;"> {{ranker.sns1_name}} ({{ranker.sns1_id}})
                            </span>
                            <span>
                                {{ranker.sns1_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/second.png" style="width:23px;"> {{ranker.sns2_name}} ({{ranker.sns2_id}})
                            </span>
                            <span>
                                {{ranker.sns2_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/third.png" style="width:23px;"> {{ranker.sns3_name}} ({{ranker.sns3_id}})
                            </span>
                            <span>
                                {{ranker.sns3_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/etc.png" style="width:23px;"> {{ranker.sns4_name}} ({{ranker.sns4_id}}) 
                            </span>
                            <span>
                                {{ranker.sns4_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/etc.png" style="width:23px;"> {{ranker.sns5_name}} ({{ranker.sns5_id}})  
                            </span>
                            <span>
                                {{ranker.sns5_count}}개
                            </span>
                        </div>
                    </div>
                <h5 class="card-title mt-3" style="text-align:center; font-family:'Jua', sans-serif;">댓글</h5>
                    <div style="font-family:'Jua', sans-serif;">
                        <div class="mb-1">
                            <span>
                                <img src="img/first.png" style="width:23px;"> {{ranker.comment1_name}} ({{ranker.comment1_id}})
                            </span>    
                            <span>
                                {{ranker.comment1_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/second.png" style="width:23px;"> {{ranker.comment2_name}} ({{ranker.comment2_id}})
                            </span>
                            <span>
                                {{ranker.comment2_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/third.png" style="width:23px;"> {{ranker.comment3_name}} ({{ranker.comment3_id}})
                            </span>
                            <span>
                                {{ranker.comment3_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/etc.png" style="width:23px;"> {{ranker.comment4_name}} ({{ranker.comment4_id}}) 
                            </span>
                            <span>
                                {{ranker.comment4_count}}개
                            </span>
                        </div>
                        <div class="mb-1">
                            <span>
                                <img src="img/etc.png" style="width:23px;"> {{ranker.comment5_name}} ({{ranker.comment5_id}})  
                            </span>
                            <span>
                                {{ranker.comment5_count}}개
                            </span>
                        </div>
                    </div>
            </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data(){
        return {
            ranker: []
        }
    },
    methods:{
        getRank(){
            axios
                .get(`http://15.165.77.204:8000/sns/todo/getranker/`)
                .then((res)=>{
                    this.ranker = res.data
                })
                .catch((err)=>{
                    console.log(err)
                })
        }
    },
    mounted(){
        this.getRank()
    }

}
</script>

<style>
#outer_btn_right { display: flex; }

@media screen and (max-width: 980px) { #outer_btn_right { display: none; } }

</style>