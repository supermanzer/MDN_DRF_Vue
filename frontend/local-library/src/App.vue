<template>
  <div id="app">
    <div id="nav">
      <library-nav v-bind:links="nav_links" title="Local Library"></library-nav>
    </div>
    <router-view />
  </div>
</template>

<script>
import LibraryNav from "@/components/Nav/NavBar.vue";
import links from "@/router/links.js";
import { csrfMixin } from "@/mixins/csrfMixin.js";

export default {
  components: {
    "library-nav": LibraryNav,
  },
  mixins: [csrfMixin],
  data() {
    return {
      nav_links: links.top_level,
    };
  },
  mounted() {
    this.getToken(this.$backEnd);
  },
};
</script>

<style>
html,
body,
#app {
  height: 100%;
}
</style>
