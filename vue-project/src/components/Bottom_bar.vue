<template>
  <footer>
    <div class="line"></div>
    <div class="foot">
      <div class="left">
        <span>
          <font-awesome-icon :icon="['fab', 'x-twitter']" />
          <a href="">Twitter</a>
        </span>
        <span>
          <font-awesome-icon :icon="['fab', 'square-github']" />
          <a href="">Twitter</a>
        </span>
        <span>
          <font-awesome-icon :icon="['fab', 'qq']" />
          <a href="">Twitter</a>
        </span>
        <span>
          <i class="fa-brands fa-square-x-twitter"></i>
          <a href="">Twitter</a>
        </span>
      </div>
      <div class="right"></div>
    </div>
  </footer>
</template>

<script setup></script>

<style lang="scss" scoped>
footer {
  width: 100vw;
  height: 7.5vh;
  position: absolute;
  background-color: aqua;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}
.line {
  width: 70vw;
  height: 2px;
  background-color: rgb(109, 109, 109, 0.8);
  flex-shrink: 0;
  margin-top: 2px;
}
.foot {
  width: 80vw;
  height: 90%;
  background-color: bisque;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}
.left {
  width: 45%;
  background-color: lightgreen;
  margin: 0;
  padding: 10px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}
.right {
  width: 45%;
  background-color: lightgreen;
  margin: 0;
  padding: 10px;
}
</style>
