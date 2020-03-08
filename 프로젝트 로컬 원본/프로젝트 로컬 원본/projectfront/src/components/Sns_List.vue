<template>
    <div class="cardbox shadow-lg bg-white">
        <div class="cardbox-heading">
            <div class="dropdown float-right">
                <button class="btn btn-flat btn-flat-icon" type="button" data-toggle="dropdown" aria-expanded="false">
                    <em class="fa fa-ellipsis-h"></em>
                </button>
                <div class="dropdown-menu dropdown-scale dropdown-menu-right" role="menu" style="position: absolute; transform: translate3d(-136px, 28px, 0px); top: 0px; left: 0px; will-change: transform;">
                    <a class="dropdown-item" href="#"  v-if="sns.user === loggedInUser.user_id" @click.prevent="snsCheck(sns)">게시글 삭제</a>
                    <a class="dropdown-item" href="#" v-else >본인만 삭제가능</a>
                    <a class="dropdown-item" href="#">게시글 수정</a>
                    <a class="dropdown-item" href="#">Report</a>
                </div>
            </div>
            <div class="media m-0">
              <div class="d-flex mr-3">
                  <a href=""></a>
              </div>
              <div class="media-body">
                  <p class="m-0">{{sns.username}}</p>

              </div>
            </div>
          </div>
        <div class="cardbox-item" style="text-align:center;">
            <img class="img-fluid" v-bind:src="`http://127.0.0.1:8000${sns.image}/`" alt="Image" style="width:60%;">
        </div>
        <div class="mt-3" style="padding:16px; font-family:'Jua', sans-serif;">
          {{sns.title}}
        </div>
        <hr>
        <div class="cardbox-comments">
            <span class="comment-avatar float-left">
                <a href=""><img class="rounded-circle" src="http://www.themashabrand.com/templates/bootsnipp/post/assets/img/users/6.jpg" alt="..."></a>                            
            </span>
            <div class="search">
              <input placeholder="Write a comment" type="text" v-model="comment.content">
              
              <button><img class="imgbutton" src="img/send.png" @click.prevent="commentCreate(sns)"></button>
            </div>
        </div>
        <div>
       
            <div class="comment" v-for='comment in comments' :key='comment.id' >
                <h5 class="h5comment">{{comment.content}}작성자:{{comment.username}}
                  <button class="btn btn-danger" v-if="comment.create_user === loggedInUser.user_id" @click.prevent="commentCheck(comment)" style="height:25px; width:auto;">
                    <img class="deletebutton" src="img/delete.png">
                  </button>
                </h5>
            </div>
        </div> 
    </div>
</template>

<script>
import axios from 'axios'

export default {
    props: [
        'sns'
    ],
    components:{
    },
    data(){
        return {
            comment: {
                content: '',
            },
            comments: []
        }
    },
    methods: {
        commentCreate(sns){
            const sns_id = sns
            const form = new FormData()
            form.append('content', this.comment.content)
            form.append('user', this.loggedInUser.username)
            console.log(sns_id)
            axios
                .post(`http://127.0.0.1:8000/sns/todo/${sns_id.id}/commentcreate/`,form)
                .then((res)=>{

                  this.comments.push(res.data)
                })
                .catch((err)=>{
                console.log(err)
                })
                this.comment.content = ''
        },
        getComment(){
            axios
                .get(`http://127.0.0.1:8000/sns/todo/${this.sns.id}/comment/`)
                .then((res)=>{
                    this.comments = res.data
  
                })
                .catch((e)=>{
                    console.log(e)
                })
        },
        commentDelete(comment){
          const comment_id = comment
          console.log(comment_id.id)
          axios
            .delete(`http://127.0.0.1:8000/sns/todo/${comment_id.id}/comment/`, this.requestHeader)
            .then((res)=>{
              alert('댓글이 삭제되었습니다.')
              console.log('commentdelete완료')
              console.log(res)
              this.getComment()
            })
            .catch((e)=>{
              console.log(e)
            })
        },
        snsDelete(sns){
          const sns_id = sns
          console.log(sns_id.id)
          axios
            .delete(`http://127.0.0.1:8000/sns/todo/${sns_id.id}/snsdelete/`, this.requestHeader)
            .then((res)=>{
              console.log('snsdelete완료')
              console.log(res)
              alert('게시글 삭제가 완료되었습니다.')
              this.$store.dispatch('getSnsAction')
            })
            .catch((e)=>{
              console.log(e)
            })
        },
        commentCheck(comment){
          if (confirm("정말 삭제하시겠습니까??") == true){
            this.commentDelete(comment)
          }else{ 
            return false;
          }
        },
        snsCheck(sns){
          if (confirm("정말 삭제하시겠습니까??") == true){
            this.snsDelete(sns)
          }else{ 
            return false;
          }
        }
    },

    mounted(){
      this.getComment()
    },

    computed:{
      loggedInUser() {
        return this.$store.getters.loggedInUser;
    },
      requestHeader() {
      return this.$store.getters.requestHeader;
    },
  },

}
</script>

<style scoped>

.hero {
  padding: 6.25rem 0px !important;
  margin: 0px !important;
}
.cardbox {
  border-radius: 3px;
  margin-bottom: 20px;
  padding: 0px !important;
}

