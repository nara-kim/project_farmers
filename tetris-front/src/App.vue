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
              <!-- <li class="nav-item"><router-link to="/"><a class="nav-link">Weather</a></router-link></li> -->
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->
              <li class="nav-item"><router-link to="/sns"><a class="nav-link">Sns</a></router-link></li>
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->

              <!-- <li class="nav-item"><a class="nav-link">Category</a>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Pages</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="blog-details.html">Blog Details</a></li>
                </ul>
              </li>
              <li class="nav-item"><router-link to = "/board"><a class="nav-link">Board</a></router-link></li>             -->
              <!-- <li class="nav-item"><a class ="nav-link"> | </a></li> -->

            </ul>
            <ul v-if="isAuthenticated" class="nav navbar-nav navbar-right navbar-social" style="width : 220px" >
            <li class ="nav-item"><router-link to ="mypage"><a class="nav-link" style="font-size:large">{{userName}}</a></router-link></li>
              <li class="nav-item"><a class="nav-link" style="font-size:large" @click.prevent="logout">로그아웃</a></li>
            </ul>
             <ul v-else class="nav navbar-nav navbar-right navbar-social" style="width : 220px">
              <li class ="nav-item"><router-link to="/login"><a class="nav-link" style="font-size:large;">로그인</a></router-link></li>
              <li class="nav-item"><router-link to="/signup"><a class="nav-link" style="font-size:large">회원가입</a></router-link></li>
            </ul> 
          </div> 
        </div>
      </nav>
    </div>
  </header> 
    </div>
    <router-view/>
    <!-- footer -->
     
    <footer class="container-fluid text-center bg-lightgray" style="height:100px;background-color:black">

        <div class="copyrights" style="margin-top:25px;">
          <img src="img/logo.png" style="width:10%; float:left">
          <!-- <p><a href="https://www.linkedin.com/in/michael-clark-webdeveloper" target="_blank">
            <i class="fa fa-linkedin-square" aria-hidden="true"></i></a></p> -->
            <p style="color:black">dfd</p>
            <p>Farmers © 2020, Samsung Software Academy For Youth
              <a href="#" style="float:right"><img src="img/icon2.png" style="width:30px;"></a>
            </p>
                <!-- <span>Samsung Software Academy For Youth</span></p> -->
            
        </div>
</footer>
<!-- Footer -->
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
@import url(http://netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.css);
.bg-lightgray
{
    background-color:LightGray;
}
</style>

    <!-- footer end -->

