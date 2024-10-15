<template>
  <footer>
    <div class="line"></div>
    <div class="foot">
      <div class="left">
        <span class="link">
          <font-awesome-icon
            :icon="['fab', 'x-twitter']"
            style="color: #e6e6e6"
          />
          <a href="">Twitter</a>
        </span>
        <span class="link">
          <font-awesome-icon
            :icon="['fab', 'square-github']"
            style="color: #e6e6e6"
          />
          <a href="">Github</a>
        </span>
        <span class="link">
          <font-awesome-icon
            :icon="['fab', 'telegram']"
            style="color: #e6e6e6"
          />
          <a href="">telegram</a>
        </span>
        <span class="link">
          <font-awesome-icon :icon="['fab', 'qq']" style="color: #e6e6e6" />
          <a href="">QQ</a>
        </span>
      </div>
      <div class="right">
        <span class="link">
          <a href="https://beian.mps.gov.cn/#/query/webSearch">
            湘ICP备<br />2024087622号
          </a>
        </span>
      </div>
    </div>
  </footer>
</template>

<script setup></script>

<style lang="scss" scoped>
footer {
  width: 100vw;
  height: 12vh;
  position: absolute;
  bottom: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: column;
}
.line {
  width: 90vw;
  height: 1.5px;
  background-color: rgba(239, 239, 239, 0.921);
  flex-shrink: 0;
  margin-top: 2px;
  border-radius: 20px;
}
.foot {
  width: 90vw;
  height: 90%;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}
.left {
  width: 45%;
  padding: 10px;
  display: flex;
  flex-direction: column;
  flex-wrap: wrap;
}

.right {
  width: 45%;
  margin: 0;
  padding: 10px;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.link {
  padding-top: 1px;
  padding-bottom: 1px;
  font-size: 1.05em;
}
</style>
