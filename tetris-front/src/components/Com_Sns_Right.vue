<template>
    <!-- Start Blog Post Siddebar -->
    <div class="col-lg-6 offset-lg-3 sidebar-widgets" style="border:1px solid #ddd; margin-bottom:30px;">
        <div class="widget-wrap">
            <!-- <div class="single-sidebar-widget newsletter-widget"> -->
            <!-- <h4 class="single-sidebar-widget__title">누구누구님 환영합니다.</h4> -->
            <div class="form-group mt-30">
                <div class="col-autos">
                <!-- <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Enter email" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Enter email'"> -->
                </div>
            </div>
                    
            <!-- <button type="button" class="bbtns d-block mt-20 w-100" data-toggle="modal" data-target="#exampleModalCenter">
                글쓰기
            </button> -->

           <!-- <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true"> -->
  <!-- <div class="modal-dialog modal-dialog-centered" role="document"> -->
    <!-- <div class="modal-content"> -->
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">SNS 업로드</h5>
        <!-- <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button> -->
      </div>
      <div class="modal-body">
            
            <textarea class="input_text" type="text" v-model="title" placeholder="무슨생각을 하고 계시나요?" style="background-color:rgba(255, 255, 255, 0.973); "></textarea>    
            <div class="filebox preview-image">
                <hr>
                <input type="file" id="input-file" ref="file" class="upload-hidden" v-on:change="handleFileUpload()">
                <!-- <img type = "file" src="img/camera.png" style="width:20%;"  for="input-file"> -->
                <label for="input-file" style="border:none; display:inline-block; width:30px;" img="img/camera.png">               
                 <img type = "file" src="img/camera.png" style="width:100%; float:right;" >
                </label>
                <button type="button" class="btn btn-primary" v-on:click="CreateSns()" data-dismiss="modal" style="background-color:gray; border:none; float:right;">Save changes</button>
            </div>

      </div>
      <!-- <div class="modal-footer"> -->
    <!-- <div class="footer11"> -->
        <!-- <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> -->
      </div>
    </div>
  <!-- </div> -->
        <!-- </div> -->

                       
</template>


<script src="//cdnjs.cloudflare.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script>
import axios from 'axios';
export default {
    name: 'Com_Sns_Right',
  props: {
    msg: String
  },
  data(){
    return{
        file:'',
        title:'',
    }
  },
  methods: {
    CreateSns(){
        let formData = new FormData();
        formData.append('file', this.file);
        formData.append('title', this.title);
        formData.append('user', this.userName)
        axios
        .post( 'http://127.0.0.1:8000/sns/todo/snscreate/',
            formData,
            {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }
        ).then(res=>{
            

            this.datalist = res.data
            this.file = ''
            this.title = ''
            this.$router.push('/sns');
        })
        .catch(function(){
          console.log('FAILURE!!');
        });
    },
    handleFileUpload(){
            this.file = this.$refs.file.files[0];
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
    computed:{
        userName() {
        return this.$store.getters.loggedInUser.username;
        }
    },
    mounted(){
        this.aa();
        this.bb();
    }
}
</script>

<style scoped>
.input_text{
    width: 100%;
}

/* imaged preview */
.filebox .upload-display {
    /* 이미지가 표시될 지역 */
    margin-bottom: 5px;
}
@media(min-width: 768px) { 
    .filebox .upload-display { 
        display: inline-block;
        margin-right: 5px; 
        margin-bottom: 0; 
    } 
} 
.filebox .upload-thumb-wrap {
    /* 추가될 이미지를 감싸는 요소 */
    display: inline-block; 
    width: 54px; 
    padding: 2px;
    vertical-align: middle;
    border: 1px solid #ddd;
    border-radius: 5px; 
    background-color: #fff; 
} 
.filebox .upload-display img { 
    /* 추가될 이미지 */ 
    display: block; 
    max-width: 100%; 
    width: 100%;
    height: auto; 
}
.filebox 
.upload-thumb{
    width: 50px;
}

.filebox input[type="file"] {
    position: absolute;
    width: 0;
    height: 0;
    padding: 0;
    overflow: hidden;
    border: 0;
}
.filebox label {
    display: inline-block;
    /* padding: 10px 20px; */
    color: #999;
    vertical-align: middle;
    background-color: #fdfdfd;
    cursor: pointer;
    border: 1px solid #ebebeb;
    border-radius: 5px;
}
.filebox .upload-name {
    display: inline-block;
  height: 35px;
  font-size:18px; 
  padding: 0 10px;
    vertical-align: middle;
    background-color: #d3cece;
  border: 1px solid #ebebeb;
  border-radius: 5px;

}




#input-file{
    background-color: beige;
}
</style>

