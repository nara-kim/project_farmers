import axios from 'axios';

const state = {
    sns_list: [],
}

const mutations = {
    getSns(state){
        axios
          .get('http://127.0.0.1:8000/sns/todo/snslist/')
          .then(res => {
            console.log('서옹???')
  
            state.sns_list = res.data;
            // this.sns_list = res.data;
            console.log('성공한듯??!!했냐냐냐냐!!!ㄴ???')
          })
          .catch(err => console.log(err))
      },
}

const actions = {
    getSnsAction(options){
        options.commit('getSns')
    },
}

const getters = {
    snsgetters(state) {
        return state.sns_list;
    }
}

export default {
	state,
	mutations,
	actions,
	getters,
};
