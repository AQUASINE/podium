<template>
  <div class="card__rule-component">
    <div class="header__row-name">
      <h1>{{ title }}</h1>
      <v-icon icon="mdi-pencil"></v-icon>
    </div>
    <div class="item__description">
      {{ description }}
    </div>
    <div class="container__config-content">
      <RegexRuleContent v-if="type === 'regex'"/>
      <DefaultRuleContent v-else/>
    </div>
  </div>
</template>
<script setup>
import {defineProps} from 'vue';
import DefaultRuleContent from "./DefaultRuleContent.vue";
import RegexRuleContent from "./RegexRuleContent.vue";

const props = defineProps({
  title: {
    type: String,
    required: true
  },
  description: {
    type: String,
    default: 'No description provided.'
  },
  type: {
    type: String,
    default: 'default'
  }
})

</script>
<style scoped>

.item__description {
  font-size: 0.85em;
  margin-top: 0.5rem;
  font-weight: 500;
}

.card__rule-component {
  font-size: 1em;
  padding: 0.75rem;
  border-radius: 0.25rem;
  background-color: var(--bg3);
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 0.6rem;
}

.container__config-content {
  margin-top: 0.5rem;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}
</style>