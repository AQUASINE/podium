<template>
  <v-autocomplete v-model="selection" :items="items" item-title="name" item-value="id"
                  :label="label" outlined>
    <template v-slot:item="{props, item}">
      <v-list-item class="item__rule-option" :title="item.title" :subtitle="item.raw.description" v-bind="props">
      </v-list-item>
    </template>
  </v-autocomplete>
</template>
<script setup>
import { ref } from 'vue';

const selection = defineModel()

const props = defineProps({
  label: {
    type: String,
    required: true
  },
  items: {
    type: Array,
    required: true
  },
})


</script>
<style>
</style>