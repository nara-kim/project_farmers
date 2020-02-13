<template>
    <!-- Start Blog Post Siddebar -->
    <div class="col-lg-4 offset-lg-1 sidebar-widgets">
        <div class="widget-wrap">
            <div class="single-sidebar-widget newsletter-widget">
            <h4 class="single-sidebar-widget__title">누구누구님 환영합니다.</h4>
            <div class="form-group mt-30">
                <div class="col-autos">
                <!-- <input type="text" class="form-control" id="inlineFormInputGroup" placeholder="Enter email" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Enter email'"> -->
                </div>
            </div>
                    
            <button type="button" class="bbtns d-block mt-20 w-100" data-toggle="modal" data-target="#exampleModalCenter">
                글쓰기
            </button>
        </div>


            <div class="single-sidebar-widget post-category-widget">
            <h4 class="single-sidebar-widget__title">Catgory</h4>
            <ul class="cat-list mt-20">
                <li>
                <a href="#" class="d-flex justify-content-between">
                    <p>Technology</p>
                    <p>(03)</p>
                </a>
                </li>
                <li>
                <a href="#" class="d-flex justify-content-between">
                    <p>Software</p>
                    <p>(09)</p>
                </a>
                </li>
                <li>
                <a href="#" class="d-flex justify-content-between">
                    <p>Lifestyle</p>
                    <p>(12)</p>
                </a>
                </li>
                <li>
                <a href="#" class="d-flex justify-content-between">
                    <p>Shopping</p>
                    <p>(02)</p>
                </a>
                </li>
                <li>
                <a href="#" class="d-flex justify-content-between">
                    <p>Food</p>
                    <p>(10)</p>
                </a>
                </li>
            </ul>
            </div>

            <div class="single-sidebar-widget popular-post-widget">
            <h4 class="single-sidebar-widget__title">Popular Post</h4>
            <div class="popular-post-list">
                <div class="single-post-list">
                <div class="thumb">
                    <img class="card-img rounded-0" src="img/blog/thumb/thumb1.png" alt="">
                    <ul class="thumb-info">
                    <li><a href="#">Adam Colinge</a></li>
                    <li><a href="#">Dec 15</a></li>
                    </ul>
                </div>
                <div class="details mt-20">
                    <a href="blog-single.html">
                    <h6>Accused of assaulting flight attendant miktake alaways</h6>
                    </a>
                </div>
                </div>
                <div class="single-post-list">
                <div class="thumb">
                    <img class="card-img rounded-0" src="img/blog/thumb/thumb2.png" alt="">
                    <ul class="thumb-info">
                    <li><a href="#">Adam Colinge</a></li>
                    <li><a href="#">Dec 15</a></li>
                    </ul>
                </div>
                <div class="details mt-20">
                    <a href="blog-single.html">
                    <h6>Tennessee outback steakhouse the
                        worker diagnosed</h6>
                    </a>
                </div>
                </div>
                <div class="single-post-list">
                <div class="thumb">
                    <img class="card-img rounded-0" src="img/blog/thumb/thumb3.png" alt="">
                    <ul class="thumb-info">
                    <li><a href="#">Adam Colinge</a></li>
                    <li><a href="#">Dec 15</a></li>
                    </ul>
                </div>
                <div class="details mt-20">
                    <a href="blog-single.html">
                    <h6>Tennessee outback steakhouse the
                        worker diagnosed</h6>
                    </a>
                </div>
                </div>
            </div>
            </div>

            <div class="single-sidebar-widget tag_cloud_widget">
                <h4 class="single-sidebar-widget__title">Popular Post</h4>
                <ul class="list">
                <li>
                    <a href="#">project</a>
                </li>
                <li>
                    <a href="#">love</a>
                </li>
                <li>
                    <a href="#">technology</a>
                </li>
                <li>
                    <a href="#">travel</a>
                </li>
                <li>
                    <a href="#">software</a>
                </li>
                <li>
                    <a href="#">life style</a>
                </li>
                <li>
                    <a href="#">design</a>
                </li>
                <li>
                    <a href="#">illustration</a>
                </li>
                </ul>
            </div>
            </div>

                        <!-- Modal -->
<div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalCenterTitle">Modal title</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body">
            <input type="file" id="8" ref="file" v-on:change="handleFileUpload()"/>
            <textarea class="input_text" type="text" v-model="title" placeholder="무슨생각을 하고 계시나요?"></textarea>    



		<div class="filebox preview-image">
            <input class="upload-name" value="파일선택" disabled="disabled">
            <label for="input-file">업로드</label>
            <input type="file" id="input-file" class="upload-hidden">
        </div>


      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary" v-on:click="CreateSns()" data-dismiss="modal">Save changes</button>
      </div>
    </div>
  </div>

</div>
        </div>
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
                    parent.prepend('<div class="upload-display"><div class="upload-thumb-wrap"><img src="'+src+'" class="upload-thumb" style="width:50%"></div></div>'); 
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


    }
  },
    computed:{
        userName() {
        return this.$store.getters.loggedInUser.username;
        }
    },
    mounted(){
        this.aa();
    }
}
</script>

<style scoped>
.input_text{
    width: 100%;
    margin-top: 5%;
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

</style>


