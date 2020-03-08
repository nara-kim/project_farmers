<template>
<div class="limiter">
      <div class="container-login100">
         <div class="wrap-login100 p-t-85 p-b-20">
            <form class="login100-form validate-form">
               <span class="login100-form-title p-b-70" style="text-align:center">
                  Welcome
               </span>
               <span class="login100-form-avatar">
                  <img src="img/loginlogo.png" alt="AVATAR">
               </span>

               <div class="wrap-input100 validate-input m-t-85 m-b-35" data-validate = "Enter username">
                  <span class="label-input100">ID</span>
                  <input class="input100" type="text" v-model="credential.username" required >
                  <span class="focus-input100"></span>
               </div>

               <div class="wrap-input100 validate-input m-b-50" data-validate="Enter password">
                  <span class="label-input100">비밀번호</span>
                  <input class="input100" type="password" v-model="credential.password" required >
                  <span class="focus-input100"></span>
               </div>

               <div class="container-login100-form-btn">
                  <button @click.prevent="login" class="login100-form-btn">
                     Login
                  </button>
               </div>

               <ul class="login-more p-t-190">
                  <li class="m-b-8">
                     <span class="txt1">
                        Forgot
                     </span>

                     <a href="#" class="txt2">
                        Username / Password?
                     </a>
                     
                  </li>

                  <li>
                     <span class="txt1">
                        Don’t have an account?
                     </span>

                     <router-link to = "/signup"><a class="txt2">
                        Sign up
                     </a></router-link>
                     
                  </li>
               </ul>
            </form>
         </div>
      </div>
   </div>
</template>
<script>
import axios from "axios";

export default {
    name: "LoginForm",
    data() {
        return {
            credential: {
                username: "",
                password: ""
            },
            testdata: {
                username: "seungue0001",
                password: "tmdrb0001"
            },
            errorMessage: ""
        };
    },
    methods: {
        login() {
            axios
                .post('http://localhost:8000/auth/accounts/login/', this.credential)
                .then(res => {
                    console.log(res.data.token)
                    const { token } = res.data;
                    console.log('1')
                    this.$session.set("mmr-token", token); // 세션에 저장
                    console.log('2')
                    this.$store.dispatch("setTokenAction", token); // vuex token에 저장
                    console.log("3")
                    this.$router.push("/"); // 홈에 보내기
                    console.log('로그인 끝!!!')
                })
                .catch(() => {
                this.loginAlert();
                });
         },
        loginAlert() {
        this.errorMessage =
            "아이디 또는 비밀번호가 올바르지 않습니다. / 한영키를 확인해주세요.";
        },
        onUsername(e) {
        this.credential.username = e.target.value;
        },
        onPassword(e) {
        this.credential.password = e.target.value;
        }
    }
}

</script>

<style scoped>

</style>