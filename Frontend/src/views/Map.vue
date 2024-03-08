<!-- navbar is not needed as its controlled at app.vue  -->
<template>
    <div class="container mt-2">
      <h1 class="text-center">Outlet Map</h1>
      <div id="map"></div>
      <!-- Bootstrap Card -->
    </div>
</template>

  <script>
  // need to install these 2 import
  import maplibregl from 'maplibre-gl';
  import { withIdentityPoolId } from '@aws/amazon-location-utilities-auth-helper';
  
  export default {
    name: 'MapComponent',
    mounted() {
      this.initializeMap();
    },
    methods: {
      async initializeMap() {
        const identityPoolId = "ap-southeast-1:8d67be78-b00d-4394-8dfe-28e4d6ccd7c7";
        const mapName = "js-map-with-marker-and-popup";
        const region = identityPoolId.split(":")[0];
  
        // Create an authentication helper instance using credentials from Cognito
        const authHelper = await withIdentityPoolId(identityPoolId);
  
        // Initialize the map
        const map = new maplibregl.Map({
          container: "map",
          // Initial map centerpoint
          center: [103.8198, 1.3521],
          // Initial zoom level
          zoom: 10,
          style: `https://maps.geo.${region}.amazonaws.com/maps/v0/maps/${mapName}/style-descriptor`,
          hash: true,
          // Provides options required to make requests to Amazon Location
          ...authHelper.getMapAuthenticationOptions(),
        });
  
        // Add navigation controls

        // Configure a new popup
        const popup = new maplibregl.Popup({
          offset: 35,
        }).setHTML(`<h3>Fitness Studio 1</h3><p>Free weights, open gym</p>`);
        // Add markers and popups
        new maplibregl.Marker()
                .zoom(this.zoom)
                .setLngLat([103.8198, 1.3521])
                .setPopup(popup)
                .addTo(map);
  
        new maplibregl.Marker()
          .setLngLat([103.8198, 1.3521])
          .setPopup(popup)
          .addTo(map);
      },
    }
  };
  </script>
  
<style>
  /* Your custom styles can go here */
#map {
  height: 60vh;
  width: 100%;
}
</style>
  