<template>
  <div class="overflow-hidden max-h-screen flex flex-col">
    <div class="bg-primary-alt flex width-100 pt-3 pb-3">
      <div class="flex justify-center items-center pl-3">
        <img src="/podium.svg" alt="Podium Logo" class="logo"/>
        <div class="font-bold pl-2">
          Podium
        </div>
      </div>
      <div class="absolute flex justify-center items-center w-full top-0 pt-2">
        <div>
          Active Configuration
        </div>
        <div class="ml-3 container__configuration-select">
        <VueSelect :options="['Default','Yummers']" class="item__configuration-select"></VueSelect>
        </div>
      </div>
    </div>
    <div class="flex">
      <div class="flex-1">
        Left
      </div>
        <MessagesView :messages="messages"/>
    </div>
  </div>
</template>

<script>


import MessagesView from "./MessagesView.vue";
import VueSelect from 'vue-select';


export default {
  name: 'App',
  components: {MessagesView, VueSelect},
  mounted() {
    window.addEventListener('resize', this.handleResize);
    this.getMessages();
  },
  data() {
    return {
      messages: []
    }
  },
  methods: {
    async getMessages() {
      this.socket = new WebSocket('ws://localhost:8765');
      this.socket.addEventListener('message', event => {
        console.log('Message from server ', event.data);
        this.pushMessage(event.data);
      });

      setInterval(() => {
        // check if socket is in the closed state
        if (this.socket.readyState === 3) {
          console.log('Socket is closed');
          this.socket = new WebSocket('ws://localhost:8765');
          this.socket.addEventListener('message', event => {
            console.log('Message from server ', event.data);
            this.pushMessage(event.data);
          });
        }

      }, 3000);
    },
    pushMessage(message) {
      const decodedMessage = JSON.parse(message);
      if (this.messages.length > 500) {
        // remove 100 messages
        this.messages = this.messages.slice(100);
      }
      this.messages.push(decodedMessage);
    },
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
  background: var(--primary-dark);
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
  background-color: var(--primary-dark);
  color: #ffffff;
  border: 1px solid transparent;
  cursor: pointer;
  transition: border-color 0.25s;
}

select:hover {
  border-color: var(--primary)
}

.container__configuration-select {
  width: 400px;
  max-width: 33vw;
}

.item__configuration-select {
}
</style>
