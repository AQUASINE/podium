<template>
  <div class="container__messages-view">
    <div class="flex container__messages-header">
      <div class="container__message-item text-left flex">
        <div>
          Messages
        </div>
        <v-icon icon="mdi-arrow-down-bold" class="ml-3" @click="toggleLock" :class="{'icon-disable': locked}"/>
        <v-icon :icon="hidden ? 'mdi-eye' : 'mdi-eye-off'" class="ml-3" @click="toggleHidden"/>
      </div>
      <div>
        Score
      </div>
    </div>
    <div class="overflow-y-scroll container__messages">
      <div v-for="message in messages" class="bg3 item__message flex">
        <div class="flex w-full">
          <div class="p-3 container__message-item flex flex-col">
            <div v-if="!hidden">
          <span class="font-bold">
          {{ message.user }}
          </span>: {{ message.message }}
            </div>
            <div v-else>
              <div class="bg4 p-3 rounded-lg">Hidden</div>
            </div>
            <div class="inline-flex flex-wrap">
              <InlineTag v-for="tag in message.tags" :text="tag"></InlineTag>
            </div>
          </div>
          <div class="flex-1 p-3 item__score">
            {{ formatScore(message.weight) }}
          </div>
        </div>
      </div>
    </div>
    <div v-if="messages.length === 0" class="container__no-messages">
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

.item__score {
  background-color: var(--bg3);
}

.container__message-item {
  width: 80%;
}

.container__messages {
  flex: 1;
  background-color: var(--bg3);
  max-height: calc(50vh - 4rem);
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