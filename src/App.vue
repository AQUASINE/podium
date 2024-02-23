<template>
  <div class="overflow-hidden max-h-screen flex flex-col">
    <div class="bg-primary-alt flex width-100 pt-3 pb-3">
      <div class="flex justify-center items-center pl-3">
        <img src="/podium.svg" alt="Podium Logo" class="logo"/>
        <div class="font-bold pl-2">
          Podium
        </div>
      </div>
      <div class="absolute flex justify-center items-center w-full top-0 pt-1.5">
        <div>
          Active Configuration
        </div>
        <select class="ml-3">
          <option>Default</option>
          <option>Default 2</option>
        </select>
      </div>
    </div>
    <div class="flex">
      <div class="flex-1">
      </div>
    <MessagesView :messages="messages"/>
    </div>
  </div>
</template>

<script>


import MessagesView from "./MessagesView.vue";

export default {
  name: 'App',
  components: {MessagesView},
  mounted() {
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
    },
    pushMessage(message) {
      const decodedMessage = JSON.parse(message);
      if (this.messages.length > 50) {
        this.messages.shift();
      }
      this.messages.push(decodedMessage);
    }
  },
}
</script>


<style>

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

</style>
