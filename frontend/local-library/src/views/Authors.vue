<template>
  <div class="container">
    <div class="row">
      <h2>Authors</h2>
      <div class="divider"></div>
      <p class="flow-text">
        Below are the authors whose books are carried by your locall library
      </p>
      <div class="col s12 m6 l4" v-for="author in authors" :key="author.id">
        <author-card v-bind:author="author"></author-card>
      </div>
    </div>
    <div class="row">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import AuthorCard from "@/components/Authors/AuthorCard.vue";

export default {
  components: {
    "author-card": AuthorCard,
  },
  data() {
    return {
      authors: [],
    };
  },
  mounted() {
    const url = `${this.$backEnd}/authors/`;
    this.$http
      .get(url)
      .then((response) => response.data)
      .then((data) => {
        this.authors = data;
      });
  },
};
</script>
