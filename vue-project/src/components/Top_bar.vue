<template>
  <div class="top_bar">
    <router-link to="/" class="skip"><div>测试</div></router-link>
    <router-link to="/" class="skip"><div>测试</div></router-link>
    <router-link to="/" class="skip"><div>测试</div></router-link>
  </div>
</template>

<script setup></script>

<style scoped>
.top_bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  width: 95vw;
  height: 5vh;
  background: rgba(54, 54, 54, 0.65);
  border-radius: 12px;
  margin-left: 2.5vw;
  margin-top: 5px;
}
.skip {
  width: 25%;
  text-align: center;
}
</style>
