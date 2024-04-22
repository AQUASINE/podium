<script setup lang="ts">
import {computed, ref} from 'vue';

const whitelist = ref('');
const whitelistedUsers = computed(() => whitelist.value.split('\n').map(u => u.trim()).filter(u => u.length > 0));
</script>

<template>
  Matches messages only for users in the whitelist. Insert each whitelisted username on a new line.
  <v-textarea v-model="whitelist" label="Whitelist" outlined dense></v-textarea>

</template>

<style scoped>

</style>