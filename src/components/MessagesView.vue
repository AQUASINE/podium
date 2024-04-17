<template>
  <div class="container__messages-view">
    <div class="flex container__messages-header">
      <div class="container__message-item text-left flex">
        <div>
          Messages
        </div>
        <v-icon icon="mdi-pause" class="ml-3" @click="toggleLock" :class="{'icon-disable': locked}"/>
        <v-icon :icon="hidden ? 'mdi-eye-off' : 'mdi-eye'" class="ml-3" @click="toggleHidden"/>
        <v-icon :icon="sortIcon" class="ml-3" @click="cycleSortType"/>
      </div>
      <div>
        Score
      </div>
    </div>
    <div class="overflow-y-scroll container__messages">
      <div v-for="message in sortedMessages" class="bg3 item__message flex" v-if="!hidden">
        <div class="flex w-full">
          <div class="p-2 container__message-item flex flex-col">
            <div v-if="!hidden">
          <span class="font-bold">
          {{ message.user }}
          </span>: {{ message.message }}
            </div>
            <div v-else>
              <div class="text-mute rounded-lg">Hidden</div>
            </div>
            <div class="inline-flex flex-wrap">
              <InlineTag v-for="tag in message.tags" :text="tag" compact></InlineTag>
            </div>
          </div>
          <div class="item__score">
            {{ formatScore(message.weight) }}
          </div>
        </div>
      </div>
      <div>
      </div>
    </div>
    <div v-if="hidden" class="container__no-messages">
      <v-icon icon="mdi-eye-off" class="mr-2"/>
      Messages are hidden
    </div>
    <div v-else-if="messages.length === 0" class="container__no-messages">
      No messages yet
    </div>
  </div>
</template>
<script>
import InlineTag from "./InlineTag.vue";

export default {
  name: 'MessagesView',
  components: {InlineTag},
  props: {
    messages: {
      type: Array,
      default: () => []
    }
  },
  watch: {
    messages: {
      handler() {
        if (this.locked) {
          return;
        }
        this.$nextTick(() => {
          const container = this.$el.querySelector('.container__messages');
          container.scrollTop = container.scrollHeight;
        });
      },
      deep: true
    },
  },
  data() {
    return {
      locked: false,
      hidden: false,
      sortType: 'time',
    }
  },
  methods: {
    toggleLock() {
      this.locked = !this.locked;
    },
    toggleHidden() {
      this.hidden = !this.hidden;
    },
    formatScore(score) {
      // 3 decimal places
      return score.toFixed(3);
    },
    cycleSortType() {
      switch (this.sortType) {
        case 'time':
          this.sortType = 'score';
          break;
        case 'score':
          this.sortType = 'score-desc';
          break;
        case 'score-desc':
          this.sortType = 'time';
          break;
        default:
          this.sortType = 'time';
      }
    }
  },
  computed: {
    sortIcon() {
      switch (this.sortType) {
        case 'time':
          return 'mdi-clock';
        case 'score':
          return 'mdi-sort-numeric-ascending';
        case 'score-desc':
          return 'mdi-sort-numeric-descending';
      }
      return 'mdi-help';
    },
    sortedMessages() {
      switch (this.sortType) {
        case 'time':
          return this.messages;
        case 'score':
          return this.messages.slice().sort((a, b) => a.weight - b.weight);
        case 'score-desc':
          return this.messages.slice().sort((a, b) => b.weight - a.weight);
      }
      return this.messages;
    }
  }
}
</script>
<style>
.icon-disable {
  color: var(--bg4) !important;
}

.item__message {
  border-bottom: 1px solid var(--bg4);
  text-align: left;
  max-width: 100%;
  width: 100%;
}

.item__message:last-child {
  border-bottom: none;
}

.item__score {
  background-color: var(--bg2);
  width: 80px;
  min-width: 80px;
  padding: 0.75rem;
  flex: 1;
  font-size: 0.85em;
}

.container__message-item {
  width: 80%;
  font-size: 0.85em;
}

.container__messages {
  flex: 1;
  background-color: var(--bg3);
  max-height: calc(50vh - 4rem);
  overflow-x: hidden;
}

.container__messages-view {
  border-left: 1px solid var(--bg4);
  width: 250px;
  flex: 1;
}

.container__messages-header {
  background-color: var(--bg1);
  font-size: 0.85em;
  padding: 0.6rem 0.75rem;
}

.container__no-messages {
padding: 1rem;
  text-align: center;
  color: var(--text-mute);
  font-size: 0.85em;
}
</style>