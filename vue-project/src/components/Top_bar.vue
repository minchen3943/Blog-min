<template>
  <header>
    <div class="top_bar">
      <router-link to="/" class="skip"><div>主页</div></router-link>
      <router-link to="/comment" class="skip"><div>评论区</div></router-link>
      <router-link to="/" class="skip"><div>测试</div></router-link>
    </div>
  </header>
</template>

<script setup></script>

<style scoped>
.top_bar {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-around;
  width: 95vw;
  height: 7vh;
  background: rgba(94, 94, 94, 0.6);
  border-radius: 12px;
  margin-left: 2.5vw;
  margin-top: 5px;
}
.skip {
  width: 25%;
  text-align: center;
  font-size: 1.4em;
}
</style>
