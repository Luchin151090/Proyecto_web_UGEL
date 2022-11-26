import Vue, { onMounted } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import VueApexCharts from 'vue-apexcharts'
import VueTour from 'vue-tour'

require('vue-tour/dist/vue-tour.css')



Vue.config.productionTip = false;

import VueRouter from "vue-router";
Vue.use(VueRouter);
Vue.use(VueApexCharts);
Vue.use(VueTour)


Vue.component('apexchart', VueApexCharts)

import LoginVue from "./components/LoginVue.vue";
import BusquedaVue from "./components/BusquedaVue.vue";
import DashboardVue from "./components/DashboardVue.vue";
import HomeVue from "./components/HomeVue.vue";
import CuentaVue from "./components/CuentaVue.vue";
import Dash2Vue from "./components/Dash2Vue.vue";
import RegistrarVue from "./components/RegistrarVue.vue";
import RegistroUser from "./components/RegistroUser.vue";
import ForgotPass from "./components/ForgotPass.vue";
import EditUser from "./components/EditUser.vue";
import BarraVue from "./components/BarraVue.vue";
import AdminUser from "./components/AdminUser.vue";
import TestVue from "./components/TestVue.vue";
const router = new VueRouter({
  mode: "history",
  base: __dirname,
  routes: [
    {
      path: "/admin",
      name: "admin",
      component: Dash2Vue,
      children: 
      [
        {
          path: "/admin/test",
          name: "adbus",
          component: BusquedaVue,
        },
        {
          path: "/admin/cuenta",
          name: "adcuen",
          component: CuentaVue,
        },
        {
          path: "/admin/administrar",
          name: "ada",
          component: RegistrarVue,
        },
        {
          path:"/admin/edit_user",
          name:"adedit_user",
          component: EditUser,
        }
      ],
    },
    {
      path:"/barra",
      name:"barra",
      component:BarraVue
    },
    {
      path:"/adminuser",
      name:"aduser",
      component:AdminUser
    },
    {
      path: "/",
      name: "home",
      component: DashboardVue,
      children: [
        {
          path: "/busquedas",
          name: "busquedas",
          component: BusquedaVue,
        },
        {
          path: "/cuenta",
          name: "cuenta",
          component: CuentaVue,
        },
        {
          path:'/test',
          name:"test",
          component:TestVue
        },
      ],
    },
    {
      path: "/logins",
      name: "logins",
      component: LoginVue,
    },
    {
      path:"/registro_user",
      name:"registro_user",
      component: RegistroUser
    },
    {
      path:"/forgot_pass",
      name:"forgot_pass",
      component: ForgotPass
    }
  ],
});



new Vue({
  vuetify,
  router,
  render: (h) => h(App),
}).$mount("#app");
