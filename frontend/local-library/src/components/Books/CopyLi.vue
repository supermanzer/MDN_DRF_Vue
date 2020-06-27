<template>
  <li class="collection-item">
    <strong
      :class="{
        available: copy.get_status_display == 'Available',
        maintenance: copy.get_status_display == 'Maintenance',
      }"
    >
      <i class="material-icons prefix">collections_bookmark</i>
      {{ copy.get_status_display }}
    </strong>
    <span v-if="copy.due_back" class="right"
      >Book Due Back: {{ copy.due_back }}</span
    >
    <span v-else class="right"></span>
    <p class="small-text grey-text">ID: {{ copy.id }}</p>
  </li>
</template>

<script>
export default {
  name: "CopyListItem",
  props: {
    copy: Object,
  },
};
</script>

<style lang="css" scoped>
.available {
  color: #1b5e20;
}
.maintenance {
  color: #ff6f00;
}
strong {
  color: #b71c1c;
}
p.small-text {
  font-size: small;
}
</style>
