<template>
    <div class="container mt-5">
      <h1 class="text-center">Payment Page</h1>
  
      <!-- Payment form -->
      <form @submit.prevent="initiatePayment">
        <!-- Card details -->
        <div id="card-element">
          <!-- A Stripe Element will be inserted here. -->
        </div>
  
        <!-- Display form errors -->
        <div id="card-errors" role="alert"></div>
  
        <!-- Additional form fields (customize as needed) -->
        <label for="name">Name on Card:</label>
        <input type="text" id="name" v-model="cardholderName" required />
  
        <!-- Button to submit the payment -->
        <button type="submit" :disabled="processing">Pay Now</button>
  
        <!-- Display a loading spinner during payment processing -->
        <div v-if="processing" class="loading-spinner"></div>
      </form>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        localClassId: null,
        cardholderName: '',
        stripe: null,
        elements: null,
        cardElement: null,
        processing: false, // Flag to indicate payment processing
      };
    },
    mounted() {
      this.localClassId = this.$route.query.classId;
  
      // Log classId and userId to the console
      console.log('Class ID:', this.localClassId);
      console.log('User ID:', this.$route.query.userId);
  
      this.stripe = Stripe('pk_12345');
      this.elements = this.stripe.elements();
  
      this.cardElement = this.elements.create('card');
      this.cardElement.mount('#card-element');
    },
    methods: {
      async initiatePayment() {
        try {
          // Disable the submit button during payment processing
          this.processing = true;
  
          // Create a PaymentIntent on your server
          const response = await axios.post('http://localhost:4242/create-payment-intent', {
            class_id: this.localClassId,
            user_id: this.$route.query.userId,
            cardholder_name: this.cardholderName,
          });
  
          // Handle the response from the server (customize as needed)
          if (response.data.requires_action) {
            // If additional authentication is required
            const { error: actionError, paymentIntent } = await this.stripe.confirmCardPayment(
              response.data.client_secret,
              { payment_method: response.data.payment_method }
            );
  
            if (actionError) {
              // Handle the error (e.g., show error message to the user)
              console.error('Error confirming payment:', actionError);
            } else {
              // Payment is confirmed
              this.handlePaymentSuccess(paymentIntent);
            }
          } else {
            // No additional authentication required
            this.handlePaymentSuccess(response.data.paymentIntent);
          }
        } catch (error) {
          // Handle errors
          console.error('Error processing payment:', error);
        } finally {
          // Enable the submit button after payment processing
          this.processing = false;
        }
      },
  
      handlePaymentSuccess(paymentIntent) {
        // Handle successful payment (e.g., show success message, redirect, etc.)
        console.log('💰 Payment received!', paymentIntent);
  
        // Perform additional actions (e.g., call complex_booking service)
        this.callComplexBookingService();
  
        // Optionally, redirect or display a success message to the user
        this.$router.push('/success'); // Replace with your success page
      },
  
      async callComplexBookingService() {
        // Call the complex_booking service (customize as needed)
        try {
          await axios.post('http://localhost:5100/complex_booking', {
            class_id: this.localClassId,
            user_id: this.$route.query.userId,
          });
        } catch (error) {
          // Handle errors in complex_booking service call
          console.error('Error calling complex_booking service:', error);
        }
      },
    },
  };
  </script>
  
  <style>
  .loading-spinner {
    border: 4px solid rgba(0, 0, 0, 0.1);
    border-left: 4px solid #3498db;
    border-radius: 50%;
    width: 30px;
    height: 30px;
    animation: spin 1s linear infinite;
  }
  
  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }
  </style>
  
  