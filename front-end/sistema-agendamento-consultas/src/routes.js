import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
    mode: 'history',
    routes: [
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
            path: '/AgendarConsulta',
            name: 'AgendamentoConsulta',
            component: () => import('./components/Agendamento_Consulta.vue')
        },
        {
            path: '/AgendaMedica/:id',
            component: () => import('./components/Agenda_Medica.vue')
        },
        {
            path: '/Login',
            name: 'Login',
            component: () => import('./components/Login.vue')
        }
    ]
})