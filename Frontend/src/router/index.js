// router.js
import { createRouter, createWebHistory } from 'vue-router';
import { getAuth, onAuthStateChanged } from 'firebase/auth'; // Uncomment this line

const router = createRouter({
  history: createWebHistory(),
  routes: [
    { path: '/', component: () => import('../views/Home.vue') },
    { path: '/mainpage', component: () => import('../views/Mainpage.vue') },
    { path: '/register', component: () => import('../views/Register.vue') },
    { path: '/sign-in', component: () => import('../views/SignIn.vue') },
    { path: '/map', component: () => import('../views/Map.vue') },
    { 
      path: '/booking', 
      component: () => import('../views/Booking.vue'),
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/stripe',
      component: () => import('../views/stripe.vue'),
      name: 'stripe'
    }
    // add more routes for more navbar options
  ],
});

const getCurrentUser = () => {
  return new Promise((resolve, reject) => {
    const removeListener = onAuthStateChanged(getAuth(), (user) => {
      removeListener();
      resolve(user);
    }, reject);
<<<<<<< Updated upstream
  }).catch((error) => {
    console.error('Error in getCurrentUser:', error);

=======
  })
  .catch(error => {
    // Handle the error here
    console.error('Error fetching current user:', error);
    throw error; // Rethrow the error to propagate it further if needed
>>>>>>> Stashed changes
  });
};


router.beforeEach(async (to, from, next) => {
  const auth = getAuth();

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (await getCurrentUser()) {
      next();
    } else {
      alert("You don't have access!");
      next('/');
    }
  } else {
    // Allow navigation for routes that do not require authentication
    next();
  }
});

export default router;



