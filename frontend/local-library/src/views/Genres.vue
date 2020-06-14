<template>
  <div class="container">
    <div class="row">
      <div class="col s12">
        <h2 class="center">Genres</h2>
        <div class="divider"></div>
        <p class="flow-text">
          The genres of books carred by your local library
        </p>
        <ul class="collapsible">
          <genre-li
            v-for="genre in genres"
            :key="genre.id"
            v-bind:genre="genre"
          >
          </genre-li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import GenreLi from "../components/Genres/GenreLi.vue";
export default {
  components: {
    "genre-li": GenreLi,
  },
  data() {
    return {
      genres: [],
    };
  },
  mounted() {
    const url = `${this.$backEnd}genres/`;
    this.$http
      .get(url)
      .then((response) => {
        this.genres = response.data;
      })
      .then(() => {
        this.$M.Collapsible.init(document.querySelectorAll(".collapsible"));
      });
  },
};
</script>
