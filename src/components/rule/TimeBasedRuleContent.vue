<script setup lang="ts">
import {ref} from "vue";

const time = ref(1.0);
</script>

<template>
<div>
  This rule will match a message once every {{ time }} seconds. This means that it will match the first message that comes in after the time has passed.
  <input type="number" v-model="time" class="input__length" id="time"/>
</div>
</template>

<style scoped>

</style>