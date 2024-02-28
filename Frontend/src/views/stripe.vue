<template>
  <div class="container mt-5">
    <h1 class="text-center">Payment Page</h1>

    <!-- Add your payment form here -->
    <form @submit.prevent="initiatePayment">
      <!-- Add your payment form fields and styling here -->
      <button type="submit">Pay Now</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      localClassId: null,
    };
  },
  mounted() {
    // Assign the value of classId from query parameters to the local data property
    this.localClassId = this.$route.query.classId;

    // Log classId and userId to the console
    console.log('Class ID:', this.localClassId);
    console.log('User ID:', this.$route.query.userId);
  },
  methods: {
    initiatePayment() {
      // Redirect to the desired URL
      window.location.href = 'http://localhost:4242/';
    },
  },
};
</script>
