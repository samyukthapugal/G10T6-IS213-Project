<template>
    <div class="container mt-5">
      <h1 class="text-center">Payment Page</h1>
  
      <!-- Add your payment form here -->
      <form @submit.prevent="initiatePayment">
        <!-- Add your payment form fields and styling here -->
        <div id="card-element">
          <!-- A Stripe Element will be inserted here. -->
        </div>
  
        <!-- Used to display form errors. -->
        <div id="card-errors" role="alert"></div>
  
        <button type="submit">Pay Now</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        localClassId: null, // Local data property to store the value of classId
        stripe: null,
        elements: null,
        cardElement: null,
      };
    },
    mounted() {
      // Assign the value of classId from query parameters to the local data property
      this.localClassId = this.$route.query.classId;
  
      // Log classId and userId to the console
      console.log('Class ID:', this.localClassId);
      console.log('User ID:', this.$route.query.userId);
  
      // Initialize Stripe.js with your publishable key
      this.stripe = Stripe('YOUR_PUBLISHABLE_KEY');
      this.elements = this.stripe.elements();
  
      // Create an instance of the card Element.
      this.cardElement = this.elements.create('card');
  
      // Add an instance of the card Element into the `card-element` div.
      this.cardElement.mount('#card-element');
    },
    methods: {
      async initiatePayment() {
        try {
          // Create a PaymentIntent on your server
          const response = await axios.post('http://localhost:4242/create-payment-intent', {
            class_id: this.localClassId,
            user_id: this.$route.query.userId,
          });
  
          // ... rest of the method remains unchanged
        } catch (error) {
          // Handle errors
          console.error('Error processing payment:', error);
        }
      },
    },
  };
  </script>
  