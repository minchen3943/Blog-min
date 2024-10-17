<template>
  <div class="comment">
    <div class="card" v-for="(item, index) in comment" :key="index">
      <div class="card-body">
        <h5>{{ item.author }}</h5>
        <p>{{ item.content }}</p>
      </div>
      <div class="card-footer text-body-secondary">{{ item.time }}</div>
    </div>
  </div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
Vue.prototype.$axios = axios
export default {
  name: 'comment_show',
  mounted() {
    this.$axios.get('')
  },
}
</script>

<style></style>
