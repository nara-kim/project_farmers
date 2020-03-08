<template>
<section class="Material-contact-section section-padding section-dark" style=" font-family: 'Jua', sans-serif; ">
      <div class="container">
          <div class="row">
              <!-- Section Titile -->
              <div class="col-md-12 wow animated fadeInLeft" data-wow-delay=".2s">
                  <h1 class="section-title">
                      <span>
                          {{mypage.nickname}}
                      </span>
                      님의마이페이지
                      </h1>
                  
              </div>
          </div>
          <div class="row">
              <!-- Section Titile -->
              <div class="col-md-6 contact-widget-section2 wow animated fadeInLeft" data-wow-delay=".2s">
                <p>- 아이디, 이름은 수정이 불가능합니다.</p>
                <div class="find-widget">
                    <input type="file" id="input-file" ref="file" class="upload-hidden"  v-on:change="handleFileUpload()" style="width:150px;">
                    <label for="input-file" style="border:none; display:inline-block; width:30px;" img="img/camera.png">               
                    <!-- <img type = "file" src="img/camera.png" style="width:100%; float:right;" > -->
                    </label>
                <button class="btn btn-primary" v-on:click="inImage(userid)" v-if="`${mydata.file}`" style="background-color:blue;">
                    프로필 수정
                </button> 
                <hr>
                <img class="img-fluid" v-bind:src="`http://127.0.0.1:8000${mypage.image}/`" alt="프로필 사진을 등록해주세요" style="width:50%; border-radius:70%">
                </div>
              </div>
              <!-- contact form -->
              <div class="col-md-6 wow animated fadeInRight" data-wow-delay=".2s">
                  <form class="shake" role="form" method="post" id="contactForm" name="contact-form" data-toggle="validator">
                      <!-- Name -->
                      <!-- <div class="form-group label-floating">
                        <label class="control-label" for="name">이름</label>
                        <hr>
                        박승규
                        <div class="help-block with-errors"></div>
                      </div> -->
                    <div class="form-group label-floating">
                        <label class="control-label" for="name">아이디</label>
                        <hr>
                        {{mypage.username}}
                        <!-- <input class="form-control" id="name" type="text" name="name" required data-error="Please enter your name"> -->
                        <div class="help-block with-errors"></div>
                      </div>

                    <!-- 닉네임 -->
                      <div class="form-group label-floating">
                        <label class="control-label" for="email">닉네임</label>
                        <hr>
                        {{mypage.nickname}}
                        <!-- <input class="form-control" id="email" type="email" name="email" required data-error="Please enter your Email"> -->
                        <span style="float:right; font-weight:100"><button class = "btn">닉네임변경</button></span>
                        <div class="help-block with-errors"></div>
                      </div>  

                      <!-- email -->
                      <div class="form-group label-floating">
                        <label class="control-label" for="email">이메일</label>
                        <hr>
                        {{mypage.email}}
                        <span style="float:right; font-weight:100"><button class = "btn">이메일변경</button></span>

                        <!-- <input class="form-control" id="email" type="email" name="email" required data-error="Please enter your Email"> -->
                        <div class="help-block with-errors"></div>
                      </div>

                    <!-- 비밀번호 -->
                      <div class="form-group label-floating">
                        <label class="control-label" for="email">비밀번호</label>
                        <hr>
                        ********                          
                        <span style="float:right; font-weight:100"><button class = "btn" >비밀번호변경</button></span>

                        <div class="help-block with-errors"></div>
                      </div>

                        <!-- 휴대전화 -->
                        <!-- <div class="form-group label-floating">
                        <label class="control-label" for="email">휴대전화</label>
                        <hr>
                        010-1111-2222
                        <div class="help-block with-errors"></div>
                      </div> -->

                      
                      <!-- Form Submit -->
                      <!-- <div class="form-submit mt-5">
                          <button class="btn btn-common" type="submit" id="form-submit"><i class="material-icons mdi mdi-message-outline"></i> Send Message</button>
                          <div id="msgSubmit" class="h3 text-center hidden"></div>
                          <div class="clearfix"></div>
                      </div> -->
                  </form>
              </div>
          </div>
      </div>
    </section>
