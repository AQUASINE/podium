<template>
  <div class="card__regex-tuning">
    <h1 class="header__card-title">{{ title }}</h1>
    <div class="item__rule_id">Rule ID: {{ ruleId }}</div>
    <div class="item__rule-description">
      {{ description }}
    </div>
    <div>
      <h2>Stats</h2>
      <div>Matches</div>
      <div v-if="!always">
        4 / 50
      </div>
      <div v-else>
        Always
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue';

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  ruleId: {
    type: String,
    required: true
  },
  always: {
    type: Boolean,
    default: false
  },
  description: {
    type: String,
    default: 'No description provided.'
  }
})
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

.card__regex-tuning {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  background-color: var(--bg3);
  width: 100%;
  padding: 0.75rem;
  border-radius: 0.25rem;
}

.header__card-title {
  font-size: 1.5em;
  font-weight: 700;
  margin-bottom: -0.2rem;
}

.item__rule_id {
  font-size: 0.85em;
  font-weight: 500;
  color: var(--text-mute);
}

.item__rule-description {
  font-size: 0.85em;
  font-weight: 500;
  color: var(--text-mute);
}
</style>