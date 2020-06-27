<template>
  <div class="book-detail card">
    <div class="card-image waves-effect waves-block waves-light">
      <img :src="book.header_image" alt="Header Image" class="activator" />
    </div>
    <div class="card-content">
      <span class="card-title activator grey-text text-darken-4">
        {{ book.title }}
      </span>
      <p>
        by <b>{{ book.author.first_name }} {{ book.author.last_name }}</b>
      </p>
      <p>Genres:</p>
      <div class="chip" v-for="genre in book.genres" :key="genre.name">
        {{ genre.name }}
      </div>
      <div class="divider"></div>
      <p class="summary">{{ book.summary }}</p>
      <div class="card-action">
        <span class="card-title grey-text text-darken-4">
          Copies of {{ book.title }}
        </span>
        <ul class="collection">
          <copy-li
            v-for="copy in book.copies"
            :key="copy.id"
            v-bind:copy="copy"
          ></copy-li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import CopyListItem from "@/components/Books/CopyLi.vue";
export default {
  name: "BookDetail",
  components: {
    "copy-li": CopyListItem,
  },
  data() {
    return {
      book: {
        author: {},
        genres: [],
        copies: [],
      },
    };
  },
  methods: {
    getBook() {
      const url = `${this.$backEnd}${this.$route.path}`;
      this.$http
        .get(url)
        .then((response) => {
          this.book = response.data;
        })
        .catch((err) => console.error(err));
    },
  },
  watch: {
    $route() {
      this.getBook();
    },
  },
  mounted() {
    this.getBook();
  },
};
</script>

<style lang="css" scoped>
.book-detail {
  min-height: 30em;
}
.divider {
  margin-top: 2em;
  margin-bottom: 2em;
}
.summary {
  margin-top: 2em;
  margin-bottom: 2em !important;
}
</style>
