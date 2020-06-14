import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import Axios from "axios";
import "materialize-css/dist/css/materialize.css";
import M from "materialize-css";

const backEnd = "http://127.0.0.1:8000/";

Vue.config.productionTip = false;
Vue.prototype.$http = Axios;
Vue.prototype.$backEnd = backEnd;
Vue.prototype.$M = M;

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
