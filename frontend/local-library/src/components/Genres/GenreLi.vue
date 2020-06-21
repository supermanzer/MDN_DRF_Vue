<template>
  <li>
    <div class="collapsible-header">
      {{ genre.name }}
      <span class="right">
        <span class="badge">{{ genre.books.length }} Books</span>
      </span>
    </div>
    <div class="collapsible-body">
      <ul v-if="genre.books">
        <li v-for="book in genre.books" :key="book.id">
          <P>{{ book.title }}</P>
        </li>
      </ul>
    </div>
  </li>
</template>

<script>
export default {
  name: "GenreLi",
  props: {
    genre: Object,
  },
};
</script>
