<template>
  <Navbar/>
  <register-form/>
</template>

<script>
import Navbar from "@/components/Navbar";
import RegisterForm from "@/components/RegisterForm";
export default {
  name: "Registration",
  components: {
    RegisterForm,
    Navbar,
  }
}
</script>

<style scoped>

</style>