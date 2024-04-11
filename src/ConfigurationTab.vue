<template>
  <div class="container__configuration-details">
    <div class="container__section-header">
      <v-icon icon="mdi-database"></v-icon>
      Data Sources
    </div>
    <DataSourceCard/>
    <DataSourceCard/>
    <div class="button__add-data-source">
      <v-icon icon="mdi-plus"></v-icon>
      Add Data Source
    </div>
    <div class="divider__center"></div>
    <div class="container__rules-card">
      <div class="container__section-header">
        <v-icon icon="mdi-ruler"></v-icon>
        Rules
      </div>
      <div class="hint__rules">
        Rules are used to determine how data is processed and tagged. They are applied in order from top to bottom.
      </div>
      <div class="tile__rule-static">
        <i>
          Start
        </i>
      </div>
      <div class="tile__rule">
        <div class="handle__rule-tile">
          <v-icon icon="mdi-drag"></v-icon>
        </div>
      </div>
      <div class="button__add-data-source">
        <v-icon icon="mdi-plus"></v-icon>
        Add Rule
      </div>
    </div>
  </div>
</template>
<script>
import DataSourceCard from "./DataSourceCard.vue";

export default {
  name: 'ConfigurationTab',
  components: {DataSourceCard}
}
</script>
<style>


.container__configuration-details {
  width: 100%;
}

.container__section-header {
  font-size: 0.9em;
  font-weight: 600;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
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
}

.hint__rules {
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
  color: var(--text-mute);
}

.container__rules-card {
  background-color: var(--bg3);
  padding: 0.75rem;
  border-radius: 0.25rem;

}

.divider__center {
  margin-top: 0.5rem;
  border-top: 1px solid var(--bg3);
  margin-bottom: 0.5rem;
}

.tile__rule {
  background-color: var(--bg4);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
}

.tile__rule-static {
  background-color: var(--bg3);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
  font-style: italic;
  color: var(--text-mute);
  border: 1px solid var(--bg4);
}
</style>