<template>
  <Navbar/>
  <register-form/>
</template>

<script>
import Navbar from "@/components/Navbar";
import RegisterForm from "@/components/RegisterForm";
export default {
  name: "Register",
  components: {
    Navbar,
    RegisterForm,
  }
}
</script>

<style scoped>

</style>