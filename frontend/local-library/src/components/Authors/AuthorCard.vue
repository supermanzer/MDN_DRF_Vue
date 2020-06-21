<template>
  <div class="card author-card">
    <div class="card-content">
      <span class="card-title">
        <router-link :to="{ name: 'Author', params: { id: author.id } }">
          {{ author.last_name }}, {{ author.first_name }}
        </router-link>
      </span>
      <p>
        {{ author.date_of_birth | happyDate }} -
        {{ author.date_of_death | happyDate }}
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthorCard",
  props: {
    author: Object,
  },
};
</script>

<style lang="css">
.author-card {
  background-image: linear-gradient(to top, #e6e9f0 0%, #eef1f5 100%);
}
</style>
