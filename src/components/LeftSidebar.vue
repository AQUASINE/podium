<template>
  <div class="container__left-sidebar">
    <div>
    <div class="container__daemon-info">
      <div class="indic__daemon" :class="{disconnected: !connected}"></div>
      <div v-if="connected">
        <div>
          Connected to daemon at
        </div>
        <div>
          <code>{{ connectionString }}</code>
        </div>
      </div>
      <div v-else>
        Not connected to daemon
      </div>
    </div>
    <div class="container__configurations-list">
      <div class="row__config-list-header">
        <h2>Configurations</h2>
        <div class="container__config-icons">
          <v-icon icon="mdi-import" class="icon__config-import"></v-icon>
          <v-icon icon="mdi-export" class="icon__config-export"></v-icon>
        </div>
      </div>
      <div class="container__configuration-items">
        <div class="item__configuration" v-for="i in 5" :class="{selected: i === 2}">
          <div>
          Configuration {{ i }}
          </div>
          <v-icon icon="mdi-check-circle" v-if="i === 2" class="icon__running"/>
        </div>
        <div class="item__add-config">
          <v-icon icon="mdi-plus"/>
          Add Configuration
        </div>
      </div>
    </div>
    </div>
    <div>
      <div class="container__authorizations">
        <div class="list__authorizations">
        <div class="item__authorization">
          <img class="pfp__auth" src="https://avatars.githubusercontent.com/u/42610534" alt="avatar"/>
          <v-icon icon="mdi-twitch"></v-icon>
          AQUASINE
        </div>
        </div>
      </div>
    <div class="button__settings">
      <v-icon icon="mdi-cog"></v-icon>
      Settings
    </div>
    </div>
  </div>
</template>
<script setup>
import {computed, ref} from "vue";
import {useStore} from "vuex";

const store = useStore();
const connectionString = computed(() => store.state.connectionString);
const connected = computed(() => store.state.isConnected);

</script>
<style>

.container__left-sidebar {
  background-color: var(--bg1);
  height: 100%;
  width: 200px;
  gap: 1rem;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  text-align: left;
}

.container__daemon-info {
  font-size: 0.8em;
  padding: 0.75rem;
  text-align: left;
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.indic__daemon {
  background-color: var(--primary);
  border-radius: 50%;
  display: inline-block;
  height: 10px;
  margin-right: 5px;
  width: 10px;
  min-width: 10px;
  min-height: 10px;
}

.disconnected {
  background-color: var(--primary-dark);
}

.container__configurations-list {
  padding: 0 0.75rem 0.75rem;
  text-align: left;
}

.container__configurations-list h2 {
  font-size: 1em;
  margin: 0;
  font-weight: 500;
}

.row__config-list-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.icon__config-import,
.icon__config-export {
  font-size: 1.5em;
  cursor: pointer;
}

.container__config-icons {
  display: flex;
  gap: 0.2rem;
}

.item__configuration {
  background-color: var(--bg2);
  border-radius: 4px;
  cursor: pointer;
  margin-bottom: 0.3rem;
  font-size: 0.8em;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.5rem 0.8rem 0.5rem 0.5rem;
  gap: 0.25rem;
}

.item__add-config {
  background-color: var(--bg1);
  border-radius: 4px;
  cursor: pointer;
  padding: 0.5rem;
  margin-bottom: 0.3rem;
  font-size: 0.8em;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  transition: background-color 0.1s;
}

.item__add-config:hover {
  background-color: var(--bg3);
}

.container__authorizations {
  background-color: var(--bg2);
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.8em;
  display: flex;
  flex-direction: column;
  height: 90px;
  align-items: start;
  gap: 0.25rem;

  margin: 0 0.75rem 0.25rem;
}

.container__authorizations h2 {
  padding: 0.5rem;
}

.pfp__auth {
  border-radius: 50%;
  height: 30px;
  width: 30px;
  min-width: 30px;
  min-height: 30px;
  background-color: var(--bg1);
}

.list__authorizations {
  flex: 1;
  overflow-y: auto;
  padding-top: 0.25rem;
}

.item__authorization {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0.5rem;
  cursor: pointer;
  transition: background-color 0.1s;
}

.button__settings {
  background-color: var(--bg2);
  border-radius: 4px;
  cursor: pointer;
  padding: 0.5rem;
  margin: 0 0.75rem 0.75rem;
  font-size: 0.8em;
  display: flex;
  align-items: center;
  gap: 0.25rem;
  transition: background-color 0.1s;
}

.icon__running {
  color: var(--primary-light);
}
</style>