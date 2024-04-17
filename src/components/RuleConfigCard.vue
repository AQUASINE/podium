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
      <AlwaysRuleContent v-if="type === 'always'"/>
      <RegexRuleContent v-else-if="type === 'regex'"/>
      <ContainsRuleContent v-else-if="type === 'contains'"/>
      <ExactMatchRuleContent v-else-if="type === 'exactMatch'"/>
      <FuzzyMatchRuleContent v-else-if="type === 'fuzzyMatch'"/>
      <MessageLengthRuleContent v-else-if="type === 'length'"/>
      <DefaultRuleContent v-else :type="type"/>
    </div>
  </div>
</template>
<script setup>
import {defineProps} from 'vue';
import DefaultRuleContent from "./rule/DefaultRuleContent.vue";
import RegexRuleContent from "./rule/RegexRuleContent.vue";
import AlwaysRuleContent from "./rule/AlwaysRuleContent.vue";
import ContainsRuleContent from "./rule/ContainsRuleContent.vue";
import ExactMatchRuleContent from "./rule/ExactMatchRuleContent.vue";
import FuzzyMatchRuleContent from "./rule/FuzzyMatchRuleContent.vue";
import MessageLengthRuleContent from "./rule/MessageLengthRuleContent.vue";

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