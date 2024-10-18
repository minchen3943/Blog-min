<template>
  <div class="comment">
    <div class="card" v-for="(item, index) in comment_list" :key="index">
      <div class="card-header">
        <h5 class="author">{{ item.author }}</h5>
      </div>
      <div class="card-body">
        <p>{{ item.content }}</p>
      </div>
      <div class="card-footer text-body-secondary">{{ item.created }}</div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import axios from 'axios'
const comment_list = ref([])
const page = ref(1)
const pagenew = ref(2)

function getData() {
  axios
    .get('/api/comment/get', {
      params: {
        page: page.value,
      },
    })
    .then(function (response) {
      console.log(response)
      if (response.status === 200) {
        const data = response.data.comments
        comment_list.value = data
      }
    })
    .catch(function (error) {
      console.log(error)
    })
}
function addData() {
  axios
    .get('/api/comment/get', {
      params: {
        page: pagenew,
      },
    })
    .then(function (response) {
      console.log(response)
      if (response.status === 200) {
        const data = response.data.comments
        comment_list.value.push = data
      }
    })
    .catch(function (error) {
      console.log(error)
    })
}
onMounted(() => {
  getData()
})
</script>

<style scoped>
.comment {
  min-height: 81vh;
  width: 80vw;
  margin-left: 10vw;
  margin-right: 10vw;
}
.card {
  background-color: rgba(190, 190, 190, 0.521);
  margin-bottom: 3vh;
}
.card-footer {
  text-align: right;
  padding-right: 10vw;
}
</style>
