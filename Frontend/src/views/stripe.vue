<template>
  <div class="container mt-5">
    <h1 class="text-center mb-4">Confirmation Page</h1>

    <!-- Confirmation Content -->
    <form>
      <!-- Add your confirmation details here -->
      <div class="alert alert-info" role="alert">
        Please review your order details before confirming the purchase.
      </div>

      <!-- Add your payment form fields and styling here -->

      <!-- Proceed to Payment Button -->
      <button type="button" class="btn btn-success" @click="confirmPurchase">
        Confirm Purchase
      </button>
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
    confirmPurchase() {
      // Display a confirmation message (you can customize this part)
      
        // If confirmed, initiate payment
        this.initiatePayment();
      
    },
    initiatePayment() {
      // Redirect to the payment page with classId and userId as query parameters
      window.location.href = `http://localhost:4242/?classId=${this.localClassId}&userId=${this.$route.query.userId}`;
    },
  },
};
</script>

