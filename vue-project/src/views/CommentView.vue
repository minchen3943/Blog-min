<template>
  <div class="title">
    <div class="introduce"></div>
    <button>评论</button>
  </div>
  <comment_show />
</template>

<script>
import comment_show from '@/components/comment_show.vue'

export default {
  components: {
    comment_show,
  },
}
</script>

<style></style>
