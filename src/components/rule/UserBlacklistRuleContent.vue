<script setup lang="ts">
import {computed, ref} from 'vue';

const blacklist = ref('');
const blacklistedUsers = computed(() => blacklist.value.split('\n').map(u => u.trim()).filter(u => u.length > 0));
</script>

<template>
  Matches messages for users that are not in the blacklist. Insert each blacklisted username on a new line.
<v-textarea v-model="blacklist" label="Blacklist" outlined dense></v-textarea>

</template>

<style scoped>

</style>