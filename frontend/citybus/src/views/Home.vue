<template>

  <!-- first section -->

  <div class="container">
    <div class="row">
      <div class="col-md-6 col-lg-6 my-5 ">
        <h1 class="display-2">Sohochor</h1>
        <h3 class="display-5 muted">Make your journey safe with us</h3>
        <button class="btn btn-primary">Checkout available route</button>
      </div>

      <!-- animation -->
      <!-- <div class="col-md-6 col-lg-6 my-3 center">
        <lottie-player src="https://assets4.lottiefiles.com/packages/lf20_BBOVEK.json"  background="transparent"  speed="1"  style="width: 350px;"  loop  autoplay></lottie-player>
      </div> -->
    </div>
  </div>

  <!-- ticket-section -->

  <section class="bg-light" @click="hide_model">
    <div class="container bg-light">
    <div class="row">
      <h1 class="display-4 text-center my-4">Purchase your ticket</h1>
      <!-- <h2>{{pickup}}</h2> -->
      <div class="col-lg-5">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Pickup Point</label>
            <input v-model="pickup" @focus="form" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div v-if="model">
              <ul  class="list-group" v-for="name in pick_obj" :key="name.id">
                <li class="list-group-item" @click="set_location(name.name_of_route)">{{name.name_of_route}}</li>
              
              </ul>
            </div>
            
            
          </div>
        </form>

      </div>

      <!-- end -->
      <div class="col-lg-5">
        <label for="exampleInputEmail1" class="form-label">Destination</label>
        <select class="form-select" id="exampleInputEmail1" aria-label="Default select example">
        <option selected>Select</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
        </select>
        

      </div>
      <div class="col-lg-2 button-top">
        <button type="button" class="btn btn-primary">Search</button>

      </div>
      
      
      
    </div>
  </div>
  </section>

  <!-- ticket-section-end -->
  
    



  
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'Home',
  

  data(){
    return{
      pickup:'',
      pick_obj:[],
      model:false
    }
  },
  watch:{
    pickup: function(value){
      const data = {
        pickup:value
      }
      axios.post('api/route_search/',data)
      .then(res => {
        console.log(res.data['data'])
        this.pick_obj = res.data['data']
      })
      .then(err => {
        console.log(err)
      })
    }
  },
  methods:{
    set_location(value){
      this.pickup = value
      this.model = false


    },
    form(){
      this.model= true
      
    }
  }
  
}
</script>
<style>
.display-2{
  font-weight: 600;
}

.center{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}

.form-label{
  font-weight: 900;
}
.display-4{
  font-weight: 400;
}

.button-top{
  margin-top: 2.2rem;
}

li { cursor: pointer; }
</style>