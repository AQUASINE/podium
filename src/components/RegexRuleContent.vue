<template>
  <div class="card__regex">
    <div class="container__regex-input">
      <codemirror v-model="regex" class="input__regex" @input="validateRegex"
                  :extensions="extensions" :options="{lineNumbers: false, theme: 'one-dark'}">
      </codemirror>
    </div>
  </div>
</template>
<script setup>
import {ref} from "vue";
import { Codemirror } from 'vue-codemirror';
import { python } from '@codemirror/lang-python';
import { oneDark } from '@codemirror/theme-one-dark';
import {minimalSetup} from "codemirror";

const regex = ref('/hello/');
const valid = ref(true);

const extensions = [
  python(),
  oneDark,
    minimalSetup
];

const validateRegex = () => {
  try {
    new RegExp(regex.value);
    valid.value = true;
  } catch (e) {
    valid.value = false;
  }

  if (valid.value) {
    console.log('Regex is valid');
  } else {
    console.log('Regex is invalid');
  }

  // highlight input__regex with highlight.js
  const elem = document.querySelector('.input__regex');
  elem.attributes['data-highlighted'] = false
  hljs.highlightElement(elem);
  console.log('highlighted');
}

</script>
<style scoped>

.item__description {
  font-size: 0.85em;
  margin-top: 0.5rem;
  font-weight: 500;
}

.input__regex {
  width: 100%;
  padding: 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid var(--bg4);
  background-color: var(--bg3);
  font-size: 0.85em;
  color: var(--text);
  margin-top: 0.5rem;
}

.input__regex .cm-editor {
  border-radius: 0.25rem;
  background-color: var(--bg2);
}

.card__regex {
  font-size: 1em;
  padding: 0.75rem;
  border-radius: 0.25rem;
  background-color: var(--bg3);
  display: flex;
  flex-direction: column;
  width: 100%;
  margin-bottom: 0.6rem;
}
</style>