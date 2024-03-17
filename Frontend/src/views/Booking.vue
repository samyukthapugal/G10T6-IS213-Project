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
      <h5 class="card-title">{{ classDetails.fitness_class_details.name }}</h5>
      <p class="card-text">Description: {{ classDetails.fitness_class_details.description }}</p>
      <p class="card-text">Instructor: {{ classDetails.fitness_class_details.instructor }}</p>
      <p class="card-text">Schedule: {{ classDetails.fitness_class_details.schedule }}</p>
      <p class="card-text">Price: ${{ classDetails.fitness_class_details.price }}</p>

      <!-- Display unique_id from fitness_class_details -->
      <p class="card-text">Unique ID: {{ classDetails.unique_id }}</p>

      <p class="card-text">payment_intent_id: {{ classDetails.payment_intent_id }}</p>

      <!-- Dropdown for Ratings -->
      <div class="form-group">
        <label for="ratingDropdown">Rate this class:</label>
        <select v-model="selectedRating" class="form-control" id="ratingDropdown">
          <option v-for="i in 5" :key="i" :value="i">{{ i }}</option>
        </select>
      </div>
      <button @click="Refund(classDetails.payment_intent_id, classDetails.unique_id)" class="btn btn-primary">Refund Button</button>
      <!-- Button to submit Rating -->
      <button @click="submitRating(classDetails.class_id, selectedRating, classDetails.unique_id)" class="btn btn-primary">
        Submit Rating
      </button>
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
      selectedRating: null, // Add this line
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

          const response = await axios.get(`http://localhost:5101/get_booking/${userId}`);
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
    async submitRating(classId, selectedRating, unique_id) {
      // the parameter inside can be any name and is pass from the above button
      try {
          const auth = getAuth();
          const user = auth.currentUser;
          
        // Send a POST request to the make_review microservice
        const response = await axios.post('http://localhost:5003/make_review', {
          classId,
          selectedRating,
          unique_id,
          user
        });

        console.log(response.data); // Log the response from make_review
      } catch (error) {
        console.error('An error occurred while submitting rating:', error);
      }
    },

    // add other functions here it will call the cancel booking complex microservice which will send the payment_intent_id over to server.py stripe service to process the refund and also call maybe another microservice for refund purpose
    async Refund(payment_intent_id, unique_id){
      try {
        const auth = getAuth();
        const user = auth.currentUser;

        if (user) {
          const userId = user.uid;  // Use Firebase user ID

          const response = await axios.post(`http://localhost:5105/get_refund/${userId}`,{payment_intent_id, unique_id, user});

          console.log(response.data);

        
          
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
    }
  }, 
};
</script>


