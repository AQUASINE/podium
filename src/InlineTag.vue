<template>
<span class="bg4 p pr-3 pl-3 mt-2 w-min pt-0.5 pb-0.5 rounded-full whitespace-nowrap mr-1 text-mute text-xs">
              {{ formattedText }}
            </span>
</template>
<script>
export default {
  name: 'InlineTag',
  props: {
    text: {
      type: String,
      default: ''
    }
  },
  computed: {
    formattedText() {
      // if longer than 20 characters, truncate middle and add ellipsis
      if (this.text.length > 20) {
        return this.text.slice(0, 10) + '...' + this.text.slice(-10);
      }
      return this.text;
    }
  }
}
</script>