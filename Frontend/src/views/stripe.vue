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
      <!-- For example, you can include input fields for card details, etc. -->

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
      // Add other necessary data properties for the payment form
    };
  },
  mounted() {
    // Assign the value of classId from query parameters to the local data property
    this.localClassId = this.$route.query.classId;

    // Log classId and userId to the console
    console.log('Class ID:', this.localClassId);
    console.log('User ID:', this.$route.query.userId);
    console.log('User email:', this.$route.query.email);
  },
  methods: {
    confirmPurchase() {
      // Display a confirmation message (you can customize this part)
      // If confirmed, directly redirect to index.html with user id and class id
      const userId = this.$route.query.userId;
      const email = this.$route.query.email;
      const redirectUrl = `http://127.0.0.1:4242/?userId=${userId}&classId=${this.localClassId}&email=${email}`;
      window.location.href = redirectUrl;
    },
  },
};
</script>
