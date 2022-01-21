<template>
  <div class="form__register container-sm">
    <form action="">
      <div class="mb-3">
      <label for="formGroupExampleInput" class="form-label">Example label</label>
      <input type="text" class="form-control" id="formGroupExampleInput" placeholder="Example input placeholder">
    </div>
    <div class="mb-3">
      <label for="formGroupExampleInput2" class="form-label">Another label</label>
      <input type="text" class="form-control" id="formGroupExampleInput2" placeholder="Another input placeholder">
    </div>
      <button class="btn btn-primary" type="submit">
        Privet
      </button>
    </form>
  </div>

</template>

<script>
export default {
  name: "RegisterForm"
}
</script>

<style scoped>
.form__register {
  width: 30%;
}
</style>