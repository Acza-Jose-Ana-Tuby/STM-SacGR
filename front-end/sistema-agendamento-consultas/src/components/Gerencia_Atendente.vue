<template>
<div>
    <p v-show="showDeletedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados do Atendente Excluídos com Sucesso</span>
    </p>
    <br>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header' style="background-color: #43A390;">
                <h3>Gerenciar Atendentes</h3>
            </div>
            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th scope="col">Nome</th>
                        <th scope="col">E-Mail</th>
                        <th scope="col">Telefone</th>
                        <th scope="col">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for='(clerk, index) in clerks' :key=index>
                        <td>{{ clerk.Atd_Nome }}</td>
                        <td>{{ clerk.Atd_Email }}</td>
                        <td>{{ clerk.Atd_Telefone }}</td>
                        <td>
                            <button @click="updateClerk(clerk.Atd_ID)" class="btn btn-warning">Editar</button>
                            <button @click="deleteClerk(clerk.Atd_ID)" class="btn btn-danger" style="margin-left: 5%;">Excluir</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align: center;">
                <button @click="createClerk()" style="width: 15%;" class="btn btn-success">Adicionar Atendente</button>
            </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readClerks()
    },
    data () {
        return {
            clerks: [],
            tableSize: '',
            showDeletedAlert: ''
        }
    },
    methods: {
        createClerk() {
            this.$router.push('/GerenciaAtendente/-1')
        },
        readClerks() {
            httpRequests.readAll('atendente')
            .then(
                response => (
                    this.clerks = response.data.objects
                )
            )
        },
        updateClerk(id) {
            this.$router.push(`/GerenciaAtendente/${id}`)
        },
        deleteClerk(id) {
            httpRequests.delete('atendente', id)
                .then(
                    response => (
                        this.showDeletedAlert = true,
                        this.readClerks(),
                        setTimeout(() => {
                            this.showDeletedAlert = false
                        }, 2000)
                    )
                )
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