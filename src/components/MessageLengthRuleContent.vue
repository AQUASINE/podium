<script setup lang="ts">
import {extendedComparisonOperators} from "../rules";
import {computed, ref} from "vue";

const operator = ref(extendedComparisonOperators[0].id);
const length = ref(1);
const distance = ref(3);
const center = ref(5);

const operatorText = computed(() => {
  const operatorInfo = extendedComparisonOperators.find(o => o.id === operator.value);
  return operatorInfo ? operatorInfo.name.toLowerCase() : '';
})

const isOperationDistance = computed(() => {
  return operator.value === 'dist >' || operator.value === 'dist <';
})

const validateLength = () => {
  length.value = Math.floor(length.value);
  if (length.value < 1) {
    length.value = 1;
  }
  if (length.value > 1000) {
    length.value = 1000;
  }
}

const validateDistance = () => {
  distance.value = Math.floor(distance.value);

  if (distance.value < 1) {
    distance.value = 1;
  }

  if (distance.value > 1000) {
    distance.value = 1000;
  }
}

const validateCenter = () => {
  center.value = Math.floor(center.value);

  if (center.value < 1) {
    center.value = 1;
  }

  if (center.value > 1000) {
    center.value = 1000;
  }
}
const rangeMin = computed(() => {
  let min = center.value - distance.value
  return min < 1 ? 1 : min
});

const rangeMax = computed(() => {
  let max = center.value + distance.value
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
        <input type="number" v-model="distance" @input="validateDistance" min="1" max="1000" class="input__length"/>
        <div>
          centered around
        </div>
        <input type="number" v-model="center" @input="validateDistance" min="1" max="1000" class="input__length"/>
      </div>
      <div class="mt-2">
        <v-icon icon="mdi-information-outline"/> Will range from {{ rangeMin }} to {{ rangeMax }}
      </div>
    </div>
    <input type="number" v-model="length" @input="validateLength" min="1" max="1000" class="input__length" v-else/>
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