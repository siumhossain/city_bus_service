<template>
    <div class="container">
        <div class="card" style="width: 30rem;">
        <div class="card-header my-3">
            <h2>Login</h2>
        </div>
        <div class="card-body">
            <form @submit.prevent="submit">
                <div class="mb-3">
                    <label for="exampleInputEmail1" class="form-label">Username</label>
                    <input type="text" v-model="username" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
                    <div id="emailHelp" class="form-text">We'll never share your email with anyone else.</div>
                </div>
                <div class="mb-3">
                    <label for="exampleInputPassword1" class="form-label">Password</label>
                    <input type="password" v-model="password" class="form-control" id="exampleInputPassword1">
                </div>
                <div class="mb-3 form-check">
                    <input type="checkbox" class="form-check-input" id="exampleCheck1">
                    <label class="form-check-label" for="exampleCheck1">Remeber me</label>

                </div>
                <div class="mb-3 ">
                    <span>Not a member? </span>
                    <router-link to='/register'>
                    Register
                    </router-link>

                </div>

                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
            
        </div>
    </div>
    </div>
    <router-view></router-view>
</template>
<script>
import axios from 'axios'
export default {
    name:'Login',

    data(){
        return{
            username:'',
            password:''
        }
    },
    methods:{
        async submit(){
            const formdata = {
                username:this.username,
                password:this.password
            }
            //console.log(formdata)
            delete  axios.defaults.headers.common["Authorization"];
            await axios.post('api/auth/token/login/',formdata)
            .then(res => {
                const token = res.data['auth_token']
                // this.$store.dispatch('user',res.data)
                localStorage.setItem('token',token)
                axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
                axios.get('api/auth/users/me/')
                .then(res => {
                    this.$store.dispatch('user',res.data)
                    //console.log(this.$store.state.user)
                    this.$router.push('/')
                })
                .then(err => {
                    console.log(err)
                })
                //console.log(this.$store.state.user.auth_token)
            })
            .then(err => {
                console.log(err)
            })
        }
    }
}
</script>
<style>
.container{
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    
}
.card{
    margin-top: 3rem;
} 
h2{
    font-weight: 900;
}
</style>