<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">Booked Classes</h1>

    <!-- Display loading message while fetching data -->
    <div v-if="loading" class="text-center">
      <p>Loading... Please wait.</p>
    </div>

    <!-- Display booked classes details here -->
    <div v-else-if="bookedClasses.length > 0">
      <div class="row">
        <div v-for="(classDetails, index) in bookedClasses" :key="classDetails.class_id" class="col-md-6 mb-4">
          <div class="card h-100 shadow rounded-lg bg-light">
            <div class="card-body">
              <h5 class="card-title">{{ classDetails.fitness_class_details.name }}</h5>
              <p class="card-text mb-2">{{ classDetails.fitness_class_details.description }}</p>
              <p class="card-text"><strong>Instructor:</strong> {{ classDetails.fitness_class_details.instructor }}</p>
              <p class="card-text"><strong>Schedule:</strong> {{ classDetails.fitness_class_details.schedule }}</p>
              <p class="card-text"><strong>Price:</strong> ${{ classDetails.fitness_class_details.price }}</p>

              <!-- Display unique_id from fitness_class_details -->
              <!-- <p class="card-text"><strong>Unique ID:</strong> {{ classDetails.unique_id }}</p>
              <p class="card-text"><strong>Payment Intent ID:</strong> {{ classDetails.payment_intent_id }}</p> -->

              <!-- Dropdown for Ratings -->
              <div v-if="!classDetails.hideRating" class="form-group mb-3">
                <label for="ratingDropdown">Rate this class:</label>
                <select v-model="classDetails.selectedRating" class="form-control" id="ratingDropdown">
                  <option v-for="i in 5" :key="i" :value="i">{{ i }}</option>
                </select>
              </div>
              <!-- Show a message if rating is already submitted -->
              <p v-else class="text-muted">Rating already submitted</p>
              
              <div class="text-center">
                <button @click="Refund(classDetails.payment_intent_id, classDetails.unique_id)" class="btn btn-danger mr-2">Refund</button>
                <button @click="submitRating(classDetails.class_id, classDetails.selectedRating, classDetails.unique_id)" class="btn btn-primary" v-if="!classDetails.hideRating">Submit Rating</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Show a message if no booked classes -->
    <div v-else class="text-center">
      <p>No booked classes found.</p>
    </div>
  </div>
</template>



<script>
import axios from 'axios';
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

      const response = await axios.get(`http://localhost:8000/api/v1/get_booking/${userId}`);
      console.log(response.data);

      // Update the booked classes data in your component
      this.bookedClasses = response.data.data.booked_classes.map(booking => ({
        ...booking,
        selectedRating: null,
        hideRating: false, // Initially, show the rating dropdown for all bookings
      }));

      // Loop through each booked class
      this.bookedClasses.forEach(booking => {
        // Check if the rate_status is "YES"
        if (booking.rate_status === "YES") {
          // If rate_status is "YES", hide the rating dropdown
          booking.hideRating = true;
        }
      });
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
      try {
        const auth = getAuth();
        const user = auth.currentUser;
          
        // Send a POST request to the make_review microservice
        const response = await axios.post('http://localhost:8000/api/v1/make_review', {
          classId,
          selectedRating,
          unique_id,
          user
        },{
          headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin' : '*',
            "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
            "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
          }
        });
        this.ratingMessage()
        console.log(response.data); // Log the response from make_review
      } catch (error) {
        console.error('An error occurred while submitting rating:', error);
      }
    },
    async Refund(payment_intent_id, unique_id){
      try {
        const auth = getAuth();
        const user = auth.currentUser;

        const confirmed = window.confirm("Are you sure you want to proceed with the refund?");
        if (user && confirmed) {
          const userId = user.uid;  // Use Firebase user ID

          const response = await axios.post(`http://localhost:8000/api/v1/get_refund/${userId}`,{payment_intent_id, unique_id, user},{
            headers: {
              'Content-Type': 'application/json',
              'Access-Control-Allow-Origin' : '*',
              "Access-Control-Allow-Methods": "GET,PUT,POST,DELETE,PATCH,OPTIONS",
              "Access-Control-Allow-Headers": "Origin, Content-Type, X-Auth-Token"
            }
          });
          this.refundMessage()
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
    },
    ratingMessage() {
            this.$snackbar.add({
                type: 'success',
                text: 'Rating Successful'
            })
    },
    refundMessage() {
            this.$snackbar.add({
                type: 'success',
                text: 'Refund Successful'
            })
    },
  }, 
};
</script>


<style scoped>
/* Add your custom styles here */
.card {
  border: 1px solid #ccc;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.card-title {
  font-size: 1.2rem;
  color: #333;
}

.card-text {
  font-size: 1rem;
  color: #555;
}

.btn {
  cursor: pointer;
}
</style>