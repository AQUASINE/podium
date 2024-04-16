<template>
  <div class="tile__rule">
    <div class="row__rule">
      <div class="tile__rule-header">
        <div class="handle__rule-tile">
          <v-icon icon="mdi-drag"></v-icon>
        </div>
        <div class="divider__tile-vert"></div>
        <div class="container__tile-info">
          <span class="strong__rule-tile">DO </span>
          <span>{{ action.name }}</span>
        </div>
        <v-icon :icon="!expanded ? 'mdi-chevron-right' : 'mdi-chevron-down'" @click="toggleExpanded"></v-icon>
      </div>
    </div>
    <div v-if="expanded" class="container__rule-details">
      <div class="row__rule-details-header">
        <h2>IF</h2>
        <v-autocomplete v-model="condition" :items="conditionTypes" item-text="name" item-value="id"
                        label="Condition Type" outlined></v-autocomplete>
      </div>
      <div class="container__rule-action">
        <RegexConfigCard/>
      </div>
      <div class="row__rule-details-header">
        <h2>THEN</h2>
        <v-autocomplete v-model="action" :items="actionTypes" item-title="name" item-value="id" label="Action Type"
                        outlined>

        </v-autocomplete>
      </div>
      <div class="container__rule-condition">
        <RegexConfigCard/>
      </div>
    </div>
  </div>
</template>
<script setup>
import {computed, ref} from "vue";
import RegexConfigCard from "./RegexConfigCard.vue";


const props = defineProps({
  rule: {
    type: Object,
    required: true
  }
})

const conditionTypes = [
  {
    id: 'none',
    name: 'Always',
    description: "Match all messages.",
  },
  {
    id: 'contains',
    name: 'Contains',
    description: "Match messages that contain a specific string.",
  },
  {
    id: 'exactMatch',
    name: 'Exact Match',
    description: "Match messages that are exactly the same as a specific string.",
  },
  {
    id: 'fuzzyMatch',
    name: 'Fuzzy Match',
    description: "Match messages that are similar to a specific string.",
  },
  {
    id: 'regex',
    name: 'Regex',
    description: "Match messages with a specific regex pattern.",
  },
  {
    id: 'length',
    name: 'Message Length',
    description: "Match messages based on how long they are.",
  },
  {
    id: 'score',
    name: 'Current Message Score',
    description: "Match messages based on the message's current score.",
  },
  {
    id: 'userscore',
    name: 'User Score',
    description: "Match messages based on the user's score.",
  },
  {
    id: 'userblacklist',
    name: 'User Blacklist',
    description: "Match messages from users on a blacklist.",
  },
  {
    id: 'userwhitelist',
    name: 'User Whitelist',
    description: "Match messages from users on a whitelist.",
  }
]

const actionTypes = [
  {
    id: 'nothing',
    name: 'Do Nothing',
    description: "Simply pass the message through without any modifications.",
  },
  {
    id: 'replace',
    name: 'Simple Replace',
    description: "Replace a specific string with another string.",
  },
  {
    id: 'regex',
    name: 'Regex Replace',
    description: "Replace a string using a regular expression.",
  },
  {
    id: 'drop',
    name: 'Drop Message',
    description: "Drop the message and do not pass it through.",
  },
  {
    id: 'set',
    name: 'Set Score',
    description: "Set the score of the message to a specific value.",
  },
  {
    id: 'math',
    name: 'Math',
    description: "Modify message or user score using math operations.",
    matchingKeywords: ['add', 'subtract', 'multiply', 'divide', 'modulo', 'power', 'root', 'function']
  },
  {
    id: 'add',
    name: 'Add to Score',
    description: "A simple way to add or subtract from the message or user score.",
  },
  {
    id: 'addtag',
    name: 'Add Tag',
    description: "Add a tag to the message or user.",
  },
  {
    id: 'removetag',
    name: 'Remove Tag',
    description: "Remove a tag from the message or user.",
  },
  {
    id: '7tvremove',
    name: 'Remove 7TV emotes',
    description: "Remove 7TV emotes from the message.",
  }
]

const expanded = ref(false);
const rule = ref(props.rule);

const action = ref(rule.value.action ?? {
  name: 'nothing',
  type: 'none'
});

const condition = ref(rule.value.condition);

const ruleText = computed(() => {
  if (condition.value) {
    return `IF ${condition.value} THEN ${action.value.name}`;
  } else {
    return `DO ${action.value.name}`;
  }
})

const toggleExpanded = () => {
  expanded.value = !expanded.value;
}

</script>
<style>


input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

.tile__rule {
  background-color: var(--bg4);
  padding: 0.5rem;
  border-radius: 0.25rem;
  margin-bottom: 0.5rem;
  font-size: 0.85rem;
}

.row__rule {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.handle__rule-tile {
  cursor: pointer;
  transition: color 0.15s;
  color: var(--text-mute);
}

.handle__rule-tile:hover {
  color: var(--text);
}

.divider__tile-vert {
  border-left: 1px solid white;
  height: 100%;
  margin-left: 0.5rem;
}

.container__tile-info {
  flex: 1;
}

.strong__rule-tile {
  font-weight: 900;
  color: var(--text-mute);
}

.tile__rule-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}

.container__rule-details {
  margin-top: 0.75rem;
  padding: 0 0.5rem;
}

.container__rule-details h2 {
  font-size: 1.5em;
  margin-bottom: 0.5rem;
  font-weight: 800;
}
</style>