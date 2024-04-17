<script setup>
import {ref} from "vue";

const contains = ref('');

</script>

<template>
<div>
  This will check each message to see if it contains the following input:
  <input type="text" v-model="contains" class="input__contains" placeholder="Contains..." />
</div>
</template>

<style scoped>
.input__contains {
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid var(--bg4);
  background-color: var(--bg2);
  font-size: 0.95em;
  margin-top: 0.5rem;
  color: var(--text);
}
</style>