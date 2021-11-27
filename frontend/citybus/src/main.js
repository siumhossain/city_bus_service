import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'



axios.defaults.baseURL  =  "https://shy-dodo-23.loca.lt/"

axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
createApp(App).use(store).use(router,axios).mount('#app')
