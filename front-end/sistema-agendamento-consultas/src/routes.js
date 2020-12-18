import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export const router = new Router({
    mode: 'history',
    routes: [
        {
            path: '/UserRegistration',
            name: 'UserRegistration',
            component: () => import('./components/UserRegistration.vue')
        }
    ]
})