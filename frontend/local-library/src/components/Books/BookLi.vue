<template>
  <li class="collection-item avatar">
    <i class="material-icons circle">book</i>
    <router-link :to="{ name: 'Book', params: { id: book.id } }">
      <span class="title">{{ book.title }}</span>
    </router-link>
    <p>
      {{ book.display_author }} <br />
      {{ book.summary | truncateWords(10) }} ....
    </p>
    <a href="#!" class="secondary-content">
      <i class="material-icons">grade</i>
    </a>
  </li>
</template>

<script>
export default {
  name: "BookListItem",
  props: {
    book: Object,
  },
};
</script>
