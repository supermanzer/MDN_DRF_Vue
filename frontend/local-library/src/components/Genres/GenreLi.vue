<template>
  <li>
    <div class="collapsible-header">
      {{ genre.name }}
      <span class="right">
        <span class="badge">{{ genre.books.length }} Books</span>
      </span>
    </div>
    <div class="collapsible-body">
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Officiis
      consequuntur quidem odit vero, quod atque! Aspernatur recusandae ab
      consequatur adipisci unde est iure velit, asperiores, temporibus facilis
      nobis doloremque! Odio.
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
