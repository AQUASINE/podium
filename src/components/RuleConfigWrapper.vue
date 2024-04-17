<template>
  <div class="container__rule-action">
    <div v-if="!ruleInfo || rule === 'always'">
      <RuleConfigCard title="Error" :description="'Could not find rule of type ' + rule" type="'default'">
      </RuleConfigCard>
    </div>
    <RuleConfigCard v-else :title="ruleInfo.name" :description="ruleInfo.description"
                    :type="rule">
    </RuleConfigCard>
  </div>
</template>
<script setup>
import RuleConfigCard from "./RuleConfigCard.vue";

const props = defineProps({
  rule: {
    type: String,
    required: true
  },
  ruleInfo: {
    type: Object,
    required: false
  }
})
</script>
<style>


input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.container__rule-details h2 {
  font-size: 1.5em;
  margin-bottom: 0.5rem;
  font-weight: 800;
}

</style>