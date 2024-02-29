<template>
    <div class="container mt-5">
      <h1 class="test">Create an Account</h1>
      <div class="mb-3">
        <label for="email" class="form-label">Email</label>
        <input type="text" class="form-control" id="email" placeholder="Email" v-model="email">
      </div>
      <div class="mb-3">
        <label for="password" class="form-label">Password</label>
        <input type="password" class="form-control" id="password" placeholder="Password" v-model="password">
      </div>
      <button @click="register" class="btn btn-primary">Submit</button>
      <button @click="signInWithGoogle" class="btn btn-success">Sign In With Google</button>
    </div>
  </template>

<script setup>
import { ref } from "vue";
import { getAuth, createUserWithEmailAndPassword, GoogleAuthProvider, signInWithPopup,} from "firebase/auth";
import { useRouter } from 'vue-router';

const email = ref("");
const password = ref("");
const router = useRouter();

const register = () => {
    createUserWithEmailAndPassword(getAuth(), email.value, password.value)
        .then((userCredential) => {
            const user = userCredential.user;
            console.log("Successfully registered!");
            console.log(user);

            router.push('/mainpage');
        })
        .catch((error) => {
            console.log(error.code);
            alert(error.message);
        });
};

const signInWithGoogle = () => {
    // Implement Google sign-in if needed
    const provider = new GoogleAuthProvider();
    signInWithPopup(getAuth(), provider)
    .then((result)=>{
        console.log(result.user);
        router.push("/mainpage");
    }).catch((error)=>{

    });
};
</script>

<style>
.test{
    color: aqua;
    size: 50px;
}
</style>
