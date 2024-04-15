<template>
  <div class="container__app">
    <div class="bg-primary-alt flex width-100 pt-3 pb-3 container__top-bar">
      <div class="flex justify-center items-center pl-3">
        <img src="/podium.svg" alt="Podium Logo" class="logo"/>
        <div class="font-bold pl-2">
          Podium
        </div>
      </div>
      <div class="absolute flex justify-center items-center w-full top-0 pt-2">
        <div class="heading__active-config">
          Active Configuration
        </div>
        <div class="ml-3 container__configuration-select">
        <VueSelect :options="['translation-chatbox-app','default']" class="item__configuration-select"></VueSelect>
        </div>
      </div>
    </div>
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
import VueSelect from 'vue-select';
import LeftSidebar from "./LeftSidebar.vue";
import CenterPanel from "./CenterPanel.vue";
import UsersView from "./UsersView.vue";
import {mapState} from "vuex";

export default {
  name: 'App',
  components: {UsersView, CenterPanel, LeftSidebar, MessagesView, VueSelect},
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

.container__configuration-select {
  width: 400px;
  max-width: 33vw;
}

.item__configuration-select {
  font-size: 0.9rem;
}

.container__top-bar {
  position: relative;
  width: 100%;
  z-index: 1000;
}

.container__daemon-info code {
  background-color: var(--bg3);
  margin-left: 0;
}

.heading__active-config {
  font-size: 0.95em;
  font-weight: 500;
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

.header__row-name h1 {
  font-size: 1.5em;
  margin: 0;
  font-weight: 700;
}

</style>
