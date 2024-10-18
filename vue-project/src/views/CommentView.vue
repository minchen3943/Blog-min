<template>
  <div class="title">
    <div class="introduce"></div>
    <button class="button1" @click="upload">添加评论</button>
  </div>
  <comment_show />
  <div class="dialog" v-if="dialogShow">
    <p class="titles">用户名</p>
    <input class="input1" v-model="form.author" type="text" />
    <p class="titles">内容</p>
    <input class="input2" v-model="form.content" type="text" />
    <button class="button2" @click="submit" v-if="!errorShow">提交</button>
  </div>
  <div class="error" v-if="errorShow">
    <p class="titles">{{ errorTip }}</p>
    <button class="button3" @click="errorexit">确认</button>
  </div>
</template>

<script setup>
import comment_show from '@/components/comment_show.vue'
import { useRouter } from 'vue-router'
import { ref } from 'vue'
import axios from 'axios'
const dialogShow = ref(false)
const errorShow = ref(false)
const errorTip = ref('')

const routergo = useRouter()
const form = ref({
  author: '',
  content: '',
})

function upload() {
  dialogShow.value = true
}

function errorexit() {
  errorShow.value = false
}

function submit() {
  const { author, content } = form.value
  const formData = new FormData()
  formData.append('author', author)
  formData.append('content', content)
  axios
    .post('/api/comment/add', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    })
    .then(function (response) {
      console.log(response)
      if (response.status === 200) {
        dialogShow.value = false
        routergo.go(0)
      }
    })
    .catch(error => {
      console.error(error)
      // 检查是否有响应，并根据状态码设置错误提示
      if (error.response) {
        switch (error.response.status) {
          case 401:
            setErrorTip('作者和内容不能为空')
            break
          case 402:
            setErrorTip('内容不能超过150个字符')
            break
          case 403:
            setErrorTip('未确认异常')
            break
          case 405:
            setErrorTip('请求方法错误')
            break
          default:
            setErrorTip('未知错误')
        }
      } else {
        setErrorTip('请求失败，请稍后再试')
      }
    })
  const setErrorTip = message => {
    errorTip.value = message
    errorShow.value = true
  }
}
</script>

<style>
.dialog {
  display: flex;
  flex-direction: column;
  background-color: aquamarine;
  width: 85vw;
  height: 33vh;
  z-index: 99;
  position: absolute;
  top: 40vh;
  left: 7.5vw;
  text-align: center;
  align-items: center;
}
.titles {
  margin: 0;
  padding: 0;
}
.input1,
.input2 {
  width: 90%;
}
.input2 {
  height: 55%;
}
.error {
  background-color: rgba(255, 0, 0, 0.704);
  height: 10vh;
  width: 60vw;
  position: absolute;
  z-index: 999;
  left: 20vw;
  top: 45vh;
  text-align: center;
  font-size: 1.4em;
}
.button2 {
  width: 20%;
  height: 15%;
  border-radius: 6px;
  margin-left: 70%;
  margin-right: 10%;
}
.button3 {
  height: 40%;
  margin-top: 1%;
  margin-left: 50%;
  font-size: 1rem;
  border-radius: 6px;
}
</style>
