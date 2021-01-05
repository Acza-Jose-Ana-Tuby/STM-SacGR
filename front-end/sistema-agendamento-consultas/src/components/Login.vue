<template>
    <div class="container-fluid">
        <div class="col d-flex justify-content-center">
            <div class="card shadow bg-light border-dark mb-3" style="width: 25%;">
                <div class="card-header border-dark">
                    <br>
                    <h3><b>Login {{userData}}</b></h3> 
                    <br>
                </div>
                <form>
                    <br>
                    <div class='form-group'>
                        <label>E-Mail</label><br>
                        <input type="text" class="form-control" v-model="name">
                    </div>
                    <div class='form-group'>
                        <label>Senha</label><br>
                        <input type="text" class="form-control" v-model="RG">
                    </div>
                    <div class='form-group'>
                        <span>Ainda não possui cadastro no sistema?<br> 
                        <a href="javascript:void(0);" @click="goToSignUpPage()"> Clique Aqui </a></span>
                    </div>
                </form>
                <button @click="goToApplication()" class="btn btn-primary rounded-pill">Entrar</button><br>
            </div>
        </div>
    </div>
</template>

<script>
import httpRequests from '../http-requests'
export default {
    methods: {
        goToApplication() {
            this.$router.push('/AgendarConsulta')
        },
        goToSignUpPage() {
            this.$router.push('/CadastroPaciente')
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

h3, form {
    text-align: center;
}

</style>