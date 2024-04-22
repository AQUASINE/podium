<template>
  <div class="container__middle">
    <div class="tabs__middle">
      <div class="tab__middle" v-for="tab in tabs" :class="{ active: activeTab === tab.name }" @click="handleTabClick(tab.name)">
        <v-icon :icon="tab.icon"></v-icon>
      </div>
    </div>
    <div class="container__middle-main">
      <PrimaryCenterView v-if="activeTab === 'home'"/>
      <PresentationModeCenterView v-else-if="activeTab === 'presentation'"/>
      <SettingsCenterView v-else-if="activeTab === 'settings'"/>
    </div>
  </div>
</template>
<script setup>
import PrimaryCenterView from "../PrimaryCenterView.vue"
import {ref} from "vue";
import PresentationModeCenterView from "../PresentationModeCenterView.vue";
import SettingsCenterView from "../SettingsCenterView.vue";

const tabs = [
  {
    name: 'home',
    icon: 'mdi-home'
  },
  {
    name: 'presentation',
    icon: 'mdi-presentation'
  },
  {
    name: 'settings',
    icon: 'mdi-cog'
  }
]
const activeTab = ref('home');

const handleTabClick = (tabName) => {
  activeTab.value = tabName;
}
</script>
<style>
.container__middle {
  width: 100%;
  background-color: var(--bg2);
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items: center;
  text-align: left;
  overflow: auto;
  max-height: calc(100vh - 3rem);
}

.container__middle-main {
  overflow-y: auto;
  width: 100%;
  display: flex;
  justify-content: center;
}

.tabs__middle {
  display: flex;
  justify-content: left;
  width: 100%;
  padding: 0.35rem;
  border-bottom: 1px solid var(--bg4);
}

.tab__middle {
  font-size: 0.9rem;
  padding: 0.22rem 0.75rem;
  margin-right: 0.5rem;
  cursor: pointer;
  border-radius: 0.25rem;
  color: var(--text);
}

.tab__middle.active {
  background-color: var(--primary-light);
  color: var(--bg1);
}
</style>