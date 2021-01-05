<template>
  <div>
    <nav v-if="this.$route.fullPath!='/Login' && this.$route.fullPath!='/CadastroPaciente'" class="navbar navbar-expand-lg navbar-dark bg-dark"> 
      <a class="navbar-brand">[NOME DA CLÍNICA]</a>

    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
      <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
      <li class="nav-item">
        <a class="nav-link" href="/GerenciaPaciente">Paciente</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/GerenciaMedico">Médico</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/GerenciaAtendente">Atendente</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/AgendarConsulta">Agendar Consulta</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/AgendarConsulta">Política de Agendamento</a>
      </li>
  
    </ul>
      <div>
        <a style="color: white;" class="nav-link" href="/Login">Sair</a>
      </div>
    </div>  
  </nav>
    <br><br>
    <router-view></router-view>
  </div>
  
</template>



<script>
export default {
  name: 'App',
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
