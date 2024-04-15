<template>
  <div class="card__regex">
    <div class="header__row-name">
      <h1>Regex</h1>
      <v-icon icon="mdi-pencil"></v-icon>
    </div>
    <div class="item__description">
      Match messages with a specific regex pattern.
    </div>
    <div class="container__regex-input">
      <highlightjs :code="regex" :language="'regex'"></highlightjs>
    </div>
  </div>
</template>
<script setup>
import 'highlight.js/lib/common';
import hljsVuePlugin from '@highlightjs/vue-plugin';
import {ref} from "vue";


const regex = ref('/hello/');

</script>
<style>


.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.header__row-name {
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
}

.header__row-name h1 {
  font-size: 1.5em;
  margin: 0;
  font-weight: 700;
}

.item__description {
  font-size: 0.85em;
  margin-top: 0.5rem;
  font-weight: 500;
}

</style>