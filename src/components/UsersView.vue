<template>
  <div class="container__users-view">
    <div class="flex container__messages-header">
      <div class="container__message-item text-left flex">
        <div class="item__user-title">
          Users
        </div>
        <v-icon :icon="sortIcon" class="ml-3" @click="toggleSortType"/>
        <v-icon :icon="hidden ? 'mdi-eye-off' : 'mdi-eye'" class="ml-3" @click="toggleHidden"/>
      </div>
      <div class="item__user-title">
        Score
      </div>
    </div>
    <div class="overflow-y-scroll container__messages" v-if="!hidden">
      <div v-for="user in sortedUsers" class="bg3 item__message flex">
        <div class="flex w-full">
          <div class="p-3 container__message-item flex flex-col">
            <div v-if="!hidden">
          <span class="font-bold overflow-auto">
          {{ user.user }}
          </span>
            </div>
            <div v-else>
              <div class="text-mute">Hidden</div>
            </div>
            <div class="inline-flex flex-wrap">
              <InlineTag v-if="user.tags" v-for="tag in user.tags" :text="tag"></InlineTag>
            </div>
          </div>
          <div class="flex-1 p-3 item__score">
            {{ formatScore(user.user_score) }}
          </div>
        </div>
      </div>
    </div>
    <div v-if="hidden" class="container__no-messages">
      <v-icon icon="mdi-eye-off" class="mr-2"/>
      Users are hidden
    </div>
    <div v-else-if="users.length === 0" class="container__no-users">
      No users yet
    </div>
  </div>
</template>
<script>
import InlineTag from "./InlineTag.vue";

export default {
  name: 'UsersView',
  components: {InlineTag},
  props: {
    users: {
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
      hidden: false,
      sortAscending: true
    }
  },
  methods: {
    toggleHidden() {
      this.hidden = !this.hidden;
    },
    formatScore(score) {
      // 3 decimal places
      return score.toFixed(3);
    },
    toggleSortType() {
      this.sortAscending = !this.sortAscending;
    }
  },
  computed: {
    sortIcon() {
      return this.sortAscending ? 'mdi-sort-numeric-ascending' : 'mdi-sort-numeric-descending';
    },
    reversedUsers() {
      return this.users.slice().reverse();
    },
    sortedUsers() {
      if (this.sortAscending) {
        return this.users;
      }
      return this.reversedUsers;
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
  width: 80px;
  min-width: 80px;
}

.container__message-item {
  width: 80%;
}

.container__messages {
  flex: 1;
  background-color: var(--bg3);
  max-height: calc(50vh - 4rem);
  overflow-x: hidden;
}

.container__users-view {
  border-left: 1px solid var(--bg4);
  border-top: 1px solid var(--bg4);
  width: 250px;
  flex: 1;
}

.container__messages-header {
  background-color: var(--bg1);
  font-size: 0.85em;
  padding: 0.6rem 0.75rem;
}

.container__no-users {
  color: var(--text-mute);
  margin-top: 1rem;
  padding: 0.5rem;
  text-align: center;
  font-size: 0.85em;
}

.item__user-title {
  font-size: 0.85rem;
}
</style>