<template>
  <MDBContainer fluid class="test shadow-5 w-50 p-0">
    <form @submit.prevent style="padding: 20px 20px;">
    <MDBInput label="email" type="email" v-model="email"/>
    <MDBInput label="password" type="password" v-model="password"/>
      <div class="text-center">
        <MDBBtn color="primary" @click="greet" type="submit">
          Регистрация
        </MDBBtn>
      </div>
  </form>
  </MDBContainer>
</template>

<script>
import { MDBBtn, MDBInput, MDBContainer } from "mdb-vue-ui-kit";
import { ref } from 'vue';
import axios from 'axios';

export default {
  data() {
    return {
      counter: 0
    }
  },
  name: "RegisterForm",
  components: {
  //   MDBCard,
  //   MDBCardBody,
  //   MDBCardTitle,
  //   MDBCardText,
    MDBBtn,
    MDBInput,
    MDBContainer,
  },
  setup() {
      const email = ref('');
      const password = ref('');

      return {
        email,
        password
      };
    },
  methods: {
    greet() {
      axios.post('/register', {
        email: this.email,
        password: this.password
      })
      .then(function (response) {
        console.log(response.data);
        alert('Успешна!')
      })
      .catch(function (error) {
        console.log(error);
        alert("Ашибна:(")
      });
    }
  }
};

</script>

<style scoped>
 * {
   margin: 0 auto;
   box-sizing: border-box;
 }

</style>