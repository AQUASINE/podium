<template>
  <div class="tile__rule">
    <div class="row__rule">
      <div class="tile__rule-header" @click="toggleExpanded">
        <div class="handle__rule-tile">
          <v-icon icon="mdi-drag"></v-icon>
        </div>
        <div class="divider__tile-vert"></div>
        <div class="container__tile-info">
          <span class="strong__rule-tile">DO </span>
          <span>{{ action.name }}</span>
        </div>
        <v-icon :icon="!expanded ? 'mdi-chevron-right' : 'mdi-chevron-down'"></v-icon>
      </div>
    </div>
    <div v-if="expanded" class="container__rule-details">
      <div class="row__rule-details-header">
        <h2>IF</h2>
        <v-autocomplete v-model="condition" :items="conditionTypes" item-title="name" item-value="id"
                        label="Condition Type" outlined>
          <template v-slot:item="{props, item}">
            <v-list-item class="item__rule-option" :title="item.title" :subtitle="item.raw.description" v-bind="props">
            </v-list-item>
          </template>
        </v-autocomplete>
      </div>
      <div class="container__rule-action">
        <RuleConfigCard v-if="conditionInfo" :title="conditionInfo.name" :description="conditionInfo.description"
                        :type="condition">
        </RuleConfigCard>
        <div v-else>
          <RuleConfigCard title="Error" :description="'Could not find rule of type ' + condition" type="'default'">
          </RuleConfigCard>
        </div>

      </div>
      <div class="row__rule-details-header">
        <h2>THEN</h2>
        <v-autocomplete v-model="action" :items="actionTypes" item-title="name" item-value="id" label="Action Type"
                        outlined>

        </v-autocomplete>
      </div>
      <div class="container__rule-condition">
      </div>
    </div>
  </div>
</template>
<script setup>
import {computed, ref} from "vue";
import RegexConfigCard from "./rule/RegexRuleContent.vue";
import {conditionTypes, actionTypes} from "../rules.js";
import RuleConfigCard from "./RuleConfigCard.vue";


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
  return actionTypes.find(a => a.id === action.value.id);
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