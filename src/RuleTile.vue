<template>
  <div class="tile__rule">
    <div class="tile__rule-header">
    <div class="handle__rule-tile">
      <v-icon icon="mdi-drag"></v-icon>
    </div>
    <div class="divider__tile-vert"></div>
    <div class="container__tile-info">
      <span class="strong__rule-tile">DO </span>
      <span>{{ action.name }}</span>
    </div>
    <v-icon :icon="expanded ? 'mdi-chevron-right' : 'mdi-chevron-down'" @click="toggleExpanded"></v-icon>
    </div>
  </div>
</template>
<script setup>
import {computed, ref} from "vue";

const props = defineProps({
  rule: {
    type: Object,
    required: true
  }
})

const expanded = ref(false);
const rule = ref(props.rule);

const action = ref(rule.value.action ?? {
  name: 'nothing',
  type: 'none'
});

const condition = ref(rule.value.condition);

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
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
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
</style>