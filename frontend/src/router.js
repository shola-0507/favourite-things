import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Home
        },{
            path: '/createCategory',
            name: 'category',
            component: () => import('./views/CreateCategory')
        },{
            path: '/createItem',
            name: 'createItem',
            component: () => import('./views/CreateItem')
        },{
            path: '/logs',
            name: 'Logs',
            component: () => import('./views/Logs')
        }
    ]
})