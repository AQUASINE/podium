<script setup lang="ts">
import { ref } from 'vue';

const chance = ref(0.5);
</script>

<template>
  <div class="rule__content">
    <div>
      This rule will match a message with a certain chance, but the chance is seeded by the hash of the message. This means that a message that matches this rule will always match this rule.
    </div>
    <input type="number" class="input__length" id="chance" min="0" max="1" v-model="chance"/>
  </div>
</template>

<style scoped>

</style>