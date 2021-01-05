<template>
<div>
    <p v-show="showDeletedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados do Médico Excluídos com Sucesso</span>
    </p>
    <br>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header bg-dark'>
                <h3>Gerenciar Médicos</h3>
            </div>

            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th scope="col">Nome</th>
                        <th scope="col">CRM</th>
                        <th scope="col">E-Mail</th>
                        <th scope="col">Telefone</th>
                        <th scope="col">Especialidade</th>
                        <th scope="col">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for='(doctor, index) in doctors' :key=index>
                        <td>{{ doctor.Med_Nome }}</td>
                        <td>{{ doctor.Med_CRM }}</td>
                        <td>{{ doctor.Med_Email }}</td>
                        <td>{{ doctor.Med_Telefone }}</td>
                        <td>{{ doctor.Med_Especialidade }}</td>
                        <td>
                            <button @click="viewSchedules(doctor.Med_ID)" class="btn btn-info">Agenda</button>
                            <button @click="updateDoctor(doctor.Med_ID)" class="btn btn-primary" style="margin-left: 5%;">Editar</button>
                            <button @click="deleteDoctor(doctor.Med_ID)" class="btn btn-danger" style="margin-left: 5%;">Excluir</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align: center;">
                <button @click="createDoctor()" style="width: 15%;" class="btn btn-success">Adicionar Médico</button>
            </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readDoctors()
    },
    data () {
        return {
            doctors: [],
            tableSize: '',
            showDeletedAlert: ''
        }
    },
    methods: {
        createDoctor() {
            this.$router.push('/GerenciaMedico/-1')
        },
        readDoctors() {
            httpRequests.readAll('medico')
            .then(
                response => (
                    this.doctors = response.data.objects
                )
            )
        },
        updateDoctor(id) {
            this.$router.push(`/GerenciaMedico/${id}`)
        },
        deleteDoctor(id) {
            httpRequests.delete('medico', id)
                .then(
                    response => (
                        this.showDeletedAlert = true,
                        this.readDoctors(),
                        setTimeout(() => {
                            this.showDeletedAlert = false
                        }, 2000)
                    )
                )
        },
        viewSchedules(id) {
            this.$router.push(`/AgendaMedica/${id}`)
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