<template>

<!-- Navbar -->
  <nav class="navbar navbar-expand-md navbar-light mx-2 px-2">
    <div class="container">
      <!-- navbar brand / title -->
      <a class="navbar-brand" href="#intro">
        <span class=" fw-bold">
          Sohochor
        </span>
      </a>
      <!-- toggle button for mobile nav -->
      <button
      class="navbar-toggler"
      type="button"
      data-mdb-toggle="collapse"
      data-mdb-target="#main-nav"
      aria-controls="main-nav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <i class="fas fa-bars"></i>
    </button>

      <!-- navbar links -->
      <div class="collapse navbar-collapse justify-content-end align-center" id="main-nav">
        <ul class="navbar-nav">
          <li class="nav-item px-2 me-1 py-2">
            <b>Hi! {{$store.state.user.username}}</b> 
          </li>
          <li class="nav-item px-2 me-1 py-2">
            <router-link to='/about'>About</router-link>
          </li>
          <li v-if='this.$store.state.user === null' class="nav-item px-2 me-1 py-2">
            <router-link to='/login'>Login</router-link>
          </li>

          <li v-else class="nav-item px-2 me-1 py-2">
            logout
          </li>
          
          
        </ul>
      </div>
    </div>
  </nav>
<!-- Navbar -->

  
  
  
          
  <router-view/>
</template>

<script>
import axios from 'axios'
export default {
  async beforeCreate(){
    await axios.get('api/auth/users/me/')
    .then(res => {
      this.$store.dispatch('user',res.data)

    })
    .then(err =>{
      console.log(err)
    })
  }
}
</script>

<style>

.navbar-brand{
  font-size: 1.5rem;
  font-weight: 900;
  
}

.navbar{
  background-color:  #F6F5F5;
}

body{
  background-color: #FEFBF3;
}




</style>
