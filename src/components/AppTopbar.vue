<template>
  <div class="bg-primary-alt flex width-100 pt-3 pb-3 container__top-bar">
    <div class="flex justify-center items-center pl-3">
      <img src="/podium.svg" alt="Podium Logo" class="logo"/>
      <div class="font-bold pl-2">
        Podium
      </div>
    </div>
    <div class="absolute flex justify-center items-center w-full top-0 pt-2">
      <div class="heading__active-config">
        Active Configuration
      </div>
      <div class="ml-3 container__configuration-select">
        <VueSelect v-bind="activeConfiguration" :options="configurationNames" class="item__configuration-select"></VueSelect>
      </div>
    </div>
  </div>
</template>
<script setup>
import VueSelect from 'vue-select'
import {useStore} from "vuex";
import {computed} from "vue";

const store = useStore();

const configurations = store.state.configurations.configurations;
const activeConfiguration = store.state.configurations.activeConfiguration;
console.log(configurations);
console.log(activeConfiguration);

const configurationNames = computed(() => configurations.map((config) => {
  return config.name
}));

const activeConfigurationId = computed(() => activeConfiguration.id);



</script>
<style>

select {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 400px;
  max-width: 33vw;
  height: 35px;
  background-color: var(--primary-xtra-dark);
  color: #ffffff;
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.25s;
}

select:hover {
  border-color: var(--primary-dark)
}

.container__configuration-select {
  width: 400px;
  max-width: 33vw;
}

.item__configuration-select {
  font-size: 0.9rem;
}

.container__top-bar {
  position: relative;
  width: 100%;
  z-index: 1000;
  background-color: var(--primary-dark) !important;
}

.heading__active-config {
  font-size: 0.95em;
  font-weight: 500;
}

</style>