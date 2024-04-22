<script setup>
import {ref} from "vue";
import CompactCheckbox from "../CompactCheckbox.vue";

const contains = ref('');
const caseSensitive = ref(false);
const threshold = ref(0.95);

</script>

<template>
<div>
  This will check each message to see if it matches the following input with some flexibility:
  <input type="text" v-model="contains" class="input__contains" placeholder="Contains..." />
  <CompactCheckbox label="Case Sensitive" v-model="caseSensitive"/>
  <div class="info__threshold">
  Choose a threshold that will determine how closely the message must match the input. The default is 0.95, which means the message must be 95% similar to the input.
  </div>
  <label>Threshold: </label>
  <input type="number" v-model="threshold" class="input__threshold" placeholder="Threshold..." />
</div>
</template>

<style scoped>
.input__contains {
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid var(--bg4);
  background-color: var(--bg2);
  margin-top: 0.75rem;
  margin-bottom: 0.25rem;
  color: var(--text);
}

.input__threshold {
  width: 80px;
  padding: 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid var(--bg4);
  background-color: var(--bg2);
  font-size: 0.95em;
  margin-top: 0.5rem;
  color: var(--text);
}

.info__threshold {
  margin-top: 0.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-mute);
}
</style>