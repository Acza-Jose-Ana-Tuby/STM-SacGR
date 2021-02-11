<template>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header bg-dark'>
                <h3>Agendar Consultas</h3>
            </div>
            <br>
            <label><b> Paciente: </b> {{patient.Pct_Nome}}</label>      

            <label><b> Selecione a Especialidade: </b></label>
            <input type="text" name="specialization" list="specializationname" v-model="selectedSpecialization"> 
                <datalist id="specializationname">
                    <option v-for="(specialization, index) in specializations" :key=index>{{specialization}}</option>
            </datalist>

            <label><b> Selecione o Médico: </b></label>
            <p v-for="(filteredDoctor, index) in filteredDoctors" :key="index"> 
                <button class="btn" @click="showSelectedDoctorSchedules(filteredDoctor.Med_ID)">{{filteredDoctor.Med_Nome}}</button>
            </p>

            <Calendario
                ref = "Calendario"
                v-if = "showCalendar"
                :doctorID = "selectedDoctorID"
                :riskGroupBelonging="parseInt(patient.Pct_Grupo_Risco)"
                @doctorScheduleID="selectedScheduleID = $event"
            >
            </Calendario><br>

            <p> <b> Dia: </b> {{formatedDay}} </p>
            <p> <b> Hora: </b> {{selectedSchedule.AgdMed_Hora_Inicio}} </p>
            
            <label><b>Selecione o modo de atendimento: </b></label>
            <select style="width: 30%; margin:auto;" v-model="appointmentMode">
                <option>Presencial</option>
                <option>Remoto</option>
            </select>

    
            <label><b>Selecione a forma de pagamento: </b></label>
            <select style="width: 30%; margin:auto;" v-model="paymentForm">
                <option>Plano de Saúde</option>
                <option>Boleto Bancário</option>
                <option>Cartão de Crédito</option>
            </select>
            <br>
            <br>

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
        this.id = this.$route.params.id
        this.readPatient()
        this.readDoctors()
    },
    watch: {
        selectedSpecialization: function(newValue, oldValue) {
            this.filteredDoctors = []
            return this.filterDoctors()
        },
        selectedScheduleID: function(newValue, oldValue) {
            this.showSelectedSchedule()
        }
    },
    data() {
        return {
            patient: '',
            doctors: [],
            specializations: [],
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
            formatedDay: '',
            id: this.$route.params.id,
            
        }
    }, 
    methods: {
        readPatient () {
            httpRequests.read('paciente', this.id)
                .then(
                    response => (
                        this.patient = response.data
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
        showSelectedDoctorSchedules(index) {
            this.selectedDoctorID = index
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
                'Cons_Descricao': 'aaaaa',
                'Cons_Pagamento': this.paymentForm,
                'Cons_Pct_ID': this.id
            }).then( () => {
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