<template>

  <!-- first section -->

  <div class="container">
    <div class="row">
      <div class="col-md-6 col-lg-6 my-5 ">
        <h1 class="display-2">Sohochor</h1>
        <h3 class="display-5 muted">Make your journey safe with us</h3>

        <router-link to="/routes">
          <button class="btn btn-primary">Checkout our pickup point</button>
        </router-link>
        
      </div>

      <!-- animation -->
      <!-- <div class="col-md-6 col-lg-6 my-3 center">
        <lottie-player src="https://assets4.lottiefiles.com/packages/lf20_BBOVEK.json"  background="transparent"  speed="1"  style="width: 350px;"  loop  autoplay></lottie-player>
      </div> -->
    </div>
  </div>

  <!-- ticket-section -->

  
  <section class="bg-light">
    <div class="container">
    <div class="row">
      <h1 class="display-4 text-center my-4">Purchase your ticket</h1>
      <!-- <h2>{{pickup}}</h2> -->
      <span v-if='this.$store.state.user === null' class="info my-3 text-center">
        <i class="fas fa-info-circle"></i>
        <b> You have to be logged in or registered for purchasing ticket</b>
      </span>
      
        <div class="row for-form">
          <div class="col-lg-8">
            <form class="mx-3 px-3">
          <div class="form-group row mb-3">
            
            <input v-model="pickup" @focus="form" type="text" class="form-control " id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="⌨ Type your location">
            <div v-if="model">
              <ul  class="list-group" v-for="name in pick_obj" :key="name.id">
                <li class="list-group-item" @click="set_location(name)">{{name.name_of_route}}</li>
              
              </ul>
            </div>
            
            
          </div>
        </form>

          </div>
        </div>
        <div class="row for-form">
          <div class="col-lg-10">
            <table v-if='table' class="table align-middle">
              <thead>
                <tr>
                  <th scope="col">Bus</th>
                  <th scope="col">Destination</th>
                  <th scope="col">Time</th>
                  <th scope="col">Confirm</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="des in destination" :key="des.id">
                  
                  <td>
                    <span class="mt-2 mx-2">
                      <i class="fas fa-bus-alt"></i>
                    </span>
                    <b>{{des.name_of_bus}}</b>
                  </td>
                  <td>
                    <span class="mt-2 mx-2">
                            <i class="fas fa-map-marker-alt"></i>
                    </span>
                    <b>{{des.name_of_route}}</b>
                  </td>
                  <td>
                    <span class="mt-2 mx-2">
                      <i class="fas fa-clock"></i>
                    </span>
                    <b>{{des.time}}</b>
                    
                  </td>
                  <td>
                    <button v-if='$store.state.user !== null' class="btn btn-primary">
                      Confirm
                    </button>
                    <button v-else class="btn btn-primary" disabled>
                      Confirm
                    </button>

                  </td>
                  
                  
                </tr>
                
                
              </tbody>
            </table>

          </div>
        </div>
        

      </div>

      <!-- end -->

      <!-- destination -->
      
      
      
      
      
    
  </div>
  </section>



  

  <!-- ticket-section-end -->
  
    
  <router-view></router-view>


  
</template>

<script>
// @ is an alias to /src
import axios from 'axios';

export default {
  name: 'Home',
  

  data(){
    return{
      pickup:'',
      table:false,
      pick_obj:[],
      destination:{},
      
      
      
      model:false
    }
  },
  watch:{
    pickup: function(value){
      const data = {
        pickup:value
      }
      delete  axios.defaults.headers.common["Authorization"];
      axios.post('api/route_search/',data)
      .then(res => {
        
        this.pick_obj = res.data['data']
        this.table = true
        axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
      })
      .then(err => {
        console.log(err)
      })
    },
    
  },
  methods:{
    async set_location(value){
      this.pickup = value.name_of_route
      this.model = false
      
      delete  axios.defaults.headers.common["Authorization"];
      const data = {
        bus_id : value.bus_id,
        serial_number: value.station_serial,
        trip_number : value.trip_number
      }
      await axios.post('api/route_search_destination/',data)
      .then(res => {
        
        console.log(res.data['data'])

        this.destination = res.data['data']
        console.log(this.destination)
        axios.defaults.headers.common['Authorization'] =  "Token "  +  localStorage.getItem('token')
      })
      .catch(err => {
        console.log(err)
      })


    },
    
    form(){
      this.model= true
      
    },
    submit(){
      console.log('click')
      
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
.point{
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
}
.for-form{
  display: flex;
  flex-direction: column;
  align-items: center;
  
}
</style>