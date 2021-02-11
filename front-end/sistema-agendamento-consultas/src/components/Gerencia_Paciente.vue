<template>
<div>
    <p v-show="showDeletedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados do Paciente Excluídos com Sucesso</span>
    </p>
    <br>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
             <div class='card-header bg-dark'>
                <h3>Gerenciar Pacientes</h3>
            </div>
            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th scope="col">Nome</th>
                        <th scope="col">RG</th>
                        <th scope="col">CPF</th>
                        <th scope="col">E-Mail</th>
                        <th scope="col">Telefone</th>
                        <th scope="col">Grupo De Risco</th>
                        <th scope="col">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for='(patient, index) in patients' :key=index>
                        <td>{{ patient.Pct_Nome }}</td>
                        <td>{{ patient.Pct_Rg }}</td>
                        <td>{{ patient.Pct_CPF }}</td>
                        <td>{{ patient.Pct_Email }}</td>
                        <td>{{ patient.Pct_Telefone }}</td>
                        <td v-if="patient.Pct_Grupo_Risco == 0">Não Pertence</td>
                        <td v-if="patient.Pct_Grupo_Risco == 1">Pertence</td>
                        <td>
                            <button @click="markAppointment(patient.Pct_ID)" class="btn btn-info" >Marcar Consulta</button>
                            <button @click="updatePatient(patient.Pct_ID)" class="btn btn-primary" style="margin-left: 5%;">Editar</button>
                            <button @click="deletePatient(patient.Pct_ID)" class="btn btn-danger" style="margin-left: 5%;">Excluir</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align: center;">
                <button @click="createPatient()" style="width: 15%;" class="btn btn-success">Adicionar Paciente</button>
            </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readPatients()
    },
    data () {
        return {
            patients: [],
            tableSize: '',
            showDeletedAlert: ''
        }
    },
    methods: {
        createPatient() {
            this.$router.push('/GerenciaPaciente/-1')
        },
        readPatients() {
            httpRequests.readAll('paciente')
            .then(
                response => (
                    this.patients = response.data.objects
                )
            )
        },
        updatePatient(id) {
            this.$router.push(`/GerenciaPaciente/${id}`)
        },
        deletePatient(id) {
            httpRequests.delete('paciente', id)
                .then(
                    response => (
                        this.showDeletedAlert = true,
                        this.readPatients(),
                        setTimeout(() => {
                            this.showDeletedAlert = false
                        }, 2000)
                    )
                )
        },
        markAppointment(id) {
            this.$router.push(`/AgendarConsulta/${id}`)
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

</style>