<template>
  <div class="container mt-5">
    <h1 class="text-center">Booked Classes</h1>

    <!-- Display loading message while fetching data -->
    <div v-if="loading">
      <p>Loading...will take a few seconds to get the latest booking please be patient</p>
    </div>

    <!-- Display booked classes details here -->
    <div v-else-if="bookedClasses.length > 0">
      <div v-for="classDetails in bookedClasses" :key="classDetails.class_id" class="card mt-3">
        <div class="card-body">
          <h5 class="card-title">{{ classDetails.description }}</h5>
          <p class="card-text">Instructor: {{ classDetails.instructor }}</p>
          <p class="card-text">Schedule: {{ classDetails.schedule }}</p>
          <p class="card-text">Price: ${{ classDetails.price }}</p>
        </div>
      </div>
    </div>

    <!-- Show a message if no booked classes -->
    <div v-else>
      <p>No booked classes found.</p>
    </div>
  </div>
</template>

<script>

import axios from 'axios';
import { ref, onMounted } from 'vue';
import { getAuth } from 'firebase/auth';

export default {
  data() {
    return {
      bookedClasses: [],
      loading: true,
    };
  },
  mounted() {
    this.fetchBookedClasses();
  },
  methods: {
    async fetchBookedClasses() {
      try {
        const auth = getAuth();
        const user = auth.currentUser;

        if (user) {
          const userId = user.uid;  // Use Firebase user ID

          const response = await axios.get(`http://localhost:5001/user/bookedClasses/${userId}`);
          console.log(response.data);

          // Update the booked classes data in your component
          this.bookedClasses = response.data.data.booked_classes;
        } else {
          console.log('User not authenticated');
          // You can handle the case where the user is not authenticated, e.g., redirect to login
        }
      } catch (error) {
        console.error('An error occurred:', error);
      } finally {
        // Set loading to false after the API call, regardless of success or failure
        this.loading = false;
      }
    },
  },
};
</script>
