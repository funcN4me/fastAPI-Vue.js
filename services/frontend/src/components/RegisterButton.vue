<template>
  <div class="login__buttons">
    <a class="navbar-text" href="/register"> <MDBIcon icon="user-plus" iconStyle="fas" size="1x"/> Зарегистрироваться </a>
    <a href="/login" class="navbar-text"> <MDBIcon icon="sign-in-alt" iconStyle="fas" size="1x"/> Войти </a>
  </div>
</template>

<script>
import { MDBIcon } from 'mdb-vue-ui-kit';
export default {
  components: {
    MDBIcon
  },
  name: "RegisterButton"
}
</script>

<style scoped>
   a {
     margin-left: 40px;
   }
</style>