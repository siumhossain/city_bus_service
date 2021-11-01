<template>

<!-- Navbar -->
<nav class="navbar navbar-expand-lg navbar-light shadow-1">
  <div class="container">
    <a class="navbar-brand text-Purple50" href="#">Sohochor</a>
    <button
      class="navbar-toggler"
      type="button"
      data-mdb-toggle="collapse"
      data-mdb-target="#navbarNav"
      aria-controls="navbarNav"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <i class="fas fa-bars"></i>
    </button>
    <div class="collapse navbar-collapse" id="navbarButtonsExample">
      <!-- Left links -->
      
      <!-- Left links -->

      <div class="d-flex align-items-center ms-auto">
        
        <div class="px-2 me-1">
          <router-link to='/about'>About</router-link>
        </div>

        <div class="px-2 me-3">
          <router-link to='/login'>Login</router-link>
        </div>
        
        
        <a
          class="btn btn-dark px-3"
          href="https://github.com/mdbootstrap/mdb-ui-kit"
          role="button"
          ><i class="fab fa-github"></i
        ></a>
      </div>
    </div>
  </div>
</nav>
<!-- Navbar -->

  
  
  
          
  <router-view/>
</template>

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
