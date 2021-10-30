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
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav ms-auto">
        <li class="nav-item">
          <router-link to="/about">About</router-link>
        </li>
        
      </ul>
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
