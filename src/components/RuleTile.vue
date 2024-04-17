<template>
  <div class="tile__rule" draggable="false">
    <div class="row__rule">
      <div class="tile__rule-header" @click="toggleExpanded">
        <div class="handle__rule-tile">
          <v-icon icon="mdi-drag"></v-icon>
        </div>
        <div class="divider__tile-vert"></div>
        <div class="container__tile-info" v-if="conditionInfo">
          <span class="strong__rule-tile">IF </span>
          <span>{{ conditionInfo?.name }}</span>
          <span class="strong__rule-tile">THEN </span>
          <span>{{ actionInfo?.name }}</span>
        </div>
        <div class="container__tile-info" v-else>
          <span class="strong__rule-tile">DO </span>
          <span>{{ actionInfo?.name }}</span>
        </div>
        <v-icon :icon="!expanded ? 'mdi-chevron-right' : 'mdi-chevron-down'"></v-icon>
      </div>
    </div>
    <div v-if="expanded" class="container__rule-details">
      <div class="row__rule-details-header">
        <h2>IF</h2>
        <RuleSelectAutocomplete label="Condition Type" v-model="condition" :items="conditionTypes"/>
      </div>
      <RuleConfigWrapper :rule="condition" :rule-info="conditionInfo"/>
      <div class="row__rule-details-header">
        <h2>THEN</h2>
        <RuleSelectAutocomplete label="Action Type" v-model="action" :items="actionTypes"/>
      </div>
      <RuleConfigWrapper :rule="action" :rule-info="actionInfo"/>
    </div>
  </div>
</template>
<script setup>
import {computed, ref} from "vue";
import {actionTypes, conditionTypes} from "../rules.js";
import RuleSelectAutocomplete from "./RuleSelectAutocomplete.vue";
import RuleConfigWrapper from "./RuleConfigWrapper.vue";


const props = defineProps({
  rule: {
    type: Object,
    required: true
  }
})


const expanded = ref(false);
const rule = ref(props.rule);

const action = ref(rule.value.action.name);

const condition = ref(rule.value.condition);

const actionInfo = computed(() => {
  return actionTypes.find(a => a.id === action.value);
})

const conditionInfo = computed(() => {
  return conditionTypes.find(c => c.id === condition.value);
})

const ruleText = computed(() => {
  if (condition.value) {
    return `IF ${condition.value} THEN ${action.value.name}`;
  } else {
    return `DO ${action.value.name}`;
  }
})

const toggleExpanded = () => {
  expanded.value = !expanded.value;
}

</script>
<style>


input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.tile__rule {
  background-color: var(--bg4);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
  font-size: 0.85rem;
}

.row__rule {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.handle__rule-tile {
  cursor: pointer;
  transition: color 0.15s;
  color: var(--text-mute);
}

.handle__rule-tile:hover {
  color: var(--text);
}

.divider__tile-vert {
  border-left: 1px solid white;
  height: 100%;
  margin-left: 0.5rem;
}

.container__tile-info {
  flex: 1;
}

.strong__rule-tile {
  font-weight: 900;
  color: var(--text-mute);
  margin-right: 0.25rem;
  margin-left: 0.25rem;
}

.strong__rule-tile:first-child {
  margin-left: 0;
}

.tile__rule-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.container__rule-details {
  margin-top: 0.75rem;
  padding: 0 0.5rem;
}

.container__rule-details h2 {
  font-size: 1.5em;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

.item__rule-option-title {
  font-size: 0.95em;
  font-weight: 700;
}
</style>