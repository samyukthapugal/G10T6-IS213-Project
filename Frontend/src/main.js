import { createApp } from 'vue';
import App from './App.vue';
import './index.css';
import router from './router'; // Ensure that your router file is correctly imported

// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app';
// Uncomment and add other SDK imports if necessary
// import { getAnalytics } from 'firebase/analytics';

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional

// my api 
const firebaseConfig = {
  // Add your Firebase configuration here
apiKey: "AIzaSyD34mwIYCA-c1QwsoRbG3-Qtx2skxaKAxs",
authDomain: "esd-project-37d35.firebaseapp.com",
databaseURL: "https://esd-project-37d35-default-rtdb.asia-southeast1.firebasedatabase.app",
projectId: "esd-project-37d35",
storageBucket: "esd-project-37d35.appspot.com",
messagingSenderId: "114774698440",
appId: "1:114774698440:web:ad516314207e365bdb78fd",
measurementId: "G-FJDVQ0FC1Z"
};

// Initialize Firebase
initializeApp(firebaseConfig);

// Create the app instance
const app = createApp(App);

// Use the router plugin
app.use(router);

// Mount the app to the element with id 'app'
app.mount('#app');



