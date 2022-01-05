<template>
  <MDBNavbar light style="background-color: #e3f2fd; padding: 20px 50px" expand="lg" container>
    <MDBNavbarBrand href="#">Navbar</MDBNavbarBrand>
    <MDBNavbarToggler target="navbarNav"></MDBNavbarToggler>
    <MDBNavbarNav collapse="navbarNav">
      <MDBNavbarItem to="#" active> Home </MDBNavbarItem>
      <MDBNavbarItem to="#"> Features </MDBNavbarItem>
      <MDBNavbarItem to="#"> Pricing </MDBNavbarItem>
      <MDBNavbarItem to="#" disabled> Jopa </MDBNavbarItem>
    </MDBNavbarNav>
    <register-button style="float: right"/>
  </MDBNavbar>

</template>

<script>
// import axios from 'axios';
  import {
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarBrand,
    MDBNavbarNav,
    MDBNavbarItem,
  } from 'mdb-vue-ui-kit';
import RegisterButton from "./RegisterButton";

  export default {
    components: {
      RegisterButton,
      MDBNavbar,
      MDBNavbarToggler,
      MDBNavbarBrand,
      MDBNavbarNav,
      MDBNavbarItem,
    },
  };
  // methods: {
  //   getMessage() {
  //     axios.get('/')
  //       .then((res) => {
  //         this.msg = res.data;
  //       })
  //       .catch((error) => {
  //         console.error(error);
  //       });
  //   },
  // },
  // created() {
  //   this.getMessage();
  // },
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
