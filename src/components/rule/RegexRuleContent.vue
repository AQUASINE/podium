<template>
  <div>
    <div>
      This will check each message to see if it matches the following regex:
    </div>
    <input type="text" v-model="regex" class="input__regex" placeholder="Regex..." @input="validateRegex"/>
    <div class="info__valid">
      <div v-if="!valid" class="error__valid">
        <v-icon icon="mdi-close"/>
        Invalid regex
      </div>
      <div v-else class="success__valid">
        <v-icon icon="mdi-check"/>
        Valid regex
      </div>
    </div>
    <div class="note__regex">
      Note: This is Python syntax regex. We recommend using <a href="https://regex101.com/" target="_blank">regex101.com</a> to test your regex.
    </div>
  </div>
</template>
<script setup>
import {ref} from "vue";

const regex = ref('/hello/');
const valid = ref(true);

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
  background-color: var(--bg2);
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

.error__valid {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-mute);
  margin-top: 0.5rem;
}

.success__valid {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: var(--text-mute);
  margin-top: 0.5rem;
}

.note__regex {
  font-size: 0.95em;
  color: var(--text-mute);
  margin-top: 0.5rem;
}
</style>