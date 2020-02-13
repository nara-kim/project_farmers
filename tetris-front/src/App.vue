<template>
  <div id="app">
    <div class ="farmerslogo" style="text-align:center">
    <router-link to = "/"><img class="logoimg" src="img/logo.png" alt="" ></router-link>
    </div>
    <div id="nav">
      <header class="header_area">
        <div class="main_menu">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container box_1620">
          <!-- Brand and toggle get grouped for better mobile display -->
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <!-- <router-link to = "/"><a class="navbar-brand logo_h"><img class="logoimg" src="img/logo.png" alt=""></a></router-link> -->
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
            <ul class="nav navbar-nav menu_nav justify-content-center">
              <li class="nav-item"><router-link to="/"><a class="nav-link">Home</a></router-link></li>
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->
              <li class="nav-item"><router-link to="/"><a class="nav-link">Weather</a></router-link></li>
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->
              <li class="nav-item"><router-link to="/sns"><a class="nav-link">Sns</a></router-link></li>
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->

              <li class="nav-item"><a class="nav-link">Category</a>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Pages</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="blog-details.html">Blog Details</a></li>
                </ul>
              </li>
              <li class="nav-item"><router-link to = "/board"><a class="nav-link">Board</a></router-link></li>            
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->

            </ul>
            <ul v-if="isAuthenticated" class="nav navbar-nav navbar-right navbar-social" style="width : 180px" >
              <li class ="nav-item"><a class="nav-link" style="font-size:small">{{userName}}</a></li>
              <li class="nav-item"><a class="nav-link" style="font-size:small" @click.prevent="logout">로그아웃</a></li>
            </ul>
             <ul v-else class="nav navbar-nav navbar-right navbar-social" style="width : 180px" >
              <li class ="nav-item"><router-link to="/login"><a class="nav-link" style="font-size:small">로그인</a></router-link></li>
              <li class="nav-item"><router-link to="/signup"><a class="nav-link" style="font-size:small">회원가입</a></router-link></li>
            </ul> 
          </div> 
        </div>
      </nav>
    </div>
  </header>
    </div>
    <router-view/>
    <!-- footer -->
     <div class="footer">
      <div class="footer1">
      <div class="container-fluid">
        
        <div class="container ">
        <div class="row">
          <div class="col-sm-4">
            <img class="logoimg" src="img/logo.png">
                <h6>김나라 박승규 박승재 최효진</h6>
            <br>
          </div>
          <!-- <div class="col-sm-4">
            <h2>Home</h2>
            <p>
              <i class="fa fa-home"></i><a href="#"> Home</a><br>
              <i class="fa fa-user-o"></i><a href="#"> About Us</a><br>
              <i class="fa fa-map-marker"></i><a href="#"> Contact Us</a><br>
              <i class="fa fa-briefcase"></i><a href="#"> Services</a><br>
              <i class="fa fa-question-circle"></i><a href="#"> Term & Conditions</a><br><br>
            </p>

          </div> -->
          <div class="col-sm-4 ">
            <h2>SSAFY</h2>
            <p>광주광역시 광산구 하남산단 6번로 107</p>
            <p>Samsung Software Academy For Youth</p>
          </div>

          <div class="col-sm-4 ">
            <a href="#">위로</a>
          </div>
        </div>
          <div class="clear30"></div>
      </div>
    </div>
  </div>
</div>
    <!-- footer end -->
  </div>
</template>

<script>

export default {
  methods: {
    logout() {
      this.$store.dispatch("logout");
      this.$session.remove("mmr-token");
      this.$session.destroy()
      this.$router.push("/");
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    userName() {
      return this.$store.getters.loggedInUser.username;
    }
  },
  
}
</script>

<style scoped>
.main_menu{
   border-style:solid;
   border-width: 1px;
   border-color: rgb(223, 221, 221)
   /* background-color: rgb(235, 240, 236); */
}
.logoimg{
  width: 200px;
  height: 65px;
}

/* footer */
.footer1{
 background-color: black;
 color: white;

}
.footer1 h2{
	margin: 5px;
	padding: 8px;
	font-size: 25px;
	font-family: "Times New Roman", Times, serif;
	
}
.footer1 a{
	color: white;
}
.footer1 a:hover{
	color: ;
}

.footer1 p{
	margin: 5px;
	padding-top: 2px;
	padding-left: 10px;
	font-size: 18px;
	font-family: "Times New Roman", Times, serif;
	
}
.footer1 h2{margin: 5px;
	padding: 5px;
	border-bottom: 1px solid white;
	
	
}

</style>