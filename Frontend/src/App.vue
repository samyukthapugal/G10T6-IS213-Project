<template>
  <div class="container-fluid">
    <div class="row">
      
      <div class="col p-0">
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
          <div class="container">
            <!-- Logo/Home link -->
            <router-link to="/" class="navbar-brand">FitnessHub</router-link>

            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav ms-auto">
                <!-- Conditionally render "Main" link if logged in -->
                

                <!-- If it's login, display the main icon -->
                <router-link v-if="isLoggedIn" to="/mainpage" class="nav-link active" aria-current="page">Classes</router-link>

                <!-- The normal navbar options -->
                <li v-if="isLoggedIn" class="nav-item">
                  <router-link to="/booking" class="nav-link">Booking</router-link>
                </li>

                <!-- Conditionally show "Register" and "Login" links -->

                <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/map" class="nav-link">Find Us</router-link>
                </li>
                <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/register" class="nav-link">Register</router-link>
                </li>
                <!-- <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/sign-in" class="nav-link">Map</router-link>
                </li> -->
                <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/sign-in" class="nav-link">Login</router-link>
                </li>

                <!-- Add more options for the fitness website below -->

                <li class="nav-item">
                  <button @click="handleSignOut" v-if="isLoggedIn" class="btn btn-danger signoutBtn">Sign Out</button>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <router-view />
      </div> <!-- col 1 end -->

    </div> <!-- row 1 end -->
  </div> <!-- Container-fluid end -->
</template>

<script setup>
// Import necessary functions from Vue and Firebase
import { onMounted, ref } from 'vue';
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import { useRouter } from 'vue-router'; 

const router = useRouter();
const isLoggedIn = ref(false);
let auth;

onMounted(() => {
  auth = getAuth();
  onAuthStateChanged(auth, (user) => {
    isLoggedIn.value = !!user;
  });
});

const handleSignOut = () => {
  signOut(auth).then(() => {
    router.push('/');
  });
};
</script>

<style scoped>
/* Add custom styles for the navbar here */
.navbar-brand {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav-link {
  margin: 0 10px;
}

.signoutBtn {
  margin-left: 10px;
}
</style>
