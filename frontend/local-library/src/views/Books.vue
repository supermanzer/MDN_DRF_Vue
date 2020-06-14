<template>
  <div class="books-list container">
    <div class="row">
      <h2>Books</h2>
      <div class="divider"></div>
      <p class="flow-text">
        Below are a list of books carried by your local libary
      </p>
      <ul class="collection">
        <li class="collection-item avatar" v-for="book in books" :key="book.id">
          <i class="material-icons circle">book</i>
          <span class="title">{{ book.title }}</span>
          <p>
            {{ book.display_author }} <br />
            More stuff goes here
          </p>
          <a href="#!" class="secondary-content">
            <i class="material-icons">grade</i>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    const url = `${this.$backEnd}books/`;
    this.$http
      .get(url)
      .then((response) => response.data)
      .then((data) => {
        this.books = data;
      });
  },
};
</script>

<style lang="css">
span.title {
  font-size: larger;
  font-weight: bold;
}
</style>
