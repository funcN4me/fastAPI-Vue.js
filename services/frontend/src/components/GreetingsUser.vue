<template>
  <div class="d-flex align-items-center justify-content-center" style="height: 350px;">
    Hello, Mr {{ msg['email'] }}
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "GreetingsUser",
  methods: {
    getMessage() {
      axios.get('/users/1')
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  beforeCreate() {
    this.getMessage();
  },
};
</script>

<style scoped>

</style>