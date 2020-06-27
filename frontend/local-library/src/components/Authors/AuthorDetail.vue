<template>
  <div>
    <h3 class="center-align indigo-text text-darken-3 gd-grey">
      {{ author.first_name }} {{ author.last_name }}
    </h3>
    <h5 class="center-align indigo-text text-darken-4">
      {{ author.date_of_birth | happyDate }} -
      {{ author.date_of_death | happyDate }}
    </h5>
    <ul class="collection with-header">
      <li class="collection-header">
        <h4>Books:</h4>
      </li>
      <book-li
        v-for="book in author.books"
        :key="book.id"
        v-bind:book="book"
      ></book-li>
    </ul>
  </div>
</template>

<script>
import BookListItem from "@/components/Books/BookLi.vue";
export default {
  name: "AuthorDetail",
  data() {
    return {
      author: {
        books: [],
      },
    };
  },
  components: {
    "book-li": BookListItem,
  },
  methods: {
    getAuthor() {
      const url = `${this.$backEnd}${this.$route.path}`;
      this.$http
        .get(url)
        .then((response) => response.data)
        .then((data) => {
          this.author = data;
        });
    },
  },
  watch: {
    $route() {
      this.getAuthor();
    },
  },
  mounted() {
    this.getAuthor();
  },
};
</script>

<style lang="css" scoped>
.gd-grey {
  background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}
</style>
