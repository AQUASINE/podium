<script setup lang="ts">
import {computed, ref} from "vue";

const n = ref(2);
const percentage = computed(() => (100 / n.value).toPrecision(2));
</script>

<template>
  <div>
    This will match every 1/{{ n }} messages sent ({{ percentage }}%).
  </div>
  <input type="number" v-model="n" class="input__length" id="nth"/>
</template>

<style scoped>

</style>