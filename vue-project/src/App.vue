<template>
  <div class="background">
    <top_bar />
    <bottom_bar />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import top_bar from '@/components/Top_bar.vue'
import bottom_bar from '@/components/Bottom_bar.vue'
</script>

<style scoped>
.background {
  width: 100vw;
  height: 100vh;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: -20px center;
  background-repeat: no-repeat;
  margin: 0;
}
</style>
