<template>
  <div class="comment">
    <div class="card" v-for="(item, index) in comments" :key="index">
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

<script>
export default {
  data() {
    return {
      comments: [
        {
          id: 1,
          author: 'admin',
          content: 'test',
          created: '42432',
        },
        {
          id: 1,
          author: 'admin',
          content: 'test',
          created: '42432',
        },
        {
          id: 1,
          author: 'admin',
          content: 'test',
          created: '42432',
        },
        {
          id: 1,
          author: 'admin',
          content: 'test',
          created: '42432',
        },
      ],
    }
  },
}
</script>

<style scoped>
.comment {
  min-height: 81vh;
  width: 80vw;
  margin-left: 10vw;
  margin-right: 10vw;
}
.card {
  /* text-align: center; */
  background-color: rgba(190, 190, 190, 0.521);
  margin-bottom: 3vh;
}
.card-footer {
  text-align: right;
  padding-right: 10vw;
}
</style>
