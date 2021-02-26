<template>
<div>
    <PainelCancelamento 
        v-if=" showCancelConfirmation"
        @showPanel = "showCancelConfirmation = $event"
        @confirmedCancellation = "confirmedCancellation = $event"
        :date = date
    >
    </PainelCancelamento> 

    <p v-show="showUpdatedAlert" style="text-align: center;">
            <span class="alert alert-success">Status da Consulta Atualizado com sucesso!</span><br>
        </p>
    <br>
    <div class="col d-flex justify-content-center">
        <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header' style="background-color: #43A390;">
                <h3>Histório de Consultas</h3>
            </div>
            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th>Data</th>
                        <th scope="col">Hora</th>
                        <th scope="col">Pagamento</th>
                        <th scope="col">Tipo</th>
                        <th scope="col">Médico</th>
                        <th scope="col">Status</th>
                        <th scope="col" colspan="2">Ações</th>
                    </tr>
                </thead>
                <tbody>
                        <tr v-for='(appointment, index) in appointments' :key='index'>
                            <td> {{appointment.Cons_Data.slice(8,10) + '/' + appointment.Cons_Data.slice(5,7) + '/' + appointment.Cons_Data.slice(0,4)}} </td>
                            <td> {{appointment.Cons_Horario.slice(0,5)}} </td>
                            <td> {{appointment.Cons_Pagamento}} </td>
                            <td> {{appointment.Cons_Tipo}} </td>
                            <td> {{appointment.medico.Med_Nome}} </td>
                            <td> {{appointment.Cons_Status}} </td>
                            <td>
                                <button v-show="editionMode[index] == false && appointment.Cons_Status != 'Cancelada'" class="btn btn-primary" @click="enableEditionMode(index)">Editar Status</button>
                                <select @change="onChange($event, appointment.Cons_Data)" v-show="editionMode[index] == true" v-model="appointment.Cons_Status"> 
                                    <option value="Marcada">Marcada</option>
                                    <option value="Concluída">Concluída</option>
                                    <option value="Cancelada">Cancelada</option>
                                </select>
                                <button @click="disableEditionMode(index)" @click.prevent="editAppoitmentStatus(index)" style="margin-left: 5%;" class="btn btn-success" v-if="editionMode[index] == true">Salvar</button>
                                <button @click="disableEditionMode(index)" @click.prevent="readAppointments()" style="margin-left: 5%;" class="btn btn-danger" v-if="editionMode[index] == true">Cancelar</button>
                            </td>
                        </tr>
      
                </tbody>
            </table>
        </div>
        </div>
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
import PainelCancelamento from './Painel_Cancelamento.vue'
export default {
    components: {
        PainelCancelamento
    },

    created() {
        this.readAppointments()
    },
    data() {
        return {
            appointments: [],
            id: this.$route.params.id,
            editionMode: [],
            showUpdatedAlert: false,
            showCancelConfirmation: false,
            confirmedCancellation: false,
            date: ''
        }
    },
    methods: {
        readAppointments() {
            this.appointments = []
            this.editionMode = []
            httpRequests.readAll('consulta').then( response => {
                for (let appointment of response.data.objects) {
                    if (parseInt(appointment.Cons_Pct_ID) == this.id) {
                        this.appointments.push(appointment)
                        this.editionMode.push(false)
                    }
                }
            })
        },
        onChange(event, date) {
            if (event.target.value == 'Cancelada') {
                this.date = date
                this.showCancelConfirmation = true
            }
        },
        editAppoitmentStatus(id) {
           

            httpRequests.update('consulta', this.appointments[id].Cons_ID, {
                'Cons_Status': this.appointments[id].Cons_Status
            }).then(() => {
                this.showUpdatedAlert = true
                setTimeout(() => {
                    this.showUpdatedAlert = false
                }, 2000)
                this.readAppointments()
            })
        },
        enableEditionMode(id) {
            this.editionMode.splice(id, 1, true)
        },
        disableEditionMode(id) {
            this.editionMode.splice(id, 1, false)
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
  background-color: #D5E6E6;
}
</style>

<style scoped>
h3 {
    color: white;
    text-align: center;
}
</style>