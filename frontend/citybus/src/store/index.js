import { createStore } from 'vuex'

export default createStore({
  state: {
    user:null,
  },
  
  actions: {
    user(context,user){
      context.commit('user',user)
    }

  },

  mutations: {
    user(state,user){
      state.user = user
    }
  },
  
})
