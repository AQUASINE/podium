<template>
  <div class="container__output-card">
    <div class="item__output-port">
      <v-icon icon="mdi-connection"></v-icon>
      <div class="output__port-name">
        Output Port
      </div>
      <input type="number" class="input__output-port" v-model="outputPort"/>
    </div>
    <CompactCheckbox v-model="consumeMode" label="Consume Mode"/>
    <CompactCheckbox v-model="logToFile" label="Log to file"/>
  </div>
</template>
<script setup>
import {ref} from "vue";
import CompactCheckbox from "./CompactCheckbox.vue";

const outputPort = ref(8765);
const consumeMode = ref(false);
const logToFile = ref(false);

</script>
<style scoped>


input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.container__output-card {
  background-color: var(--bg3);
  padding: 0.75rem;
  border-radius: 0.25rem;
}

.item__output-port {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.85em;
  margin-bottom: 0.5rem;
}

.item__output-port .input__output-port {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 50px;
  height: 30px;
  background-color: var(--bg2);
  text-align: center;
  border: 1px solid transparent;
  transition: border-color 0.25s;
}

.item__consume-mode {
  display: flex;
  align-items: center;
  justify-content: left;
  font-size: 0.85em;
}

</style>