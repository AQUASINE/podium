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
    <div class="container__output-card">
      <div class="item__output-port">
        <v-icon icon="mdi-connection"></v-icon>
        <div class="output__port-name">
          Output Port
        </div>
        <input type="number" class="input__output-port"/>
      </div>
      <div class="item__consume-mode">
        <v-checkbox label="Consume Mode"></v-checkbox>
      </div>
      <div class="item__consume-mode">
        <v-checkbox label="Test"></v-checkbox>
      </div>
    </div>
    <div class="button__save">
      Save
      </div>
  </div>
</template>
<script setup>
import DataSourceCard from "./DataSourceCard.vue";
import {ref} from "vue";
import RulesCard from "./RulesCard.vue";
import IconSectionHeader from "./IconSectionHeader.vue";

const dataSources = ref([
  { name: 'AQUASINE', type: 'ttv', connected: true, startingScore: 100 },
  { name: 'AQUASINE', type: 'youtube', connected: false, startingScore: 100 },
]);

</script>
<style>


.container__configuration-details {
  width: 100%;
}

.container__section-header {
  font-size: 0.9em;
  font-weight: 600;
  margin-bottom: 0.75rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1rem;
}

.container__section-header:first-child {
  margin-top: 0.25rem;
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

.divider__center {
  margin-top: 0.5rem;
  border-top: 1px solid var(--bg3);
  margin-bottom: 0.5rem;
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

.item__consume-mode .v-checkbox {
  font-size: 0.95rem;
  margin-top: -0.5rem;
  margin-bottom: -2rem;
  margin-left: -0.5rem;
}

.item__consume-mode .v-label {
  font-size: 0.85rem;
  color: var(--text) !important;
  opacity: 1;
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