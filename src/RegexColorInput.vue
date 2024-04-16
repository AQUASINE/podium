<script setup>
import {ref, watch} from 'vue';


const inputText = ref('');
const highlightedText = ref('');

const highlightSyntax = () => {
  // Regex pattern to identify capture groups
  const captureGroupPattern = /\((?!\?)/g;

  // Check if input text matches regex syntax
  const isValid = validateRegexSyntax(inputText.value);

  // Highlight syntax
  if (isValid) {
    const highlighted = inputText.value.replace(captureGroupPattern, '<span style="color: blue;">$&</span>');
    highlightedText.value = highlighted;
  } else {
    // Highlight invalid syntax in red
    highlightedText.value = `<span style="color: red;">${inputText.value}</span>`;
  }
};

const validateRegexSyntax = (text) => {
  try {
    new RegExp(text);
    return true;
  } catch (error) {
    return false;
  }
};

watch(inputText, highlightSyntax);

</script>

<template>
  <input type="text" v-model="inputText" @input="highlightSyntax" />
  <div v-html="highlightedText"></div>
</template>

<style scoped>

</style>