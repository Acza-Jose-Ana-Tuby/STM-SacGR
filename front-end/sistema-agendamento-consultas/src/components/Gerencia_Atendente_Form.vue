<template>
<div>
    <p v-show="showIncompleteAlert" style="text-align: center;">
        <span class="alert alert-warning">Preencha todos os campos para prosseguir.</span><br>
    </p>
    <p v-show="showCreatedAlert" style="text-align: center;">
        <span class="alert alert-success">Atendente criado com sucesso!</span><br>
    </p>
    <p v-show="showUpdatedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados atualizados com sucesso!</span><br>
    </p>

    <div class="col d-flex justify-content-center">
        <div class="card bg-light " style="width: 70%;"> 
            <div v-show="id=='-1'" class="card-header"> 
                <h3>Cadastrar novo Atendente</h3>
            </div>
            <div v-show="id!='-1'" class="card-header"> 
                <h3>Editar dados do Atendente</h3>
            </div>
           <form>
                    <br>
                    <div class='form-group'>
                        <label>Nome</label><br>
                        <input type="text" class="form-control" v-model="name">
                    </div>
                    <div class='form-group'>
                        <label>E-mail</label><br>
                        <input type="text" class="form-control" v-model="email">
                    </div>
                    <div class='form-group'>
                        <label>Telefone</label><br>
                        <input type="text" class="form-control" v-model="telephone">
                    </div>
                    <div class='form-group'>
                        <label>Senha</label><br>
                        <input v-show="id == '-1'" type="password" class="form-control" v-model="password">
                        <input v-show="id != '-1'" type="password" class="form-control" placeholder="Nova Senha" v-model="password">
                    </div>
                    <br>
                </form>
                <p style="text-align: center;">
                    <button v-show="id=='-1'" @click="createClerk()" class="btn btn-success" style="width: 15%">Adicionar Atendente</button>
                    <button v-show="id!='-1'" @click="createClerk()" class="btn btn-success" style="width: 15%">Salvar Alterações</button>
                </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readClerk()
    },
    data() {
        return {
            name: '',
            email: '',
            telephone: '',
            password: '',
            id: this.$route.params.id,
            showIncompleteAlert: false,
            showCreatedAlert: false,
            showUpdatedAlert: false
        }
    },
    methods: {
        backToList() {
            this.$router.push({name: 'GerenciaAtendente'})  
        },
        readClerk() {
            if (this.id != '-1') {
                httpRequests.read('atendente', this.id).then(response => (
                        this.name = response.data.Atd_Nome,
                        this.email = response.data.Atd_Email,
                        this.telephone = response.data.Atd_Telefone
                ))
            }
        },
        createClerk() {
            if (!this.name || !this.email) {
                this.showIncompleteAlert = true
                return 
            }
            if (this.id == '-1') {
                httpRequests.create('atendente', 
                    {   'Atd_Nome': this.name,
                        'Atd_Email': this.email,
                        'Atd_Telefone': this.telephone,
                        'Atd_Senha': this.password
                    }
                ).then(() => {
                    this.showIncompleteAlert = false
                    this.showCreatedAlert = true
                    setTimeout(() => {
                        this.backToList()
                    }, 2000)
                })
            } else {
                httpRequests.update('atendente', this.id,
                    {   'Atd_Nome': this.name,
                        'Atd_Email': this.email,
                        'Atd_Telefone': this.telephone,
                        'Atd_Senha': this.password
                    }
                ).then(() => {
                    this.showIncompleteAlert = false
                    this.showUpdatedAlert = true
                    setTimeout(() => {
                        this.backToList()
                    }, 2000)
                })
            }
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

input[type="text"] { 
    text-align: center; 
    margin: 0 auto;
    float: none; 
    width: 75%;
}

input[type="password"] { 
    text-align: center; 
    margin: 0 auto;
    float: none; 
    width: 75%;
}

input[type="email"] { 
    text-align: center; 
    margin: 0 auto;
    float: none; 
    width: 75%;
}

h3 {
    text-align: center;
}

label {
    text-align: center;
}

</style>