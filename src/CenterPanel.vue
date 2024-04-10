<template>
  <div class="container__middle">
    <div class="header__row-name">
      <h1>translation-chatbox-app</h1>
      <v-icon icon="mdi-pencil"></v-icon>
    </div>
    <div class="item__active-indicator">
      ACTIVE
    </div>
    <div class="item__description">
      This is a translation chatbox app that uses the Google Translate API to translate messages in real-time.
    </div>
  </div>
</template>
<script>
export default {
  name: 'CenterPanel'
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
</style>