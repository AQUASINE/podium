<template>
  <div class="container__rules-card">
    <div class="hint__rules">
      Rules are used to determine how data is processed and tagged. They are applied in order from top to bottom.
    </div>
    <div class="tile__rule-static start">
      <i>
        Start
      </i>
    </div>
    <RuleTile :rule="testRule"/>
    <div class="button__add-rule">
      <v-icon icon="mdi-plus"></v-icon>
      Add Rule
    </div>
    <div class="tile__rule-static end">
      <i>
        End
      </i>
    </div>
  </div>
</template>
<script setup>
import RuleTile from "./RuleTile.vue";

const testRule = {
  condition: {
    type: 'none',
    name: 'nothing'
  },
  action: {
    type: 'none',
    name: 'nothing'
  }
}
</script>
<style>


input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.button__add-rule {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.1rem 0.5rem 0.5rem;
  border-radius: 0.25rem;
  background-color: var(--bg3);
  cursor: pointer;
  font-size: 0.8rem;
  color: var(--text-mute);
  margin-bottom: 0.25rem;
}

.hint__rules {
  font-size: 0.8rem;
  margin-bottom: 0.5rem;
  color: var(--text-mute);
  font-style: italic;
}

.container__rules-card {
  background-color: var(--bg3);
  padding: 0.75rem;
  border-radius: 0.25rem;

}

.tile__rule-static {
  background-color: var(--bg3);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.85rem;
  font-style: italic;
  color: var(--text-mute);
  border: 1px solid var(--bg4);
}

.tile__rule-static.start {
  user-select: none;
}

.tile__rule-static.end {
  user-select: none;
}

</style>