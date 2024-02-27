<!-- <template>
    <h1>Sign In to an Account</h1>
    <p><input type="text" placeholder="Email" v-model="email"></p>
    <p><input type="text" placeholder="Password" v-model="password"></p>
    <p v-if="errMsg">{{ errMsg }}</p>
    <p><button @click="register">Submit</button></p>
    <p><button @click="signInWithGoogle">Sign In With Google</button></p>
</template>

<script setup>
import { ref } from "vue";
import { getAuth, signInWithEmailAndPassword, GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { useRouter } from 'vue-router';

const email = ref("");
const password = ref("");
const errMsg = ref();
const router = useRouter();

const register = () => {
  signInWithEmailAndPassword(getAuth(), email.value, password.value)
    .then((userCredential) => {
      const user = userCredential.user;
      console.log("Successfully Signed in!");
      console.log(user);

      router.push('/mainpage');
    })
    .catch((error) => {
      console.error("Sign-in Error:", error);

      if (error.code) {
        switch (error.code) {
          case "auth/invalid-email":
            errMsg.value = "Invalid email";
            break;
          case "auth/user-not-found":
            errMsg.value = "No account with that email was found";
            break;
          case "auth/wrong-password":
            errMsg.value = "Incorrect Password";
            break;
          default:
            errMsg.value = "Email or password was incorrect";
            break;
        }
      } else {
        errMsg.value = "An unexpected error occurred during sign-in.";
      }
    });
};

const signInWithGoogle = () => {
  const provider = new GoogleAuthProvider();
  signInWithPopup(getAuth(), provider)
    .then((result) => {
      console.log(result.user);
      router.push("/mainpage");
    })
    .catch((error) => {
      console.error("Google Sign-in Error:", error);
    });
};
</script> -->

<template>
  <div>
    <h1>Sign In to an Account</h1>
    <p><input type="text" placeholder="Email" v-model="email"></p>
    <p><input type="password" placeholder="Password" v-model="password"></p>
    <p v-if="errMsg">{{ errMsg }}</p>
    <p><button @click="login">Submit</button></p>
    <p><button @click="signInWithGoogle">Sign In With Google</button></p>
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
      const user = userCredential.user;
      console.log("Successfully Signed in!");
      console.log(user);

      // Set the user ID variable
      userId.value = user.uid;

      router.push('/mainpage');
    })
    .catch((error) => {
      console.error("Sign-in Error:", error);
      handleAuthError(error);
    });
};

// const signInWithGoogle = () => {
//   const provider = new GoogleAuthProvider();
//   signInWithPopup(getAuth(), provider)
//     .then((result) => {
//       console.log(result.user);
//       console.log("User ID:", user.uid); // Log the user ID
//       // Set the user ID variable
//       userId.value = result.user.uid;

//       router.push("/mainpage");
//     })
//     .catch((error) => {
//       console.error("Google Sign-in Error:", error);
//       handleAuthError(error);
//     });
// };

const handleAuthError = (error) => {
  if (error.code) {
    switch (error.code) {
      case "auth/invalid-email":
        errMsg.value = "Invalid email";
        break;
      case "auth/user-not-found":
        errMsg.value = "No account with that email was found";
        break;
      case "auth/wrong-password":
        errMsg.value = "Incorrect Password";
        break;
      default:
        errMsg.value = "Email or password was incorrect";
        break;
    }
  } else {
    errMsg.value = "An unexpected error occurred during sign-in.";
  }
};
</script>
