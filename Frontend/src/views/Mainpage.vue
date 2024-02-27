<template>
  <div class="container mt-5">
    <h1 class="text-center">Fitness Classes</h1>

    <div class="row mt-3">
      <div
        v-for="(fitnessClass, index) in fitnessClasses"
        :key="fitnessClass.id"
        class="col-md-4 mb-4"
      >
        <div
          class="card"
          @click="openModal(fitnessClass, imageUrls[index])"
          style="cursor: pointer;"
        >
          <img :src="imageUrls[index]" class="card-img-top" alt="Fitness Class Image">
          <div class="card-body">
            <h5 class="card-title">{{ fitnessClass.name }}</h5>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="selectedFitnessClass" class="modal show" tabindex="-1" role="dialog" style="display: block;">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">{{ selectedFitnessClass.name }}</h5>
            <button type="button" class="close" @click="closeModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <p>{{ selectedFitnessClass.description }}</p>
            <p>{{ selectedFitnessClass.availability }}</p>
            <!-- Move the "Book Class" button here -->
            <button @click="bookClass(selectedFitnessClass.id, userId)">Book Class</button>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">
              Close
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Display user ID -->
    <div v-if="userId">
      User ID: {{ userId }}
    </div>
  </div>
</template>



<script>
import axios from 'axios';
import { getAuth } from 'firebase/auth';

export default {
  data() {
    return {
      userId: null, // Initialize as null
      fitnessClasses: [],
      selectedFitnessClass: null,
      imageUrls: [
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        // ... other image URLs
      ],
    };
  },
  mounted() {
    // Check user authentication
    const auth = getAuth();
    const user = auth.currentUser;

    if (user) {
      // If user is authenticated, fetch fitness classes and user ID
      axios.get('http://localhost:5000/fitnessclass')
        .then(response => {
          this.fitnessClasses = response.data.data.fitnessclass;
          
          // Log user ID after fetching data
          this.userId = user.uid;
          console.log('User ID:', this.userId);
        })
        .catch(error => {
          console.error('Error fetching fitness classes:', error);
        });
    } else {
      // Handle the case where the user is not authenticated
      console.log('User not authenticated');
      // You might want to redirect to the login page or handle it accordingly
    }
  },
  methods: {
    openModal(fitnessClass) {
      console.log('Clicked on:', fitnessClass.name);
      this.selectedFitnessClass = fitnessClass;
    },
    closeModal() {
      this.selectedFitnessClass = null;
    },
    bookClass(classId) {
      // Use this.userId to pass the user ID in the request
      axios.post('http://localhost:5100/complex_booking', { class_id: classId, user_id: this.userId })
  .then(response => {
    console.log(response.data);

    // Manually update the fitnessClasses array after a successful booking
    const updatedFitnessClasses = this.fitnessClasses.map(fc => {
      if (fc.id === classId) {
        // Decrease availability for the booked class
        fc.availability -= 1;
      }
      return fc;
    });

    // Update the data property
    this.fitnessClasses = updatedFitnessClasses;
  })
  .catch(error => {
    // Handle Axios errors
    if (error.response) {
      // The request was made and the server responded with a status code
      // that falls out of the range of 2xx
      console.error('Server responded with an error:', error.response.data);
    } else if (error.request) {
      // The request was made but no response was received
      console.error('No response received from the server:', error.request);
    } else {
      // Something happened in setting up the request that triggered an Error
      console.error('Error setting up the request:', error.message);
    }
  });

    },
  },
};
</script>



