<!-- <template>
  <router-link to="/">Home</router-link> |
    <router-link to="/feed">Feed</router-link> |
    <router-link to="/register">Register</router-link> |
    <router-link to="/sign-in">Login</router-link> |

    <br>
    <button @click="handleSignOut" v-if="isLoggedIn">Sign Out</button>
  <router-view />

  
</template> -->

<template>
  <div class="container-fluid">
    <div class="row">
      
      <div class="col p-0">
        <nav class="navbar navbar-expand-lg bg-black ">
          <div class="col">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <!-- Plan to be icon  -->
              <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>

              <!-- The normal navbar options -->
              <ul class="navbar-nav ms-auto ">
                <!-- <li class="nav-item ms-3 ">
                  <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>
                </li> -->
                <li class="nav-item">
                  <router-link to="/booking" class="nav-link">Booking</router-link>
                </li>
                <!-- Conditionally show "Register" and "Login" links -->
                <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/register" class="nav-link">Register</router-link>
                </li>
                <li v-if="!isLoggedIn" class="nav-item">
                  <router-link to="/sign-in" class="nav-link">Login</router-link>
                </li>

                <!-- Can add more option for fitness website below -->

                <li class="nav-item">
                  <button @click="handleSignOut" v-if="isLoggedIn" class="btn btn-danger signoutBtn">Sign Out</button>
                </li>
              </ul>
            </div>
          </div>
        </nav>

        <router-view />
      </div> <!--col 1 end-->

    </div> <!--row 1 end-->





  </div> <!--Container-fluid end-->
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { getAuth, onAuthStateChanged, signOut } from "firebase/auth";
import { useRouter } from 'vue-router'; // Import useRouter

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
.signoutBtn {
  margin-left: 10px;
}
</style>
