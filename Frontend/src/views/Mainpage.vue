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
          class="card class-card"
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
            <p>Slot Availability:{{ selectedFitnessClass.availability }}</p>
            <!-- Move the "Book Class" button here -->
            <button @click="initiatePayment(selectedFitnessClass.id, userId)">Book Now</button>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" @click="closeModal">
              Close
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
// Import necessary libraries
import axios from 'axios';
import { getAuth } from 'firebase/auth';

export default {
  data() {
    return {
      userId: null,
      fitnessClasses: [],
      ratingsData: [],
      selectedFitnessClass: null,
      imageUrls: [
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FHIIT.jpg?alt=media&token=207113a2-d9f4-4e35-9b47-3df41d83e91c',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fyoga.jpg?alt=media&token=cccc81b0-aeb4-41ff-b192-b5bd532a78e3',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Frunning.jpg?alt=media&token=400df06d-d007-415f-b0b4-c6a89018a805',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fimage1.jpg?alt=media&token=0391562c-fae5-4fe1-82df-c4a21c6cfb74',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fzumba.jpg?alt=media&token=d9709f77-d47a-4f01-9007-57fc7b037b52',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fpilate.jpg?alt=media&token=cfaa50e0-bc11-4300-b376-b3abd9a52ea2',
      ],
    };
  },
  mounted() {
  const auth = getAuth();
  const user = auth.currentUser;

  if (user) {
    axios.get('http://localhost:5200/view_classes')
      .then(response => {
        console.log('Response data:', response.data);
        this.fitnessClasses = response.data.data.fitnessclass;
        this.userId = user.uid;

        // After successfully fetching fitness classes, make a request to get ratings
        axios.get('http://localhost:5200/view_rating')
          .then(ratingsResponse => {
            console.log('Rating data:', ratingsResponse.data);
            this.ratingsData = ratingsResponse.data.data.rating; // Updated name

          })
          .catch(ratingsError => {
            console.error('Error fetching ratings:', ratingsError);
          });
      })
      .catch(error => {
        console.error('Error fetching fitness classes:', error);
      });
  } else {
    console.log('User not authenticated');
  }
},
  methods: {
    openModal(fitnessClass) {
      this.selectedFitnessClass = fitnessClass;
    },
    closeModal() {
      this.selectedFitnessClass = null;
    },
    initiatePayment(classId, userId) {
      this.$router.push({ name: 'stripe', query: { classId, userId } });
    },
  },
};
</script>

<style>
.class-card {
  height: 100%; /* Set a fixed height for the card */
  display: flex;
  flex-direction: column;
}

.card-img-top {
  object-fit: cover; /* Ensure the image covers the entire card */
  height: 200px; /* Set a fixed height for the image */
}
</style>
