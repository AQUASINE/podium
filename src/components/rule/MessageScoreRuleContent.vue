<script setup lang="ts">
import {comparisonOperators} from "../../rules";
import {ref} from "vue";

const operator = ref(comparisonOperators[0].id);
const score = ref(1);
</script>

<template>
  <div>
    Use a comparison operator to check the message's current score.
  </div>
  <v-autocomplete
      v-model="operator"
      :items="comparisonOperators"
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
  <input type="number" v-model="score" class="input__length"/>
</template>

<style scoped>

</style>