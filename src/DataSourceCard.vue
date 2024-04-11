<template>
  <div class="container__data-card">
    <div class="container__data-card-header">
      <div>
        <v-icon icon="mdi-twitch"></v-icon>
        AQUASINE
      </div>
      <div class="info__connected-indic">
        <v-icon icon="mdi-check"></v-icon>
        Connected
      </div>
    </div>
    <div class="container__start-score">
      <div class="info__starting-score">
        Starting Score
      </div>
      <input type="number" class="input__starting-score">
    </div>
    <div class="container__identify-tags">
      Generated Tags:
      <InlineTag>ttv</InlineTag>
      <InlineTag>ttv:aquasine</InlineTag>
    </div>
  </div>
</template>
<script>
import InlineTag from "./InlineTag.vue"

export default {
  name: 'DataSourceCard',
  components: {InlineTag}
}
</script>
<style>

.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.header__row-name h1 {
  font-size: 1.5em;
  margin: 0;
  font-weight: 700;
}

.container__data-card {
  font-size: 0.85em;
  padding: 0.75rem;
  border-radius: 0.25rem;
  background-color: var(--bg3);
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 0.6rem;
}

.container__data-card-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 0.5rem;
}

.info__connected-indic {
  color: var(--text-mute);
  font-size: 0.85em;
  font-weight: 500;
}

.input__starting-score {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 60px;
  max-width: 33vw;
  height: 30px;
  background-color: var(--bg2);
  text-align: center;
  border: 1px solid transparent;
  transition: border-color 0.25s;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.container__start-score {
  display: flex;
  justify-content: start;
  align-items: center;
  gap: 0.5rem;
}

.container__identify-tags {
  font-size: 0.85em;
  color: var(--text-mute);
  margin-top: 0.75rem;
}
</style>