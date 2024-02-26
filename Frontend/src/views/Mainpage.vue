<!-- Your Vue.js component template -->
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
            <button @click="bookClass(fitnessClass.id, userId)">Book Class</button>
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
import axios from 'axios';

export default {
  data() {
    return {
      userId: 100, // Set your actual user ID here
      fitnessClasses: [],
      selectedFitnessClass: null,
      imageUrls: [
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2Fdolphin.jpg?alt=media&token=0969b7e8-a848-475f-b3a4-865045b3d946',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FblueWhale.jpg?alt=media&token=b753c5b6-2420-4a26-9bbb-aae7f142d913',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FblueWhale.jpg?alt=media&token=b753c5b6-2420-4a26-9bbb-aae7f142d913',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FblueWhale.jpg?alt=media&token=b753c5b6-2420-4a26-9bbb-aae7f142d913',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FblueWhale.jpg?alt=media&token=b753c5b6-2420-4a26-9bbb-aae7f142d913',
        'https://firebasestorage.googleapis.com/v0/b/test1-69744.appspot.com/o/images%2FblueWhale.jpg?alt=media&token=b753c5b6-2420-4a26-9bbb-aae7f142d913',
        // ... other image URLs
      ],
    };
  },
  mounted() {
    axios.get('http://localhost:8000/api/v1/fitnessclass')
      .then(response => {
        this.fitnessClasses = response.data.data.fitnessclass;
      })
      .catch(error => {
        console.error('Error fetching fitness classes:', error);
      });
  },
  methods: {
    openModal(fitnessClass) {
      console.log('Clicked on:', fitnessClass.name);
      this.selectedFitnessClass = fitnessClass;
    },
    closeModal() {
      this.selectedFitnessClass = null;
    },
    bookClass(classId, userId) {
      axios.post('http://localhost:5100/complex_booking', { class_id: classId, user_id: userId })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error('Error booking class:', error);
        });
    },
  },
};
</script>

<style scoped>
/* Add any custom styles specific to this component */
</style>
