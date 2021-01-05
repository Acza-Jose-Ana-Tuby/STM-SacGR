<template>
<div>

    <p v-show="showIncompleteAlert" style="text-align: center;">
        <span class="alert alert-warning">Preencha todos os campos para prosseguir.</span><br>
    </p>
    <p v-show="showCreatedAlert" style="text-align: center;">
        <span class="alert alert-success">Médico criado com sucesso!</span><br>
    </p>
    <p v-show="showUpdatedAlert" style="text-align: center;">
        <span class="alert alert-success">Dados atualizados com sucesso!</span><br>
    </p>

    <div class="col d-flex justify-content-center">
        <div class="card bg-light " style="width: 70%;"> 
            <div v-show="id=='-1'" class="card-header"> 
                <h3>Cadastrar novo Médico</h3>
            </div>
            <div v-show="id!='-1'" class="card-header"> 
                <h3>Editar dados do Médico</h3>
            </div>
           <form>
                    <br>
                    <div class='form-group'>
                        <label>Nome</label><br>
                        <input type="text" class="form-control" v-model="name">
                    </div>
                    <div class='form-group'>
                        <label>CRM</label><br>
                        <input type="text" class="form-control" v-model="CRM">
                    </div>
                    <div class='form-group'>
                        <label>E-Mail</label><br>
                        <input type="text" class="form-control" v-model="email">
                    </div>
                     <div class='form-group'>
                        <label>Telefone</label><br>
                        <input type="text" class="form-control" v-model="telephone">
                    </div>
                    <div class='form-group'>
                        <label>Especialização</label><br>
                        <input type="text" class="form-control" v-model="specialization">
                    </div>
                    <br>
                </form>
                <p style="text-align: center;">
                    <button v-show="id=='-1'" @click="createDoctor()" class="btn btn-success" style="width: 15%">Adicionar Médico</button>
                    <button v-show="id!='-1'" @click="createDoctor()" class="btn btn-success" style="width: 15%">Salvar Alterações</button>
                </p>
        </div>    
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    created() {
        this.readDoctor()
    },
    data() {
        return {
            name: '',
            CRM: '',
            specialization: '',
            email: '', 
            telephone: '',
            id: this.$route.params.id,
            showIncompleteAlert: false,
            showCreatedAlert: false,
            showUpdatedAlert: false
        }
    },
    methods: {
        backToList() {
            this.$router.push({name: 'GerenciaMedico'})  
        },
        readDoctor() {
            if (this.id != '-1') {
                httpRequests.read('medico', this.id).then(response => (
                        this.name = response.data.Med_Nome,
                        this.CRM = response.data.Med_CRM,
                        this.email = response.data.Med_Email,
                        this.telephone = response.data.Med_Telefone,
                        this.specialization = response.data.Med_Especialidade
                    ))
            }
        },
        createDoctor() {
            if (!this.name || !this.CRM || !this.specialization) {
                this.showIncompleteAlert = true
                return 
            }
            if (this.id == '-1') {
                httpRequests.create('medico', 
                    {   'Med_Nome': this.name,
                        'Med_CRM': this.CRM,
                        'Med_Email': this.email,
                        'Med_Telefone': this.telephone,
                        'Med_Especialidade': this.specialization
                    }
                ).then(() => {
                    this.showIncompleteAlert = false
                    this.showCreatedAlert = true
                    setTimeout(() => {
                        this.backToList()
                    }, 2000)
                })
            } else {
                httpRequests.update('medico', this.id,
                    {   'Med_Nome': this.name,
                        'Med_CRM': this.CRM,
                        'Med_Email': this.email,
                        'Med_Telefone': this.telephone,
                        'Med_Especialidade': this.specialization
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
    margin: auto;
    text-align: center;
}

</style>