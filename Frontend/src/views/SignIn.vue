<template>
  <div class="bg-img">
    <div class="content">
      <header>Sign In to an Account</header>
      <div class="field" style="padding-left: 10%;">
        <input type="text" placeholder="Email" v-model="email">
      </div>
      <div class="field space" style="padding-left: 10%;">
        <input type="password" placeholder="Password" v-model="password">
      </div>
      <p v-if="errMsg">{{ errMsg }}</p>
      <div class="field space2">
        <input type="submit" value="Login" @click="login">
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { getAuth, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { useRouter } from 'vue-router';

const email = ref("");
const password = ref("");
const errMsg = ref();
const userId = ref(null); // Variable to store user ID
const router = useRouter();

const login = () => {
  signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((userCredential) => {
      // Successful login actions
      userId.value = userCredential.user.uid;
      router.push('/mainpage');
    })
    .catch((error) => {
      // Handle login errors
      handleAuthError(error);
    });
};

// Uncomment and adjust if signInWithGoogle functionality is desired
// const signInWithGoogle = () => { ... };

const handleAuthError = (error) => {
  // Handle authentication errors
};
</script>

<style>
/* Include your CSS styles here */
@import url('https://fonts.googleapis.com/css?family=Montserrat:400,500,600,700|Poppins:400,500&display=swap');
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  user-select: none;
}
.bg-img {
  background: url('bg.jpg');
  height: 100vh;
  background-size: cover;
  background-position: center;
  position: relative;
}
.bg-img:after {
  position: absolute;
  content: '';
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background: rgba(0,0,0,0.7);
}
.content {
  position: absolute;
  top: 50%;
  left: 50%;
  z-index: 999;
  text-align: center;
  padding: 60px 32px;
  width: 370px;
  transform: translate(-50%,-50%);
  background: rgba(255,255,255,0.04);
  box-shadow: -1px 4px 28px 0px rgba(0,0,0,0.75);
}
.content header{
  color: white;
  font-size: 33px;
  font-weight: 600;
  margin: 0 0 35px 0;
  font-family: 'Montserrat',sans-serif;
}

.field{
  position: relative;
  height: 45px;
  width: 100%;
  display: flex;
  background: rgba(255,255,255,0.94);
}

.field span{
  color: #222;
  width: 40px;
  line-height: 45px;
}
.field input{
  height: 100%;
  width: 100%;
  background: transparent;
  border: none;
  outline: none;
  color: #222;
  font-size: 16px;
  font-family: 'Poppins',sans-serif;
}
.space{
  margin-top: 16px;
}
.space2{
  margin-top: 36px;
}

.show{
  position: absolute;
  right: 13px;
  font-size: 13px;
  font-weight: 700;
  color: #222;
  display: none;
  cursor: pointer;
  font-family: 'Montserrat',sans-serif;
}
.field input[type="submit"]{
  background: #3498db;
  border: 1px solid #2691d9;
  color: white;
  font-size: 18px;
  letter-spacing: 1px;
  font-weight: 600;
  cursor: pointer;
  font-family: 'Montserrat',sans-serif;
}
.field input[type="submit"]:hover{
  background: #2691d9;
}
.login{
  color: white;
  margin: 20px 0;
  font-family: 'Poppins',sans-serif;
}
/* The rest of your CSS styles */
</style>