</template>
<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
import axios from 'axios'
import { mapGetters } from 'vuex';
export default {
    data(){
        return{
            userid:'',
            mypage:'',
            mydata:{
                file:'',
            },
            getsns: []
        }       
    },
    computed: {
    ...mapGetters(["imgrequestHeader",])
    },
    methods:{
        getSns(){
            axios
                .get(`http://127.0.0.1:8000/sns/todo/${this.sns.id}/comment/`)
                .then((res)=>{
                    this.getsns = res.data
                    // this.comments.push(res.data)
  
                })
                .catch((e)=>{
                    console.log(e)
                })
        },
        getMypage(userid){
            const requestHeader = {
                headers: {
                Authorization: 'JWT ' + this.token
                }
            }
            console.log(userid)
            axios
                .get(`http://127.0.0.1:8000/auth/accounts/mypage/${userid}/`,requestHeader)
                .then(res => {
                    const {data} = res
                    this.mypage = data
                })
                .catch(err => console.log(err))
        },
        inImage(userid){
            let formData = new FormData();
            formData.append('file', this.mydata.file)
            axios
                .post(`http://127.0.0.1:8000/auth/accounts/inimage/${userid}/`, formData,this.imgrequestHeader)
                .then((res)=>{
                    console.log('성공')
                    alert('프로필 수정이 완료되었습니다.')
                    this.getMypage(userid)
                })
                .catch(err =>console.log)
        },
            handleFileUpload(){
            this.mydata.file = this.$refs.file.files[0];
        },
        aa(){
            //preview image
            var imgTarget = $('.preview-image .upload-hidden');
            imgTarget.on('change', function(){
                var parent = $(this).parent();
                parent.children('.upload-display').remove();
                if(window.FileReader){
                    //image 파일만
                    if (!$(this)[0].files[0].type.match(/image\//)) return;
                    
                    var reader = new FileReader();
                    reader.onload = function(e){ 
                        var src = e.target.result; 
                        parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img src="'+src+'" class="upload-thumb" style="width:50%; display: block; margin: 0px auto;"></div></div>'); 
                    }
                    reader.readAsDataURL($(this)[0].files[0]);
                }
                
                else { 
                    $(this)[0].select();
                    $(this)[0].blur(); 
                    var imgSrc = document.selection.createRange().text;
                    parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img class="upload-thumb"></div></div>');
                    
                    var img = $(this).siblings('.upload-display').find('img');
                    img[0].style.filter = "progid:DXImageTransform.Microsoft.AlphaImageLoader(enable='true',sizingMethod='scale',src=\""+imgSrc+"\")";
                }
            });
        },
        bb(){
            $("#file").on('change',function(){
            var fileName = $("#file").val();
            $(".upload-name").val(fileName);
            });
        }
    },
    mounted(){
        this.userid = this.$route.params.userid
        this.getMypage(this.userid)
        this.aa()
        this.bb()
    }
}
</script>
<style scoped>
@import url("https://fonts.googleapis.com/css?family=Rubik:500,700|Roboto:400,600");
.btn{
    width:100px;
    background-color:#D2D2D2;
    border-radius:5px;
}
.btn:hover{
    opacity: 0.5;
}
.section-padding {
    padding: 45px 0;
}
.section-dark {
    background-color: #f9f9f9;
    z-index: -2;
}
.form-control,
.form-group .form-control {
    border: 0;
    background-image: -webkit-gradient(linear, left top, left bottom, from(#009688), to(#009688)), -webkit-gradient(linear, left top, left bottom, from(#D2D2D2), to(#D2D2D2));
    background-image: -webkit-linear-gradient(#009688, #009688), -webkit-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: -o-linear-gradient(#009688, #009688), -o-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: linear-gradient(#009688, #009688), linear-gradient(#D2D2D2, #D2D2D2);
    -webkit-background-size: 0 2px, 100% 1px;
    background-size: 0 2px, 100% 1px;
    background-repeat: no-repeat;
    background-position: center bottom, center -webkit-calc(100% - 1px);
    background-position: center bottom, center calc(100% - 1px);
    background-color: rgba(0, 0, 0, 0);
    -webkit-transition: background 0s ease-out;
    -o-transition: background 0s ease-out;
    transition: background 0s ease-out;
    float: none;
    -webkit-box-shadow: none;
    box-shadow: none;
    border-radius: 0
}

.form-control::-moz-placeholder,
.form-group .form-control::-moz-placeholder {
    color: #BDBDBD;
    font-weight: 400
}

.form-control:-ms-input-placeholder,
.form-group .form-control:-ms-input-placeholder {
    color: #BDBDBD;
    font-weight: 400
}

.form-control::-webkit-input-placeholder,
.form-group .form-control::-webkit-input-placeholder {
    color: #BDBDBD;
    font-weight: 400
}

.form-control[disabled],
.form-control[readonly],
.form-group .form-control[disabled],
.form-group .form-control[readonly],
fieldset[disabled] .form-control,
fieldset[disabled] .form-group .form-control {
    background-color: rgba(0, 0, 0, 0)
}

.form-control[disabled],
.form-group .form-control[disabled],
fieldset[disabled] .form-control,
fieldset[disabled] .form-group .form-control {
    background-image: none;
    border-bottom: 1px dotted #D2D2D2
}

.form-group {
    position: relative
}

.form-group.label-floating label.control-label,
.form-group.label-placeholder label.control-label,
.form-group.label-static label.control-label {
    position: absolute;
    pointer-events: none;
    -webkit-transition: .3s ease all;
    -o-transition: .3s ease all;
    transition: .3s ease all
}

.form-group.label-floating label.control-label {
    will-change: left, top, contents
}

.form-group.label-placeholder:not(.is-empty) label.control-label {
    display: none
}

.form-group .help-block {
    position: absolute;
    display: none
}

.form-group.is-focused .form-control {
    outline: 0;
    background-image: -webkit-gradient(linear, left top, left bottom, from(#009688), to(#009688)), -webkit-gradient(linear, left top, left bottom, from(#D2D2D2), to(#D2D2D2));
    background-image: -webkit-linear-gradient(#009688, #009688), -webkit-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: -o-linear-gradient(#009688, #009688), -o-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: linear-gradient(#009688, #009688), linear-gradient(#D2D2D2, #D2D2D2);
    -webkit-background-size: 100% 2px, 100% 1px;
    background-size: 100% 2px, 100% 1px;
    -webkit-box-shadow: none;
    box-shadow: none;
    -webkit-transition-duration: .3s;
    -o-transition-duration: .3s;
    transition-duration: .3s
}

.form-group.is-focused .form-control .material-input:after {
    background-color: #009688
}

.form-group.is-focused label,
.form-group.is-focused label.control-label {
    color: #009688
}

.form-group.is-focused.label-placeholder label,
.form-group.is-focused.label-placeholder label.control-label {
    color: #BDBDBD
}

.form-group.is-focused .help-block {
    display: block
}

.form-group.has-warning .form-control {
    -webkit-box-shadow: none;
    box-shadow: none
}

.form-group.has-warning.is-focused .form-control {
    background-image: -webkit-gradient(linear, left top, left bottom, from(#ff5722), to(#ff5722)), -webkit-gradient(linear, left top, left bottom, from(#D2D2D2), to(#D2D2D2));
    background-image: -webkit-linear-gradient(#ff5722, #ff5722), -webkit-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: -o-linear-gradient(#ff5722, #ff5722), -o-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: linear-gradient(#ff5722, #ff5722), linear-gradient(#D2D2D2, #D2D2D2)
}

.form-group.has-warning .help-block,
.form-group.has-warning label.control-label {
    color: #ff5722
}

.form-group.has-error .form-control {
    -webkit-box-shadow: none;
    box-shadow: none
}

.form-group.has-error .help-block,
.form-group.has-error label.control-label {
    color: #f44336
}

.form-group.has-success .form-control {
    -webkit-box-shadow: none;
    box-shadow: none
}

.form-group.has-success.is-focused .form-control {
    background-image: -webkit-gradient(linear, left top, left bottom, from(#4caf50), to(#4caf50)), -webkit-gradient(linear, left top, left bottom, from(#D2D2D2), to(#D2D2D2));
    background-image: -webkit-linear-gradient(#4caf50, #4caf50), -webkit-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: -o-linear-gradient(#4caf50, #4caf50), -o-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: linear-gradient(#4caf50, #4caf50), linear-gradient(#D2D2D2, #D2D2D2)
}

.form-group.has-success .help-block,
.form-group.has-success label.control-label {
    color: #4caf50
}

.form-group.has-info .form-control {
    -webkit-box-shadow: none;
    box-shadow: none
}

.form-group.has-info.is-focused .form-control {
    background-image: -webkit-gradient(linear, left top, left bottom, from(#03a9f4), to(#03a9f4)), -webkit-gradient(linear, left top, left bottom, from(#D2D2D2), to(#D2D2D2));
    background-image: -webkit-linear-gradient(#03a9f4, #03a9f4), -webkit-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: -o-linear-gradient(#03a9f4, #03a9f4), -o-linear-gradient(#D2D2D2, #D2D2D2);
    background-image: linear-gradient(#03a9f4, #03a9f4), linear-gradient(#D2D2D2, #D2D2D2)
}

.form-group.has-info .help-block,
.form-group.has-info label.control-label {
    color: #03a9f4
}

.form-group textarea {
    resize: none
}

.form-group textarea~.form-control-highlight {
    margin-top: -11px
}

.form-group select {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

.form-group select~.material-input:after {
    display: none
}

.form-control {
    margin-bottom: 7px
}

.form-control::-moz-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-control:-ms-input-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-control::-webkit-input-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}
.checkbox label,
.radio label,
label {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

label.control-label {
    font-size: 12px;
    line-height: 1.07142857;
    font-weight: 400;
    margin: 16px 0 0 0
}

.help-block {
    margin-top: 0;
    font-size: 12px
}

.form-group {
    padding-bottom: 7px;
    margin: 28px 0 0 0
}

.form-group .form-control {
    margin-bottom: 7px
}

.form-group .form-control::-moz-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-group .form-control:-ms-input-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-group .form-control::-webkit-input-placeholder {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-group .checkbox label,
.form-group .radio label,
.form-group label {
    font-size: 16px;
    line-height: 1.42857143;
    color: #BDBDBD;
    font-weight: 400
}

.form-group label.control-label {
    font-size: 12px;
    line-height: 1.07142857;
    font-weight: 400;
    margin: 16px 0 0 0
}

.form-group .help-block {
    margin-top: 0;
    font-size: 12px
}

.form-group.label-floating label.control-label,
.form-group.label-placeholder label.control-label {
    top: -7px;
    font-size: 16px;
    line-height: 1.42857143
}

.form-group.label-floating.is-focused label.control-label,
.form-group.label-floating:not(.is-empty) label.control-label,
.form-group.label-static label.control-label {
    top: -30px;
    left: 0;
    font-size: 12px;
    line-height: 1.07142857
}

.form-group.label-floating input.form-control:-webkit-autofill~label.control-label label.control-label {
    top: -30px;
    left: 0;
    font-size: 12px;
    line-height: 1.07142857
}

.form-group.form-group-sm {
    padding-bottom: 3px;
    margin: 21px 0 0 0
}

.form-group.form-group-sm .form-control {
    margin-bottom: 3px
}

.form-group.form-group-sm .form-control::-moz-placeholder {
    font-size: 11px;
    line-height: 1.5;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-sm .form-control:-ms-input-placeholder {
    font-size: 11px;
    line-height: 1.5;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-sm .form-control::-webkit-input-placeholder {
    font-size: 11px;
    line-height: 1.5;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-sm .checkbox label,
.form-group.form-group-sm .radio label,
.form-group.form-group-sm label {
    font-size: 11px;
    line-height: 1.5;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-sm label.control-label {
    font-size: 9px;
    line-height: 1.125;
    font-weight: 400;
    margin: 16px 0 0 0
}

.form-group.form-group-sm .help-block {
    margin-top: 0;
    font-size: 9px
}

.form-group.form-group-sm.label-floating label.control-label,
.form-group.form-group-sm.label-placeholder label.control-label {
    top: -11px;
    font-size: 11px;
    line-height: 1.5
}

.form-group.form-group-sm.label-floating.is-focused label.control-label,
.form-group.form-group-sm.label-floating:not(.is-empty) label.control-label,
.form-group.form-group-sm.label-static label.control-label {
    top: -25px;
    left: 0;
    font-size: 9px;
    line-height: 1.125
}

.form-group.form-group-sm.label-floating input.form-control:-webkit-autofill~label.control-label label.control-label {
    top: -25px;
    left: 0;
    font-size: 9px;
    line-height: 1.125
}

.form-group.form-group-lg {
    padding-bottom: 9px;
    margin: 30px 0 0 0
}

.form-group.form-group-lg .form-control {
    margin-bottom: 9px
}

.form-group.form-group-lg .form-control::-moz-placeholder {
    font-size: 18px;
    line-height: 1.3333333;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-lg .form-control:-ms-input-placeholder {
    font-size: 18px;
    line-height: 1.3333333;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-lg .form-control::-webkit-input-placeholder {
    font-size: 18px;
    line-height: 1.3333333;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-lg .checkbox label,
.form-group.form-group-lg .radio label,
.form-group.form-group-lg label {
    font-size: 18px;
    line-height: 1.3333333;
    color: #BDBDBD;
    font-weight: 400
}

.form-group.form-group-lg label.control-label {
    font-size: 14px;
    line-height: .99999998;
    font-weight: 400;
    margin: 16px 0 0 0
}

.form-group.form-group-lg .help-block {
    margin-top: 0;
    font-size: 14px
}

.form-group.form-group-lg.label-floating label.control-label,
.form-group.form-group-lg.label-placeholder label.control-label {
    top: -5px;
    font-size: 18px;
    line-height: 1.3333333
}

.form-group.form-group-lg.label-floating.is-focused label.control-label,
.form-group.form-group-lg.label-floating:not(.is-empty) label.control-label,
.form-group.form-group-lg.label-static label.control-label {
    top: -32px;
    left: 0;
    font-size: 14px;
    line-height: .99999998
}

.form-group.form-group-lg.label-floating input.form-control:-webkit-autofill~label.control-label label.control-label {
    top: -32px;
    left: 0;
    font-size: 14px;
    line-height: .99999998
}

select.form-control {
    border: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
    border-radius: 0
}

.form-group.is-focused select.form-control {
    -webkit-box-shadow: none;
    box-shadow: none;
    border-color: #D2D2D2
}

.form-group.is-focused select.form-control[multiple],
select.form-control[multiple] {
    height: 85px
}

.input-group-btn .btn {
    margin: 0 0 7px 0
}

.form-group.form-group-sm .input-group-btn .btn {
    margin: 0 0 3px 0
}

.form-group.form-group-lg .input-group-btn .btn {
    margin: 0 0 9px 0
}

.input-group .input-group-btn {
    padding: 0 12px
}

.input-group .input-group-addon {
    border: 0;
    background: 0 0
}

.form-group input[type=file] {
    opacity: 0;
    position: absolute;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 100
}
.contact-widget-section .single-contact-widget {
    background: #f9f9f9;
    padding: 20px 25px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.26);
    height: 260px;
    margin-top: 25px;
    transition: all 0.3s ease-in-out
}

.contact-widget-section .single-contact-widget i {
    font-size: 75px
}

.contact-widget-section .single-contact-widget h3 {
    font-size: 20px;
    color: #333;
    font-weight: 700;
    padding-bottom: 10px
}

.contact-widget-section .single-contact-widget p {
    line-height: 16px
}

.contact-widget-section .single-contact-widget:hover {
    background: #fff;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.46);
    cursor: pointer;
    transition: all 0.3s ease-in-out
}

#contactForm {
    margin-top: -10px
}

#contactForm .form-group label.control-label {
    color: #8c8c8c
}

#contactForm .form-control {
    font-weight: 500;
    height: auto
}
.btn .btn-light:hover{
    opacity: 0.5;
    color:#333;
}



</style>