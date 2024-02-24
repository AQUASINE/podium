<template>
  <div class="flex-1 container__messages-view">
    <div class="flex">

      <div class="container__message-item text-left p-3 flex">
        <div>
          Messages
        </div>
        <v-icon icon="mdi-arrow-down-bold" class="ml-3" @click="toggleLock" :class="{'icon-disable': locked}"/>
      </div>
      <div class="p-3">
        Score
      </div>
    </div>
    <div class="overflow-y-scroll container__messages">
      <div v-for="message in messages" class="bg3 item__message flex">
        <div class="flex w-full">
          <div class="p-3 container__message-item flex flex-col">
            <div>
          <span class="font-bold">
          {{ message.user }}
          </span>: {{ message.message }}
            </div>
            <div class="inline-flex flex-wrap">
            <span v-for="tag in message.tags"
                  class="bg4 p pr-3 pl-3 mt-2 w-min rounded-full whitespace-nowrap mr-1 text-mute text-xs">
              {{ tag }}
            </span>
            </div>
          </div>
          <div class="flex-1 p-3 item__score">
            {{ formatScore(message.weight) }}
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'MessagesView',
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
      locked: false
    }
  },
  methods: {
    toggleLock() {
      this.locked = !this.locked;
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
  background-color: var(--bg2);
}

select {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 400px;
  max-width: 33vw;
  height: 35px;
  background-color: var(--primary-dark);
  color: #ffffff;
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.25s;
}

select:hover {
  border-color: var(--primary)
}

.container__message-item {
  width: 80%;
}

.container__messages {
  max-height: calc(100vh - 100px);
  height: 100vh;
  background-color: var(--bg2);
}

.container__messages-view {
  border-left: 1px solid var(--bg4);
}
</style>