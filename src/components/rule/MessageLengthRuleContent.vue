<script setup lang="ts">
import {extendedComparisonOperators} from "../../rules";
import {computed, ref} from "vue";
import {useMessageLengthValidator} from "../../utils";

const operator = ref(extendedComparisonOperators[0].id);
const length = useMessageLengthValidator(1);
const distance = useMessageLengthValidator(3);
const center = useMessageLengthValidator(5);

const operatorText = computed(() => {
  const operatorInfo = extendedComparisonOperators.find(o => o.id === operator.value);
  return operatorInfo ? operatorInfo.name.toLowerCase() : '';
})

const isOperationDistance = computed(() => {
  return operator.value === 'dist >' || operator.value === 'dist <';
})

const rangeMin = computed(() => {
  let min = center.value.value - distance.value.value
  return min < 1 ? 1 : min
});

const rangeMax = computed(() => {
  let max = center.value.value + distance.value.value
  return max > 1000 ? 1000 : max
})


</script>

<template>
  <div>
    Use a comparison operator to check the length of each message.
  </div>
  <v-autocomplete
      v-model="operator"
      :items="extendedComparisonOperators"
      item-title="id"
      item-value="id"
      label="Operator"
      dense
      outlined
  >
    <template v-slot:item="{ props, item }">
      <v-list-item class="item__rule-option" :title="item.id" :subtitle="item.raw.name" v-bind="props">
      </v-list-item>
    </template>
  </v-autocomplete>
  <div class="info__length-match">
    Match messages <strong class="info__operator">{{ operatorText }}</strong> length:
    <div v-if="isOperationDistance" class="mt-2">
      <div class="ga-1 flex align-center">
        <input type="number" v-model="distance.value" @input="distance.validate" min="1" max="1000" class="input__length"/>
        <div>
          centered around
        </div>
        <input type="number" v-model="center.value" @input="center.validate" min="1" max="1000" class="input__length"/>
      </div>
      <div class="mt-2">
        <v-icon icon="mdi-information-outline"/> Will range from {{ rangeMin }} to {{ rangeMax }}
      </div>
    </div>
    <input type="number" v-model="length.value" @input="length.validate" min="1" max="1000" class="input__length" v-else/>
  </div>
</template>

<style scoped>
.info__operator {
  font-weight: bold;
  color: var(--text);
}

.info__length-match {
  margin-top: -0.5rem;
  margin-bottom: 0.25rem;
  color: var(--text-mute);
}

.input__length {
  color: var(--text);
}
</style>