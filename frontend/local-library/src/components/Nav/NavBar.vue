<template>
  <nav>
    <div class="nav-wrapper">
      <a href="/" class="brand-logo">Local Library</a>
      <ul class="right hide-on-med-and-down">
        <li v-for="link in links" :key="link.name">
          <router-link :to="{ name: link.name }" class="navbar-item">
            {{ link.name }}
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "LibraryNav",
  props: {
    title: String,
    links: Array,
  },
};
</script>

<style lang="css" scoped>
nav {
  background-image: linear-gradient(to top, #cfd9df 0%, #e2ebf0 100%);
  color: black;
  padding-left: 2em;
  padding-right: 2em;
}
a.brand-logo {
  color: black;
}
a.navbar-item {
  color: black;
}
</style>
