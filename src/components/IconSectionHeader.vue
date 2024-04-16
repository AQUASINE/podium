<template>
  <div class="container__section-header">
    <v-icon :icon="icon"></v-icon>
    <slot/>
  </div>
</template>
<script setup>
import { defineProps } from 'vue';

const props = defineProps({
  icon: {
    type: String,
    required: true
  }
})
</script>
<style>


.container__section-header {
  font-size: 0.9em;
  font-weight: 600;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

.container__section-header:first-child {
  margin-top: 0.25rem;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

</style>