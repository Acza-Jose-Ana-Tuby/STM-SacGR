<template>
<div>
    <p v-show="showDeletedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados do Médico Excluídos com Sucesso</span>
    </p>
    <br>
    <div class="col d-flex justify-content-center">
        <div class="card" style="width: 70%;"> 
            <div class='card-header' style="background-color: #43A390;">
                <h3>Gerenciar Administradores</h3>
            </div>

            <table class="table">
                <thead class="thead-light">
                    <tr>
                        <th scope="col">Nome</th>
                        <th scope="col">Telefone</th>
                        <th scope="col">E-Mail</th>
                        <th scope="col">Ações</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for='(admin, index) in clinicAdministrators' :key="index">
                        <td>{{ admin.AdmCli_Nome }}</td>
                        <td>{{ admin.AdmCli_Telefone }}</td>
                        <td>{{ admin.AdmCli_Email }}</td>
                        <td>
                            <button @click="updateAdmin(admin.AdmCli_ID)" class="btn btn-warning" style="margin-left: 5%;">Editar</button>
                            <button @click="deleteAdmin(admin.AdmCli_ID)" class="btn btn-danger" style="margin-left: 5%;">Excluir</button>
                        </td>
                    </tr>
                </tbody>
            </table>
            <p style="text-align: center;">
                <button @click="createAdmin()" style="width: 15%;" class="btn btn-success">Adicionar Administrador</button>
            </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readAdmins()
    },
    data () {
        return {
            clinicAdministrators: [],
            tableSize: '',
            showDeletedAlert: ''
        }
    },
    methods: {
        createAdmin() {
            this.$router.push('/GerenciaAdministrador/-1')
        },
        readAdmins() {
            httpRequests.readAll('adm_clinica')
            .then(
                response => (
                    this.clinicAdministrators = response.data.objects
                )
            )
        },
        updateAdmin(id) {
            this.$router.push(`/GerenciaAdministrador/${id}`)
        },
        deleteAdmin(id) {
            httpRequests.delete('adm_clinica', id)
                .then(
                    response => (
                        this.showDeletedAlert = true,
                        this.readAdmins(),
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