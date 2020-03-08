<template>
    <div class="limiter" style=" font-family: 'Jua', sans-serif;" >
      <div class="container-login100" >
         <!-- <div class="login100-more" style="background-image: url('images/bg-01.jpg');"></div> -->

         <div class="wrap-login100 p-l-50 p-r-50 p-t-72 p-b-50" style=" font-family: 'Jua', sans-serif;">
            <form class="login100-form validate-form">
               <span class="login100-form-title p-b-59" >
                  회원가입
               </span>

               <div class="wrap-input100 validate-input" data-validate="Name is required">
                  <span class="label-input100">아이디</span>
                  <input class="input100" type="text" name="name" placeholder="Name..."  maxlength="10" v-model="credential.username" required >
                  <small v-if="error.username">{{ error.userid }}</small>
                  <span class="focus-input100"></span>
               </div>

               <div class="wrap-input100 validate-input" data-validate = "Valid email is required: ex@abc.xyz">
                  <span class="label-input100">이메일</span>
                  <input class="input100" type="text" name="email" placeholder="Email addess..." v-model="credential.email" required >
                  <span class="focus-input100"></span>
               </div>

               <div class="wrap-input100 validate-input" data-validate="Username is required">
                  <span class="label-input100">닉네임</span>
                  <input class="input100" type="text" name="username" placeholder="Username..." maxlength="7" v-model="credential.nickname">
                  <span class="focus-input100"></span>
               </div>

               <div class="wrap-input100 validate-input" data-validate = "Password is required">
                  <span class="label-input100">비밀번호</span>
                  <input class="input100" type="password" name="pass" placeholder="*************" maxlength="15" v-model="credential.password" required >
                  <small v-if="error.password">{{ error.password }}</small>
                  <span class="focus-input100"></span>
               </div>

               <div class="wrap-input100 validate-input" data-validate = "Repeat Password is required">
                  <span class="label-input100">비밀번호확인</span>
                  <input class="input100" type="password" name="repeat-pass" placeholder="*************" maxlength="15" v-model="credential.passwordConfirm" required >
                  <small v-if="error.passwordConfirm">{{ error.passwordConfirm }}</small>
                  <span class="focus-input100"></span>
               </div>

               <div class="container-login100-form-btn">
                  <div class="wrap-login100-form-btn">
                     <div class="login100-form-bgbtn"></div>
                     <!-- <button @click.prevent="signup" class="login100-form-btn">
                        Sign Up
                     </button> -->
                    <button @click.prevent="signup" class="login100-form-btn">
                     회원가입완료
                  </button>
                  </div>
                  
                  <router-link to = "/login"><a class="dis-block txt3 hov1 p-r-30 p-t-10 p-b-10 p-l-30">
                     Sign in
                     <i class="fa fa-long-arrow-right m-l-5"></i>
                  </a></router-link>
               </div>
            </form>
         </div>
      </div>
   </div>
</template>
<script>
import axios from "axios";
export default {
    name: "SignupForm",
    data() {
        return {
            credential: {
               email:"",
               nickname:"",
               username: "",
               password: "",
               passwordConfirm: "",
            },
            testdata:{
               username: "seungue0004",
               password: "tmdrb0004",
               passwordConfirm: "tmdrb0004",
            },
            error: {
                username: "",
                password: "",
                passwordConfirm: "",
            }
        }
    },
    methods: {
        validation() {
            if (this.credential.password !== this.credential.passwordConfirm) {
                this.error.passwordConfirm = "비밀번호가 동일하지 않습니다.";
                return false;
            }
            return true;
        },
        signup() {
            this.error = {
                username: "",
                password: "",
                passwordConfirm: "",
            };
            if (this.validation()) {
                axios
                    .post('http://15.165.77.204:8000/auth/accounts/signup/', this.credential)
                    .then(res => {
                        // 로그인 시키고 홈으로.
                        const { token } = res.data;
                        this.$session.set("mmr-token", token);
                        this.$store.dispatch("setTokenAction", token);
                        this.$router.push("/");
                    })
                    .catch(err => {
                        const { data } = err.response;
                        for (let key in data) {
                            if (data.hasOwnProperty(key)) {
                                this.error[key] = data[key][0];
                            }
                        }
                    });
            }
        },
        onUsername(e) {
            this.credential.username = e.target.value;
        },
        onPassword(e) {
            this.credential.password = e.target.value;
        },
        onPasswordConfirm(e) {
            this.credential.passwordConfirm = e.target.value;
        }
    }
};
</script>

<style>

</style>