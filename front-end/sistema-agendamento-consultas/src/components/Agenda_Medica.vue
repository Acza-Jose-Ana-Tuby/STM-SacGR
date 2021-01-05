<template>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header bg-dark'>
                <h3>Agenda Médica</h3>
            </div>
            <br>
            <div class="card" style="width: 70%; margin: 0 auto;"> 
                <h4> Cadatrar novo Horário </h4><br>
                <p> Dia: <input type="date" v-model="date"> </p>
                <p> Hora: <input type="time" v-model="time"> </p>
                <p> Duração: <input type="number" min="5" max="60" step="5" v-model="duration"> minutos </p><br>
                <p>
                    <button class="btn btn-success" style="width: 15%" @click="createSchedule">Adicionar Horário</button>
                </p>
            </div><br><br>
           <Calendario
            :doctorID='id'
            ref = "Calendario"
           > </Calendario>
           <br>
        </div>
    </div>
</template>

<script>
import httpRequests from '../http-requests'
import Calendario from './Calendario'
export default {
    created() {
        this.readSchedules()
    },
    components: {
        Calendario
    },
    data() {
        return {
            date: '',
            time: '',
            duration: '',
            id: this.$route.params.id,
            schedules: []
        }
    },
    methods: {
        readSchedules(){
            httpRequests.readAll('agenda_medica')
                .then(response => {
                    for (let schedule of response.data.objects) {
                        if (schedule.AgdMed_Med_ID == this.id) {
                            this.schedules.push(schedule)
                        }
                    }
                })
        },
        createSchedule() {
            if (!this.date || !this.time || !this.duration) {
                return
            }
            httpRequests.create('agenda_medica', {
                'AgdMed_Marcado': 0,
                'AgdMed_Dia': this.date,
                'AgdMed_Hora_Inicio': this.time, 
                'AgdMed_Duracao': this.duration, 
                'AgdMed_Med_ID': this.id,
            }).then(() => {
                this.date = ''
                this.time = ''
                this.duration = ''
                this.$refs.Calendario.readDoctorSchedules()
            })
        }
    }
}
</script>

<style>
body, html {
  padding: 0;
  margin: 0;
  width: 100%;
  min-height: 100vh;
  background-color: #dee9ff;
}
</style>

<style scoped>
h3 {
    color: white;
    text-align: center;
}
hr { 
  border-style: solid;
  border-width: 2px;
} 
input {
    width: 20%
}
p, h4 {
    text-align: center;
}
</style>