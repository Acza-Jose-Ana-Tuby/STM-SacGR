<template>
<div>

    <p v-show="showIncompleteAlert" style="text-align: center;">
        <span class="alert alert-warning">Preencha todos os campos para prosseguir.</span><br>
    </p>
    <p v-show="showCreatedAlert" style="text-align: center;">
        <span class="alert alert-success">Paciente criado com sucesso!</span><br>
    </p>
    <p v-show="showUpdatedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados atualizados com sucesso!</span><br>
    </p>

    <div class="col d-flex justify-content-center">
        <div class="card bg-light " style="width: 70%;"> 
            <div v-show="id=='-1'" class="card-header"> 
                <h3>Cadastrar novo Paciente</h3>
            </div>
            <div v-show="id!='-1'" class="card-header"> 
                <h3>Editar dados do Paciente</h3>
            </div>
           <form>
                    <br>
                    <div class='form-group'>
                        <label>Nome</label><br>
                        <input type="text" class="form-control" v-model="name">
                    </div>
                    <div class='form-group'>
                        <label>RG</label><br>
                        <input type="text" class="form-control" v-model="RG">
                    </div>
                    <div class='form-group'>
                        <label>CPF</label><br>
                        <input type="text" class="form-control" v-model="CPF" placeholder="Digite Somente Números">
                    </div>
                    <div class='form-group'>
                        <label>Endereço</label><br>
                        <input type="text" class="form-control" v-model="address">
                    </div>
                    <div class='form-group'>
                        <label>E-mail</label><br>
                        <input type="email" class="form-control" v-model="email">
                    </div>
                    <div class='form-group'>
                        <label>Telefone</label><br>
                        <input type="text" class="form-control" v-model="telephone">
                    </div>
                    <div class='form-group'>
                        <label>Senha</label><br>
                        <input type="password" class="form-control" v-model="password">
                    </div>
                    <div class='form-group'>
                        <label>Pertence a algum grupo de risco?</label><br>
                        <input name="riskGroup" @click="riskGroup = 1" type="radio"> Sim
                        <input name="riskGroup" @click="riskGroup = 0" type="radio"> Não
                    </div><br>
                </form>
                <p style="text-align: center;">
                    <button v-show="id=='-1'" @click="createPatient()" class="btn btn-success" style="width: 15%">Adicionar Paciente</button>
                    <button v-show="id!='-1'" @click="createPatient()" class="btn btn-success" style="width: 15%">Salvar Alterações</button>
                </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readPatient()
    },
    data() {
        return {
            name: '',
            RG: '',
            CPF: '',
            address: '',
            email: '',
            telephone: '',
            password: '',
            riskGroup: '',
            id: this.$route.params.id,
            showIncompleteAlert: false,
            showCreatedAlert: false,
            showUpdatedAlert: false
        }
    },
    methods: {
        backToList() {
            this.$router.push({name: 'GerenciaPaciente'})  
        },
        readPatient() {
            if (this.id != '-1') {
                httpRequests.read('paciente', this.id).then(response => (
                        this.name = response.data.Pct_Nome,
                        this.RG = response.data.Pct_Rg,
                        this.CPF = response.data.Pct_CPF,
                        this.address = response.data.Pct_Endereco,
                        this.email = response.data.Pct_Email,
                        this.telephone = response.data.Pct_Telefone,
                        this.password = response.data.Pct_Senha
                    ))
            }
        },
        createPatient() {
            if (!this.name || !this.RG || !this.CPF || !this.address || !this.email || !this.telephone || !this.password) {
                this.showIncompleteAlert = true
                return 
            }
            if (this.id == '-1') {
                httpRequests.create('paciente', 
                    {   'Pct_Nome': this.name,
                        'Pct_Rg': this.RG,
                        'Pct_CPF': this.CPF,
                        'Pct_Endereco': this.address,
                        'Pct_Email': this.email,
                        'Pct_Telefone': this.telephone,
                        'Pct_Senha': this.password,
                        'Pct_Grupo_Risco': this.riskGroup
                    }
                ).then(() => {
                    this.showIncompleteAlert = false
                    this.showCreatedAlert = true
                    setTimeout(() => {
                        this.backToList()
                    }, 2000)
                })
            } else {
                httpRequests.update('paciente', this.id,
                    {   'Pct_Nome': this.name,
                        'Pct_Rg': this.RG,
                        'Pct_CPF': this.CPF,
                        'Pct_Endereco': this.address,
                        'Pct_Email': this.email,
                        'Pct_Telefone': this.telephone,
                        'Pct_Senha': this.password,
                        'Pct_Grupo_Risco': this.riskGroup
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
    margin: 0 auto;
}


</style>