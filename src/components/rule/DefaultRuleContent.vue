<template>
  <div>
    This is the default rule content. If you are seeing this, then the selected rule type <code>{{ type }}</code> has not yet been implemented.
  </div>
</template>
<script>
export default {
  name: 'DefaultRuleContent',
  props: {
    type: {
      type: String,
      required: true
    }
  }
}
</script>