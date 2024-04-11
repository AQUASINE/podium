<template>
  <div class="container__middle">
    <div class="header__row-name">
      <h1>translation-chatbox-app</h1>
      <v-icon icon="mdi-pencil"></v-icon>
    </div>
    <div class="item__active-indicator">
      <v-icon icon="mdi-check"></v-icon>
      ACTIVE
    </div>
    <div class="item__description">
      This is a translation chatbox app that uses the Google Translate API to translate messages in real-time.
    </div>
    <div class="container__tab-panel">
      <div class="container__tab-row">
        <div class="item__tab">
          <v-icon icon="mdi-wrench"></v-icon>
        </div>
        <div class="item__tab">
          <v-icon icon="mdi-tune"></v-icon>
        </div>
      </div>
      <ConfigurationTab/>
    </div>
  </div>
</template>
<script>
import ConfigurationTab from "./ConfigurationTab.vue";

export default {
  name: 'CenterPanel',
  components: {ConfigurationTab}
}
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
  background-color: var(--primary-dark);
  color: #ffffff;
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.25s;
}

select:hover {
  border-color: var(--primary)
}

.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.container__middle {
  width: 100%;
  background-color: var(--bg2);
  display: flex;
  flex-direction: column;
  justify-content: left;
  align-items: start;
  padding: 1rem;
  text-align: left;
  overflow: auto;
  max-height: calc(100vh - 3rem);
}

.header__row-name {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
}

.header__row-name h1 {
  font-size: 1.5em;
  margin: 0;
  font-weight: 700;
}

.item__active-indicator {
  color: var(--primary);
  margin-top: 0.25rem;
  font-size: 0.85em;
  font-weight: 800;
  border-radius: 0.25rem;
}

.item__description {
  font-size: 0.85em;
  margin-top: 0.5rem;
  font-weight: 500;
}

.container__tab-row {
  display: flex;
  margin-top: 1rem;
  border-bottom: 1px solid var(--bg4);
  width: 100%;
}

.item__tab {
  font-size: 0.75em;
  cursor: pointer;
  border: 1px solid var(--bg4);
  border-right: none;
  border-bottom: none;
  padding: 0.4rem 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.item__tab:last-child {
  border-right: 1px solid var(--bg4);
  border-top-right-radius: 0.25rem;
}

.item__tab:first-child {
  border-top-left-radius: 0.25rem;
}

.container__tab-panel {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  align-items: start;
  gap: 0.5rem;
}

</style>