<template>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header bg-dark'>
                <h3>Agendar Consultas</h3>
            </div>
            <br>
            <label><b> Selecione o Paciente: </b></label>
            <input type="text" name="patient" list="patientname" v-model="selectedPatient"> 
                <datalist id="patientname">
                    <option v-for="(patient, index) in patients" :key="index">{{patient.Pct_Nome}}</option>
                </datalist>

            <label><b> Selecione a Especialidade: </b></label>
            <input type="text" name="specialization" list="specializationname" v-model="selectedSpecialization"> 
                <datalist id="specializationname">
                    <option v-for="(specialization, index) in specializations" :key=index>{{specialization}}</option>
            </datalist>

            <label><b> Selecione o Médico </b></label>
            <p v-for="(filteredDoctor, index) in filteredDoctors" :key="index"> 
                <button class="btn" @click="showSelectedDoctorSchedules(filteredDoctor.Med_ID)">{{filteredDoctor.Med_Nome}}</button>
            </p>

            <Calendario
                ref = "Calendario"
                v-if = "showCalendar"
                :doctorID = "selectedDoctorID"
                @doctorScheduleID = "selectedScheduleID = $event"
            >
            </Calendario><br>

            <p> <b> Dia: </b> {{formatedDay}} </p>
            <p> <b> Hora: </b> {{selectedSchedule.AgdMed_Hora_Inicio}} </p>
            
            <label><b>Selecione o modo de atendimento: </b></label>
            <p> Presencial &nbsp;&nbsp; <input @click="appointmentMode = 'Presen'" name="appointmentMode" type="radio"> </p>
            <p> Remoto <input @click="appointmentMode = 'Remoto'" name="appointmentMode" type="radio"> </p>
    
            <label><b>Selecione a forma de pagamento: </b></label>
            <p> Plano de Saúde <input @click="paymentForm = 'Plano'" name="paymentForm" type="radio"> </p>
            <p> Boleto Bancário <input @click="paymentForm = 'Boleto'" name="paymentForm" type="radio"> </p>
            <p> Cartão de Crédito <input @click="paymentForm = 'Cartão'" name="paymentForm" type="radio"> </p><br>
            
            <p>
                <button class="btn btn-success" style="width: 15%;" @click="markAppointment()">Marcar Consulta</button>
            </p>

            <br>
            <p v-show="showIncompleteAlert" style="text-align: center;">
                <span class="alert alert-warning">Preencha todos os campos para prosseguir.</span><br>
            </p>
            <p v-show="showCreatedAlert" style="text-align: center;">
                <span class="alert alert-success">Consulta Agendada com Sucesso!</span><br>
            </p>
            <br>
        </div>
    </div>
</template>

<script>
import moment from 'moment'
import httpRequests from '../http-requests'
import Calendario from './Calendario'
export default {
    components: {
        Calendario
    },
    created() {
        this.readPatients()
        this.readDoctors()
    },
    watch: {
        selectedSpecialization: function(oldValue, newValue) {
            this.filteredDoctors = []
            return this.filterDoctors()
        },
        selectedScheduleID: function(oldValue, newValue) {
            this.showSelectedSchedule()
        }
    },
    data() {
        return {
            patients: [],
            doctors: [],
            specializations: [],
            selectedPatient: '',
            selectedSpecialization: '',
            filteredDoctors: [],
            selectedDoctorID: '',
            showCalendar: false,
            selectedScheduleID: '',
            selectedSchedule: '',
            appointmentMode: '',
            paymentForm: '',
            showIncompleteAlert: '',
            showCreatedAlert: '',
            formatedDay: ''
        }
    }, 
    methods: {
        readPatients () {
            httpRequests.readAll('paciente')
                .then(
                    response => (
                        this.patients = response.data.objects
                    )
                )
        },
        readDoctors() {
            httpRequests.readAll('medico')
                .then(
                    response => (
                        this.doctors = response.data.objects,
                        this.defineSpecializations()
                    )
                )
        },
        defineSpecializations() {
            for (let doctor of this.doctors) {
                this.specializations.push(doctor.Med_Especialidade)
            }
            this.specializations = this.specializations.filter((item, i) => this.specializations.indexOf(item) === i)
        },
        filterDoctors() {
            for (let doctor of this.doctors) {
                if (doctor.Med_Especialidade === this.selectedSpecialization) {
                    this.filteredDoctors.push(doctor)
                }
            }
        },
        showSelectedDoctorSchedules(id) {
            this.selectedDoctorID = id
            this.showCalendar = true
            this.$refs.Calendario.readDoctorSchedules()
        },
        showSelectedSchedule() {
            httpRequests.read('agenda_medica', this.selectedScheduleID)
                .then(
                    response => (
                        this.selectedSchedule = response.data,
                        this.formatedDay = moment(response.data.AgdMed_Dia).format('DD/MM/YYYY')
                    )
                )
        },
        markAppointment() {
            httpRequests.create('consulta', {
                'Cons_Data': this.selectedSchedule.AgdMed_Dia,
                'Cons_Horario': this.selectedSchedule.AgdMed_Hora_Inicio,
                'Cons_Med_ID': this.selectedDoctorID, 
                'Cons_Tipo': this.appointmentMode,
                'Cons_Descricao': 'aaaa',
                'Cons_Pagamento': this.paymentForm,
                'Cons_Pct_ID': 2
            }).then( () => {
                this.$router.push('/Login')
                this.selectedPatient = ''
                this.selectedSpecialization = ''
                this.filteredDoctors = []
                this.selectedSchedule = ''
                this.appointmentMode = ''
                this.paymentForm = ''
                this.showCreatedAlert = true
            } )
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

p, label {
    text-align: center;
}

input[type="text"]{
    width: 50%;
    margin: auto;
}

</style>