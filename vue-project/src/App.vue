<template>
  <div class="background">
    <top_bar />
    <RouterView />
    <bottom_bar />
  </div>
</template>

<script setup>
import { RouterView } from 'vue-router'
import top_bar from '@/components/Top_bar.vue'
import bottom_bar from '@/components/Bottom_bar.vue'
</script>

<style scoped>
.background {
  min-width: 100vw;
  min-height: 100vh;
  background-image: url('@/assets/background.jpg');
  background-size: cover;
  background-position: -45px center;
  background-repeat: no-repeat;
  margin: 0;
  display: flex;
  flex-direction: column;
}
</style>
