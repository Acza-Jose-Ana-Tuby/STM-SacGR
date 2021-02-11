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
                    <button class="btn btn-success" style="width: 15%" @click="createSchedule()">Adicionar Horário</button>
                </p>
            </div><br><br>
           <Calendario
            :doctorID='id'
            ref = "Calendario"
           > </Calendario>
           <p class="note"> 
                A faixa de horários preenchida em cinza representa o turno de atendimento ao Grupo de Risco.
            </p>
           <br>
        </div>
    </div>
</template>

<script>
import httpRequests from '../http-requests'
import Calendario from './Calendario'
import moment from 'moment'
export default {
    created() {
        this.readSchedules()
        this.readSchedulingPolicy()
    },
    components: {
        Calendario
    },
    watch: {
        date: function(newValue, oldValue) {
            this.readAllDaySchedules()
        },
        time: function(newValue, oldValue) {
            this.checkInterval()
        }
    },
    data() {
        return {
            date: '',
            time: '',
            duration: '',
            id: parseInt(this.$route.params.id),
            schedules: [],
            allDaySchedules: [],
            interval: '',
            schedulingPolicies: []
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
        readSchedulingPolicy() {
            httpRequests.readAll('politica_agendamento')
                .then(response => {
                    this.schedulingPolicies = response.data.objects[0]
                })
        },
        readAllDaySchedules() {
            this.allDaySchedules = []
            httpRequests.readAll('agenda_medica')
                .then(response => {
                    for (let schedule of response.data.objects) {
                        if (schedule.AgdMed_Dia == this.date) {
                            this.allDaySchedules.push(schedule)
                        }
                    }
                })
        },
        checkInterval () {
            if (moment(this.time, 'HH:mm').isBefore(moment('12:01', 'HH:mm'))) {
                this.interval = 'Manhã' 
            } else {
                this.interval = 'Tarde'
            }
        },
        checkCapacity () {
            let capacity
            let counter = 0

            if (this.interval == this.schedulingPolicies.PltAgd_Turno_Grupo_Risco) {
                capacity = this.schedulingPolicies.PltAgd_Capacidade_Grupo_Risco
            } else {
                capacity = this.schedulingPolicies.PltAgd_Capacidade_Regular
            }
            
            for (let schedule of this.allDaySchedules) {

                let startTime = schedule.AgdMed_Hora_Inicio
                let endTime = moment(schedule.AgdMed_Hora_Inicio, 'HH:mm').add(parseInt(schedule.AgdMed_Duracao), 'minutes').format('HH:mm')

                while (startTime.toString() != endTime.toString()) {
                    if (startTime == this.time) {
                        counter++
                        break
                    }
                    startTime = moment(startTime, 'HH:mm').add(1, 'minutes').format('HH:mm')

                }

                 if (counter == capacity) {
                    alert ('Não é possível agendar consulta nesse horário. Capacidade cheia')
                    return -1
                }
            
            }
        },
        createSchedule() {
            if (!this.date || !this.time || !this.duration) {
                return
            }
            if (this.checkCapacity() == -1 ) {
                this.date = ''
                this.time = ''
                this.duration = ''
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
.note {
    font-size: 0.75em; 
    color: red;
}
</style>