<!-- navbar is not needed as its controlled at app.vue  -->
<template>
    <div class="container mt-2">
      <h1 class="text-center">Outlet Map</h1>
      <div id="map"></div>
      <div id="popup" class="popup"></div>
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
        scrollZoom: false,
        doubleClickZoom: false,
        // Provides options required to make requests to Amazon Location
        ...authHelper.getMapAuthenticationOptions(),
      });

      const controlContainer = document.getElementsByClassName('maplibregl-control-container')[0];
      if (controlContainer) {
          controlContainer.parentNode.removeChild(controlContainer);
      }

      // Add markers 
      const popupContent1 = `<h3>Fitness Studio 1</h3><p>Free weights, open gym</p>`;
      const popup1 = new maplibregl.Popup().setHTML(popupContent1);
      const marker1 = new maplibregl.Marker().setLngLat([104.129, 1.7521]).addTo(map);
      marker1.getElement().addEventListener('click', () => {
        popup1.setLngLat(marker1.getLngLat()).addTo(this.map);
      });

      const popupContent2 = `<h3>Fitness Studio 2</h3><p>Free weights, open gym</p>`;
      const popup2 = new maplibregl.Popup().setHTML(popupContent2);
      const marker2 = new maplibregl.Marker().setLngLat([104.229, 1.7521]).addTo(map);
      marker2.getElement().addEventListener('click', () => {
        popup2.setLngLat(marker2.getLngLat()).addTo(this.map);
      });


    },
  },
  head: {
    // Define CSP meta tag
    meta: [
      {
        httpEquiv: 'Content-Security-Policy',
        content: "script-src 'self' 'unsafe-eval';",
      },
    ],
  },
}
</script>
  
  
<style>
  /* Your custom styles can go here */
#map {
  height: 60vh;
  width: 100%;
}
</style>
  