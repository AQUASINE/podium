<template>
  <div class="overflow-y-scroll max-h-screen">
    Messages
    <div v-for="message in messages" class="bg3 item__message flex">
      <div class="flex w-full">
        <div class="p-3 container__message-item">
          <span class="font-bold">
          {{ message.user }}
          </span>: {{ message.message }}
          <div class="pt-2">
            <span v-for="tag in message.tags" class="bg4 p-1 pr-3 pl-3 w-min rounded-full whitespace-nowrap mr-1">
              {{ tag }}
            </span>
          </div>
        </div>
        <div class="flex-1 p-1 item__score">
          {{ message.weight }}
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'MessagesView',
  props: {
    messages: {}
  }
}
</script>
<style>
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

</style>