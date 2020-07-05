<template>
  <form class="row" @submit.prevent="authenticateUser">
    <div class="col s8 offset-s2 input-field">
      <input v-model="username" type="text" name="username" id="username" />
      <label for="username">Username</label>
    </div>
    <div class="col s8 offset-s2 input-field">
      <input v-model="password" type="password" name="password" id="password" />
      <label for="password">Password</label>
    </div>
    <div class="col s12 center-align input-field">
      <a href="/" class="btn cancel">Cancel</a>
      <button class="btn white-text" type="submit">Log In</button>
    </div>
  </form>
</template>

<script>
export default {
  name: "LoginForm",

  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    aunthenticateUser() {
      // Do form submission things here
      const payload = {
        username: this.username,
        password: this.password,
      };
      this.$http
        .post(this.$store.state.endpoints.obtainJWT, payload)
        .then((response) => {
          this.$store.commit("updateToken", response.data.token);
          const base = {
            baseURL: this.$store.state.endpoints.baseUrl,
            headers: {
              Authorization: `JWT ${(this.$store, state.jwt)}`,
              "Content-type": "application/json",
            },
            xhrFields: {
              withCredentials: true,
            },
          };

          const axInst = this.$http.create(base);
          axInst({
            url: "/user/",
            method: "get",
            params: [],
          }).then((response) => {
            this.$store.commit("setAuthUser", {
              authUser: response.data,
              isAuthenticated: true,
            });
            this.$router.push({ name: "Home" });
          });
        })
        .catch((error) => {
          console.log(error);
          console.debug(error);
        });
    },
  },
};
</script>

<style>
.btn {
  background-image: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
}
.cancel {
  background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
  margin-right: 5em;
}
.input-field {
  margin-top: 3em;
}
</style>
