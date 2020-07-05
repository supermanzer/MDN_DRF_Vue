/** views/Login.vue This SFC file defines a login form we will use to
authenticate visitors to our Local Library site. */
<template>
  <div class="container">
    <div class="row valign-wrapper">
      <div class="col s8 offset-s2">
        <div class="card">
          <div class="card-image">
            <div class="gradient"></div>
            <span class="card-title">Log in to your Local Library</span>
          </div>
          <div class="card-content">
            <login-form></login-form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import LoginForm from "@/components/Registration/LoginForm.vue";
export default {
  components: {
    "login-form": LoginForm,
  },
};
</script>

<style>
.container,
.row {
  height: 90%;
}
.gradient {
  min-height: 20rem;
  background-image: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
</style>
