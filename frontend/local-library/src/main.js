import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import store from './store'
import "materialize-css/dist/css/materialize.css";
import M from "materialize-css";
import "./filters"

const backEnd = "http://127.0.0.1:8000";
const logIn = `${backEnd}/api-auth/login/`;
const logOut = `${backEnd}/api-auth/logout/`;

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.prototype.$backEnd = backEnd;
Vue.prototype.$logIn = logIn;
Vue.prototype.$logOut = logOut;
Vue.prototype.$M = M;

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");