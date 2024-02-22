<template>
  <div class="flex-center">
    <div>
      Messages
      <div v-for="message in messages">
        {{ message }}
      </div>
    </div>
  </div>
</template>

<script>


export default {
  name: 'App',
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
    }
  },
}
</script>


<style></style>
