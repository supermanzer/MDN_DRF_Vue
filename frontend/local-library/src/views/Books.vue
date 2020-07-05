<template>
  <div class="books container">
    <div class="row">
      <h2>Books</h2>
      <div class="divider"></div>
      <p class="flow-text">
        Below are a list of books carried by your local libary
      </p>
      <div class="col s6">
        <ul class="collection">
          <book-li
            v-for="book in books"
            :key="book.id"
            v-bind:book="book"
          ></book-li>
        </ul>
      </div>
      <div class="col s6">
        <transition name="fade">
          <router-view></router-view>
        </transition>
      </div>
    </div>
  </div>
</template>

<script>
import BookListItem from "@/components/Books/BookLi.vue";
export default {
  components: {
    "book-li": BookListItem,
  },
  data() {
    return {
      books: [],
    };
  },
  mounted() {
    const url = `${this.$backEnd}/books/`;
    this.$http
      .get(url)
      .then((response) => {
        return response.data;
      })
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

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.75s;
}
.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
