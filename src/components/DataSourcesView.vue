<script setup>

</script>

<template>
  <h1>Data Sources</h1>
  <div v-for="dataSource in dataSources">
    <div>
      <v-icon :icon="dataSource.icon"></v-icon>
      {{ dataSource.type }}
    </div>
  </div>
</template>

<style scoped>

</style>