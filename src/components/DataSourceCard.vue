<template>
  <div class="container__data-card">
    <div class="container__data-card-header">
      <div class="info__connected-name">
        <v-icon :icon="typeIcon"></v-icon>
        {{ name }}
        <v-icon icon="mdi-pencil" class="icon__pencil"></v-icon>
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
      <input type="number" class="input__starting-score" v-model="startingScore"/>
    </div>
    <div class="container__identify-tags">
      Generated Tags:
      <InlineTag v-for="tag in generatedTags" :text="tag"></InlineTag>
    </div>
  </div>
</template>
<script setup>
import InlineTag from "./InlineTag.vue";
import {computed, ref} from "vue";

const props = defineProps({
  source: {
    type: Object,
    required: true
  }
})

const startingScore = ref(props.source.startingScore);
const type = ref(props.source.type);
const name = ref(props.source.name);

const typeIcon = computed(() => {
  if (type.value === 'ttv') {
    return 'mdi-twitch';
  } else if (type.value === 'youtube') {
    return 'mdi-youtube';
  }
  return 'mdi-help';
})

const generatedTags = computed(() => {
  if (type.value === 'ttv') {
    return ['ttv', `ttv:${name.value.toLowerCase()}`];
  } else if (type.value === 'youtube') {
    return ['yt', `yt:${name.value.toLowerCase()}`];
  }
})


</script>
<style>

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
  display: flex;
  align-items: center;
  gap: 0.25rem;
  color: var(--text-mute);
  font-size: 0.85em;
  font-weight: 500;
}

.input__starting-score {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 50px;
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

.info__connected-name {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 1em;
  font-weight: 500;
}
</style>