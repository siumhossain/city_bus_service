<template >
    <div class="container">
        <div class="row">
            <div class="row mt-4 mb-2 text-center">
                <h3 class="display-5">Your purchased ticket history</h3>
            </div>

        </div>
    </div>    

    <div class="container">   
        <div class="row">
            
            <table class="table mx-2 mt-3 mb-5">
            <thead>
                <tr>
                <th scope="col">Bus name</th>
                <th scope="col">Pickup point</th>
                <th scope="col">Destination</th>
                <th scope="col">Time</th>
                <th scope="col">Cancel</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="ticket in ticket_obj" :key="ticket.id">
                    <th>
                        <span class="mt-2 mx-2">
                            <i class="fas fa-bus-alt"></i>
                        </span>
                        <b>{{ticket.busname}}</b>
                    </th>
                    <th>{{ticket.pickup}}</th>
                    <th>{{ticket.destination}}</th>
                    <th>{{ticket.time}}</th>
                    <th>
                        <button @click="cancel(ticket.id,ticket.time)" class="btn btn-primary">Cancel</button>
                    </th>
                </tr>
                
            </tbody>
            </table>
            
        </div>
    </div>
</template>
<script>
import axios from 'axios'
export default {

    data(){
        return{
            ticket_obj:{}
        }
    },

    async mounted() {
        const id = this.$store.state.user.id
        await axios.get(`api/single_ticket/${id}`)
        .then(res => {
            console.log(res.data)
            this.ticket_obj = res.data['data']
        })
    },
    methods:{
        async cancel(id,time){
            console.log(id,time)
            //console.log(this.ticket_obj)
            const data = {
                id:id,
                time:time
            }
            //console.log(data['id'])
            await axios.put('/api/ticket/',data)
            .then(res => {
                console.log(res)
                const id = this.$store.state.user.id
                axios.get(`api/single_ticket/${id}`)
                .then(res => {
                    this.ticket_obj = res.data['data']

                })
                
            })
            //console.log(data)
        }
    }
}
</script>
<style >
    
</style>