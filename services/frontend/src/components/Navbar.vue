<template>
  <MDBNavbar light style="background-color: #e3f2fd; padding: 20px 50px" expand="lg" container>
    <MDBNavbarBrand href="/">Navbar</MDBNavbarBrand>
    <MDBNavbarToggler target="navbarNav"></MDBNavbarToggler>
    <MDBNavbarNav collapse="navbarNav">
      <MDBNavbarItem to="#" active> Home </MDBNavbarItem>
      <MDBNavbarItem to="#"> Features </MDBNavbarItem>
      <MDBNavbarItem to="#"> Pricing </MDBNavbarItem>
    </MDBNavbarNav>
    <register-button style="float: right"/>
  </MDBNavbar>

</template>

<script>
import {
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarBrand,
    MDBNavbarNav,
    MDBNavbarItem,
  } from 'mdb-vue-ui-kit';
import RegisterButton from "./RegisterButton";

export default {
  name: "Navbar",
  components: {
      RegisterButton,
      MDBNavbar,
      MDBNavbarToggler,
      MDBNavbarBrand,
      MDBNavbarNav,
      MDBNavbarItem,
    },
}
</script>

<style scoped>

</style>