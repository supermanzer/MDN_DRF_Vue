<template>
  <div class="row">
    <h2>Books</h2>
    <div class="divider"></div>
    <p class="flow-text">
      Below are a list of books carried by your local libary
    </p>

    <ul class="collection">
      <book-li v-for="book in books" :key="book.id" v-bind:book="book">
      </book-li>
    </ul>
  </div>
</template>

<script>
import BookListItem from "@/components/Books/BookLi.vue";
export default {
  name: "BookList",
  props: {
    books: Array,
  },
  components: {
    "book-li": BookListItem,
  },
};
</script>
