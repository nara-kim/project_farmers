<template>
  <div id="app">
    <div class ="farmerslogo" style="text-align:center">
    </div>
    <div id="nav">
      <header class="header_area">
        <div class="main_menu">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container box_1620">
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span> 
          </button>
          <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
            <ul class="nav navbar-nav menu_nav justify-content-left">
              <li class="nav-item"><router-link to="/"><a class="nav-link">메인</a></router-link></li>
              <li class="nav-item"><router-link to="/sns"><a class="nav-link">오늘의땀</a></router-link></li>
              <li class="nav-item"><router-link to = "/board"><a class="nav-link">일손</a></router-link></li>            

            </ul>
            <router-link to = "/"><img class="d-none d-sm-block" id="logoimg" src="img/logo.png" style="margin-right:200px;"></router-link>

            <ul v-if="isAuthenticated" class="nav navbar-nav navbar-right navbar-social" style="width : 600px;float:left;" >
              <li class ="nav-item"><a class="nav-link" style="font-size:medium" @click="mypage(userId)">{{userName}}</a></li>
              <li class="nav-item"><a class="nav-link" style="font-size:medium; padding-left:15px;" @click.prevent="logout">로그아웃</a></li>
            </ul>
             <ul v-else class="nav navbar-nav navbar-right navbar-social" style="width : 600px;float:left;">
              <li class ="nav-item"><router-link to="/login"><a class="nav-link" style="font-size:medium;">로그인</a></router-link></li>
              <li class="nav-item"><router-link to="/signup"><a class="nav-link" style="font-size:medium; padding-left:15px;">회원가입</a></router-link></li>
            </ul> 
          </div> 
        </div>
      </nav>
    </div>
  </header> 
    </div>
    <router-view/>
     
    <footer class="container-fluid text-center bg-lightgray" style="height:100px;background-color:black">
      
        <div class="copyrights" style="margin-top:25px;">
          <img src="img/logo.png" style="width:10%; float:left">
            <p style="color:black">dfd</p>
            <p>Farmers © 2020, Samsung Software Academy For Youth
              <a href="#" style="float:right"><img src="img/icon2.png" style="width:30px;"></a>
            </p>
            
        </div>
</footer>
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
    mypage(userId){
      this.$router.push(`/mypage/${userId}`)
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    userName() {
      return this.$store.getters.loggedInUser.username;
    },
    userId() {
    return this.$store.getters.loggedInUser.user_id;
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
#logoimg{
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
