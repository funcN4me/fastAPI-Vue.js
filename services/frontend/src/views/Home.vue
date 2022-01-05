<template>
  <HelloWorld
    msg="Thank you for using our product. We're glad you're with us."
  />
</template>

<script>
// @ is an alias to /src
import HelloWorld from "@/components/HelloWorld.vue";

export default {
  name: "Home",
  components: {
    HelloWorld
  }
};
</script>