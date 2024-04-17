<template>
  <div class="checkbox__compact">
    <v-checkbox :label="label" v-model="model"></v-checkbox>
  </div>
</template>
<script setup>
const props = defineProps({
  label: {
    type: String,
    required: true
  },
});

const model = defineModel();

</script>
<style scoped>
.checkbox__compact {
  display: flex;
  align-items: center;
  justify-content: left;
  font-size: 0.85em;
}

.checkbox__compact >>> .v-checkbox {
  font-size: 0.95rem;
  margin-top: -0.5rem;
  margin-bottom: -2rem;
  margin-left: -0.5rem;
}

.checkbox__compact >>> .v-label {
  font-size: 0.85rem;
  color: var(--text) !important;
  opacity: 1;
}

</style>