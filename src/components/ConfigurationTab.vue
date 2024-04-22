<template>
  <div class="container__configuration-details">
    <IconSectionHeader icon="mdi-database">Data Sources</IconSectionHeader>
    <DataSourceCard v-for="source in dataSources" :source="source"/>
    <div class="button__add-data-source">
      <v-icon icon="mdi-plus"></v-icon>
      Add Data Source
    </div>
    <IconSectionHeader icon="mdi-ruler">Rules</IconSectionHeader>
    <RulesCard/>
    <IconSectionHeader icon="mdi-cog">Output</IconSectionHeader>
    <OutputCard :outputPort="outputPort"/>
    <div class="button__save">
      Save
      </div>
  </div>
</template>
<script setup>
import DataSourceCard from "./DataSourceCard.vue";
import {ref} from "vue";
import RulesCard from "./RulesListCard.vue";
import IconSectionHeader from "./IconSectionHeader.vue";
import OutputCard from "./OutputCard.vue";

const dataSources = ref([
  { name: 'AQUASINE', type: 'ttv', connected: true, startingScore: 100 },
  { name: 'AQUASINE', type: 'youtube', connected: false, startingScore: 100 },
]);


</script>
<style scoped>
.container__configuration-details {
  width: 100%;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.button__add-data-source {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem;
  border-radius: 0.25rem;
  background-color: var(--bg3);
  cursor: pointer;
  font-size: 0.8rem;
  color: var(--text-mute);
}



.button__save {
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0.5rem;
  border-radius: 0.25rem;
  background-color: var(--primary);
  color: var(--text);
  cursor: pointer;
  font-size: 0.9rem;
  margin-top: 1rem;
}
</style>