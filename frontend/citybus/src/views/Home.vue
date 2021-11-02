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

  <section class="bg-light">
    <div class="container bg-light">
    <div class="row">
      <h1 class="display-4 text-center my-4">Purchase your ticket</h1>
      <!-- <h2>{{pickup}}</h2> -->
      <span v-if='this.$store.state.user === null' class="info my-3 text-center">
        <i class="fas fa-info-circle"></i>
        <b> You have to be logged in or registered for purchasing ticket</b>
      </span>
      
      <div class="col-lg-4">
        <form>
          <div class="mb-3">
            <label for="exampleInputEmail1" class="form-label">Pickup Point</label>
            <input v-model="pickup" @focus="form" type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp">
            <div v-if="model">
              <ul  class="list-group" v-for="name in pick_obj" :key="name.id">
                <li class="list-group-item" @click="set_location(name)">{{name.name_of_route}}</li>
              
              </ul>
            </div>
            
            
          </div>
        </form>

      </div>

      <!-- end -->

      <!-- destination -->
      <div class="col-lg-4">
        <label for="exampleInputEmail1" class="form-label">Destination</label>
        <select class="form-select" id="exampleInputEmail1" aria-label="Default select example">
        <option selected>Select</option>
        <option v-for="des in destinantion" :key="des.id" value="{{des.name_of_route}}">{{des.name_of_route}}</option>
        
        </select>
        

      </div>
      <!-- end -->

      <!-- time -->
      <div class="col-lg-2">
        <label for="exampleInputEmail1" class="form-label">Time</label>
        <select class="form-select" id="exampleInputEmail1" aria-label="Default select example">
        <option selected>Select</option>
        <option v-for="name in pick_obj" :key="name.id" value="{{name.time}}">{{name.time}}</option>
        
        </select>

      </div>

      <!-- end -->

      <div class="col-lg-1 button-top">
        <button v-if='this.$store.state.user !== null' type="button" class="btn btn-primary">Confirm</button>
        
        <button
          disabled
          v-else
          type="button"
          class="btn btn-primary"
        >
          Confirm
        </button>
       
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
      destinantion:[],
      
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
    async set_location(value){
      this.pickup = value.name_of_route
      this.model = false
      
      console.log(value.bus_id,value.trip_number,value.station_serial)
      const data = {
        bus_id : value.bus_id,
        serial_number: value.station_serial,
        trip_number : value.trip_number
      }
      await axios.post('api/route_search_destination/',data)
      .then(res => {
        console.log(res.data['data'])
        this.destinantion = res.data['data']
      })
      .catch(err => {
        console.log(err)
      })


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

.info{
  color:crimson
}
</style>