<template>
  <div class="SNS">
    <section class="blog-post-area">
      <div>
        <img src="img/snsmain.png" style="width:100%;">
    </div>
      <div class ="container">
        <div class = "row" v-if="loggedInUser">
          <div class="col-lg-8" style="margin-top:60px; font-family: 'Jua', sans-serif;">
            <Com_Sns_Right/>
            <Com_Sns_Left/>
          </div>
          <div class="col-lg-4 sidebar-widgets" style="margin-top:108px;">
            <Com_Sns_Rank/>
          </div>
        </div>
        <div v-else>
          <div class="card text-center" style="height:375px; border:none; font-family:'Jua', sans-serif;">
            <div class="card-body">
              <span>
                <img src="img/logo.png" alt="" style="width: 50%;">
              </span>
              <h2 class="card-title">로그인 후 이용해주세요</h2>
                <router-link to="/login" style="margin:6px">
                <button class="login100-form-btn" style="font-family:'Jua', sans-serif; font-size:27px">
                     로그인
                </button>
                </router-link>
                <router-link to="/signup" style="margin:6px;">
                  <button class="login100-form-btn" style="font-family:'Jua', sans-serif; font-size:27px">
                      회원가입
                  </button>
                </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Com_Sns_Left from '@/components/Com_Sns_Left.vue'
import Com_Sns_Right from '@/components/Com_Sns_Right.vue'
import Com_Sns_Rank from '@/components/Com_Sns_Rank.vue'

export default {
  name: 'SNS',
  components: {
    Com_Sns_Left,
    Com_Sns_Right,
    Com_Sns_Rank,
  },
  computed:{
    loggedInUser() {
      return this.$store.getters.loggedInUser;
    },
  }
}
</script>