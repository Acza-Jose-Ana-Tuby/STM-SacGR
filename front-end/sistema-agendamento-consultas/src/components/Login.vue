<template>
    <div class="container-fluid">
        <div class="col d-flex justify-content-center">
            <div class="card shadow bg-light border-dark mb-3" style="width: 25%;">
                <div class="card-header border-dark">
                    <br>
                    <h3><b>Login</b></h3> 
                    <br>
                </div>
                <form>
                    <br>
                    <div class='form-group'>
                        <label>E-Mail</label><br>
                        <input type="text" class="form-control" v-model="email">
                    </div>

                    <div class='form-group'>
                        <label>Senha</label><br>
                        <input type="password" class="form-control" v-model="password">
 
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
    created() {
        this.readUsers()
    },
    data () {
        return {
            users: [],
            userIndex: '',
            email: '',
            password: ''
        }
    }, 
    methods: {
        goToApplication() {
            this.$router.push('/AgendarConsulta')
        },
        goToSignUpPage() {
            this.$router.push('/CadastroPaciente')
        },
        readUsers() {
            httpRequests.readAll('paciente').then(response => {
                this.users = response.data.objects
            })
        }, 
        checkUser() {
            /*
            for (let user of users) {
                if (user.Pct_Email == this.email) {
                    this.userIndex = this.user.Pct_ID
                    return false
                }
            }
            return true 

            for (let i = 0 ; i < listLength ; i++) {
                if (this.users[i].Pct_Email == this.email) { 
                    this.userIndex = i 
                    console.log(i)
                    return true
                }
            } 
            return false */
        }, 
        checkCredentials() {
            if (this.users[this.userIndex].password == this.password) {
                return true
            }
            return false 
        },
        login() { 
            if (!this.checkUser()) {
                return 
            } 
            if (!this.checkCredentials()) {
                return
            } 
            this.goToApplication()
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