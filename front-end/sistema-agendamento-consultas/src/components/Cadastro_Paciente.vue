<template>
    <div>
         <PainelAviso v-if="showInformation"
            @showPanel = "showInformation = $event"
         >
         </PainelAviso>
    <div class="container-fluid">
        <div class="col d-flex justify-content-center">
            <div class="card shadow bg-light border-dark mb-3" style="width: 30%;">
                <div class="card-header border-dark">
                    <br>
                    <h3><b>Cadastro de Paciente {{userData}}</b></h3> 
                    <br>
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
                        <input type="text" class="form-control" v-model="CPF">
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
                        <input @click="riskGroup = 1" name="riskGroup" type="radio"> Sim
                        <input @click="riskGroup = 0" name="riskGroup" type="radio"> Não <br>
                    </div>
                    <div class='form-group'>
                        <span>Como saber se sou um paciente do Grupo de Risco? <br> 
                        <a href="javascript:void(0);" @click="showInformation = true"> Clique Aqui </a></span>
                    </div>
                </form>

                <button @click="createUser()" class="btn btn-primary rounded-pill">Enviar</button><br><br>

                <p v-show="showIncompleteAlert" style="text-align: center;">
                    <span class="alert alert-warning">Preencha todos os campos para prosseguir.</span><br>
                </p>
                <p v-show="showCreatedAlert" style="text-align: center;">
                    <span class="alert alert-success">Paciente cadastrado com sucesso!</span><br>
                </p>
                <br>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import httpRequests from '../http-requests'
import PainelAviso from './Painel_Aviso'
export default {
    components: {
        PainelAviso
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
            userData: '',
            showInformation: '',
            showIncompleteAlert: false,
            showCreatedAlert: false
        }
    },
    methods: {
        createUser() {
            if (!this.name || !this.RG || !this.CPF || !this.address || !this.email || !this.telephone || !this.password || this.riskGroup === '') {
                this.showIncompleteAlert = true
                return
            }

            httpRequests.create('paciente', 
                {'Pct_Nome': this.name,
                 'Pct_Rg': this.RG,
                 'Pct_CPF': this.CPF,
                 'Pct_Endereco': this.address,
                 'Pct_Email': this.email,
                 'Pct_Telefone': this.telephone,
                 'Pct_Senha': this.password,
                 'Pct_Grupo_Risco': this.riskGroup
            }).then ( () => {
                this.showIncompleteAlert = false
                this.showCreatedAlert = true
                setTimeout(() => {
                    this.$router.push('/Login')
                }, 2000)
            })
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

button{
    text-align: center; 
    margin: 0 auto;
    float: none; 
    width: 25%;
}

h3 {
    text-align: center;
}

form {
    text-align: center;

}


</style>