.cardbox .cardbox-heading {
  padding: 16px;
  margin: 0;
}
.cardbox .btn-flat.btn-flat-icon {
 border-radius: 50%;
 font-size: 24px;
 height: 32px;
 width: 32px;
 padding: 0;
 overflow: hidden;
 color: #fff !important;
 background: #b5b6b6;
 
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
text-align: center;
}
.cardbox .float-right .dropdown-menu{
  position: relative;
  left: 13px !important;  
}
.cardbox .float-right a:hover{
  background: #f4f4f4 !important;   
}
.cardbox .float-right a.dropdown-item {
  display: block;
  width: 100%;
  padding: 4px 0px 4px 10px;
  clear: both;
  font-weight: 400;
  font-family: 'Abhaya Libre', serif;
  font-size: 14px !important;
  color: #848484;
  text-align: inherit;
  white-space: nowrap;
  background: 0 0;
  border: 0;
}


.media {
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: start;
  align-items: flex-start;
}
.d-flex {
  display: -ms-flexbox !important;
  display: flex !important;
}
.media .mr-3{
  margin-right: 1rem !important;
}
.media img{
  width: 48px !important;
  height: 48px !important;
  padding: 2px;
  border: 2px solid #f4f4f4;
} 
.media-body {
  -ms-flex: 1;
  flex: 1;
  padding: .4rem !important;
}
.media-body p{
  font-family: 'Rokkitt', serif;   
  font-weight: 500 !important;
  font-size: 14px;
  color: #88898a;
}
.media-body small span{
  font-family: 'Rokkitt', serif;   
  font-size: 12px;
  color: #aaa;
  margin-right: 10px;
}


.cardbox .cardbox-item {
    position: relative;
    display: block;
}
.cardbox .cardbox-item img{
}
.img-responsive{
    display: block;
    max-width: 100%;
    height: auto;
}   
.fw {
    width: 100% !important;
   height: auto;
}

.cardbox-base{
 border-bottom: 2px solid #f4f4f4;
}   
.cardbox-base ul{
 margin: 10px 0px 10px 15px!important; 
 padding: 10px !important;
 font-size: 0px;   
  display: inline-block;
}
.cardbox-base li {
  list-style: none;
  margin: 0px 0px 0px -8px !important;
  padding: 0px 0px 0px 0px !important;
  display: inline-block;
}

.cardbox-base li a{
  margin: 0px !important;
  padding: 0px !important;
}
.cardbox-base li a i{
 position: relative;
 top: 4px; 
 font-size: 16px;
 color: #8d8d8d;
 margin-right: 15px;
}
.cardbox-base li a span{
 font-family: 'Rokkitt', serif;
 font-size: 14px;
 color: #8d8d8d;
 margin-left: 20px;
 position: relative;
 top: 5px; 
}
.cardbox-base li a em{
 font-family: 'Rokkitt', serif;
 font-size: 14px;
 color: #8d8d8d;
 position: relative;
 top: 3px; 
}
.cardbox-base li a img{
  width: 25px;
  height: 25px;
  margin: 0px !important;
  border: 2px solid #fff;
}


/* ------------------------------- */
/* Cardbox Comments
---------------------------------- */
.cardbox-comments{
  padding: 10px 40px 20px 50px !important;
  font-size: 0px;   
  text-align: center;
  display: inline-block;
}
.cardbox-comments .comment-avatar img{
  margin-top: 1px;
  margin-right: 10px;
  position: relative;
  display: inline-block;
  text-align: center;
  width: 100%;
  height: 40px;
}
.cardbox-comments .comment-body {
  overflow: auto;
}
.search {
 position: relative;
 top: -40px;
 margin-bottom: -40px;
 border: 2px solid #f4f4f4;   
 width: 100%;
 overflow: hidden;
}
.search input[type="text"] {
 background-color: #fff;
 line-height: 10px;
 padding: 15px 60px 20px 50px;
 border: none;
 border-radius: 4px;
 width: 100%;
 font-family: 'Rokkitt', serif;
 font-size: 14px;
 color: #8d8d8d;
 height: inherit;
 font-weight: 700;
}
.search button {
 position: absolute;
 right: 0;
 top: 0px;
 border: none;
 background-color: transparent;
 color: #bbbbbb;
 padding: 15px 25px;
 /* padding: 2.5%; */
 cursor: pointer;
 width: auto;
 height: 20px;

display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
text-align: center;
}
/* .search button img {
 font-size: 20px;
 line-height: 30px;
 display: block;
} */
.imgbutton{
  width: auto;
  height: 30px;
  margin-left: 50%;
  margin-top: 60%;
  text-align: center;
}
.deletebutton{
  width: auto;
  height: 15px;
  margin-bottom: 18px;
}
.h5comment{
  position: relative;
  text-align: right;
  margin-right: 10%;
  font-size : 15px;
}


/* ------------------------------- */
/* Author
---------------------------------- */
.author a{
 font-family: 'Rokkitt', serif;
 font-size: 16px;
 color: #00C4CF;
}
.author p{
 font-family: 'Rokkitt', serif;
 font-size: 16px;
 color: #8d8d8d;
}
</style>