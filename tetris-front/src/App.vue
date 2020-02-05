<template>
  <div id="app">
    <div id="nav">
      <header class="header_area">
    <div class="main_menu">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container box_1620">
          <!-- Brand and toggle get grouped for better mobile display -->
          <router-link to = "/"><a class="navbar-brand logo_h"><img class="logoimg" src="img/logo.png" alt=""></a></router-link>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <!-- Collect the nav links, forms, and other content for toggling -->
          <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
            <ul class="nav navbar-nav menu_nav justify-content-center">
              <li class="nav-item"><router-link to="/"><a class="nav-link">Home</a></router-link></li>
              <li class="nav-item"><router-link to="/"><a class="nav-link">Weather</a></router-link></li>
              <li class="nav-item"><router-link to="/sns"><a class="nav-link">Sns</a></router-link></li>
              <li class="nav-item"><a class="nav-link">Category</a>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Pages</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="blog-details.html">Blog Details</a></li>
                </ul>
              </li>
              <router-link to = "/board"><li class="nav-item"><a class="nav-link">Board</a></li></router-link>
            </ul>
             <ul class="nav navbar-nav navbar-right navbar-social" style="width : 180px">
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
  </div>
</template>

<script>

export default {
  methods: {
    logout() {
      this.$store.dispatch("logout");
      // this.$session.remove("mmr-token");
      this.$router.push("/login");
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
.logoimg{
  width: 200px;
  height: 65px;
}
</style>

