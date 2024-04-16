<template>
  <div class="container__app">
    <AppTopbar/>
    <div class="flex flex-1">
      <div class="flex-1">
        <LeftSidebar/>
      </div>
      <CenterPanel/>
      <div class="container__right-sidebar">
        <MessagesView :messages="messages"/>
        <UsersView :users="users"/>
      </div>
    </div>
  </div>
</template>

<script>


import MessagesView from "./MessagesView.vue";
import LeftSidebar from "./LeftSidebar.vue";
import CenterPanel from "./CenterPanel.vue";
import UsersView from "./UsersView.vue";
import {mapState} from "vuex";
import AppTopbar from "./AppTopbar.vue";

export default {
  name: 'App',
  components: {AppTopbar, UsersView, CenterPanel, LeftSidebar, MessagesView},
  async mounted() {
    window.addEventListener('resize', this.handleResize);
    await this.$store.dispatch('getMessages');
  },
  computed: {
    ...mapState(['messages', 'users'])
  },
  methods: {
    handleResize() {
      this.$forceUpdate();
    }
  },
}
</script>


<style>

.item__configuration-select .vs__search::placeholder,
.item__configuration-select .vs__dropdown-toggle,
.item__configuration-select .vs__dropdown-menu {
  background: var(--primary-xtra-dark);
  border: none;
  text-transform: lowercase;
  font-variant: small-caps;
}

select {
  border-radius: 8px;
  font-size: 1em;
  font-weight: 500;
  font-family: inherit;
  width: 400px;
  max-width: 33vw;
  height: 35px;
  background-color: var(--primary-xtra-dark);
  color: #ffffff;
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.25s;
}

select:hover {
  border-color: var(--primary-dark)
}

.container__app {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.container__right-sidebar {
  width: 250px;
  height: calc(100vh - 3rem);
  max-height: calc(100vh - 3rem);
  display: flex;
  flex-direction: column;
}

</style>
