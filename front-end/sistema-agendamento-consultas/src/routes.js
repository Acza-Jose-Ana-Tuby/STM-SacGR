import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/PoliticaAgendamento',
            name: 'PoliticaAgendamento',
            component: () => import('./components/Politica_Agendamento.vue')
        },
        {
            path: '/CadastroPaciente',
            name: 'CadastroPaciente',
            component: () => import('./components/Cadastro_Paciente.vue')
        },
        {
            path: '/GerenciaPaciente',
            name: 'GerenciaPaciente',
            component: () => import('./components/Gerencia_Paciente.vue')
        },
        {
            path: '/GerenciaAdministrador',
            name: 'GerenciaAdministrador',
            component: () => import('./components/Gerencia_Administrador.vue')
        },
        {
            path: '/GerenciaAdministrador/:id',
            component: () => import('./components/Gerencia_Administrador_Form.vue')
        },
        {
            path: '/GerenciaPaciente/:id',
            component: () => import('./components/Gerencia_Paciente_Form.vue')
        },
        {
            path: '/GerenciaMedico',
            name: 'GerenciaMedico',
            component: () => import('./components/Gerencia_Medico.vue')
        },
        {
            path: '/GerenciaMedico/:id',
            component: () => import('./components/Gerencia_Medico_Form.vue')
        },
        {
            path: '/GerenciaAtendente',
            name: 'GerenciaAtendente',
            component: () => import('./components/Gerencia_Atendente.vue')
        },
        {
            path: '/GerenciaAtendente/:id',
            component: () => import('./components/Gerencia_Atendente_Form.vue')
        },
        {
            path: '/AgendarConsulta/:id',
            name: 'AgendamentoConsulta',
            component: () => import('./components/Agendamento_Consulta.vue')
        },
        {
            path: '/AgendaMedica/:id',
            name: 'AgendaMedica', 
            component: () => import('./components/Agenda_Medica.vue')
        },
        {
            path: '/HistoricoConsultas/:id',
            name: 'HistoricoConsultas',
            component: () => import('./components/Historico_Consulta.vue')
        },
        {
            path: '/Login',
            name: 'Login',
            component: () => import('./components/Login.vue')
        },
    ]
})