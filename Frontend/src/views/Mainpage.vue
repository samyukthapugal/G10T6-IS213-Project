<template>
    <div class="container mt-5">
      <h1 class="text-center">Fitness Classes</h1>
  
      <div class="row mt-3">
        <div v-for="fitnessClass in fitnessClasses" :key="fitnessClass.id" class="col-md-4 mb-4">
          <div class="card">
            <img :src="fitnessClass.image" class="card-img-top" alt="Fitness Class Image">
            <div class="card-body">
              <h5 class="card-title">{{ fitnessClass.name }}</h5>
              <p class="card-text">{{ fitnessClass.description }}</p>
              <a href="#" class="btn btn-primary">Learn More</a>
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
        fitnessClasses: [],
      };
    },
    mounted() {
      // Fetch fitness classes data from your backend API
      axios.get('http://localhost:8000/api/v1/fitnessclass')
        .then(response => {
          this.fitnessClasses = response.data.data.fitnessclass;
        })
        .catch(error => {
          console.error('Error fetching fitness classes:', error);
        });
    },
  };
  </script>
  
  <style scoped>
  /* Add any custom styles specific to this component */
  </style>
  