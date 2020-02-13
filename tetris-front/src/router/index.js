import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Sns from '../views/Sns.vue'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import Board from '../views/Board.vue'
import Detail_Sns from '../views/Detail_Sns.vue'
import Sns_Write from '../views/Sns_Write.vue'
import View_Board_Write from '../views/View_Board_Write.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/sns',
    name: 'sns',
    component: Sns
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path : '/board',
    name : 'board',
    component:Board
  },
  {
    path: '/detail_sns',
    name: 'detail_sns',
    component: Detail_Sns
  },
  {
    path : '/sns_write',
    name:'sns_write',
    component: Sns_Write
  },
  {
    path : '/view_board_write',
    name:'view_board_write',
    component: View_Board_Write
  },
]

const router = new VueRouter({
  mode:'history',
  routes
})

export default router