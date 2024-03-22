<template>
  <div class="container mt-2">
    <h1 class="text-center">Amazon Location Service Map</h1>
    <object style="width:100vh; height:100vh; margin:1%;" data="http://localhost:5501/Map/index.html#10/1.3521/103.8198"></object>
  </div>
</template>

<script>
import maplibregl from 'maplibre-gl';
import { withIdentityPoolId } from '@aws/amazon-location-utilities-auth-helper';

export default {
  name: 'AmazonLocationMap',
  data() {
    return {
      showPopup: false,
      popupTitle: '',
      popupContent: '',
      popupTop: 0,
      popupLeft: 0,
    };
  },
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
        // Disable scroll and zoom
        scrollZoom: false,
        doubleClickZoom: false,
        touchZoomRotate: false,
        // Provides options required to make requests to Amazon Location
        ...authHelper.getMapAuthenticationOptions(),
      });

      // Remove the maplibregl-control-container div
      const controlContainer = document.getElementsByClassName('maplibregl-control-container')[0];
      if (controlContainer) {
          controlContainer.parentNode.removeChild(controlContainer);
      }


      // Add navigation controls
      map.addControl(new maplibregl.NavigationControl(), "top-left");

      // Add markers
      const marker1 = new maplibregl.Marker().setLngLat([104.129, 1.7521]).addTo(map);
      const marker2 = new maplibregl.Marker().setLngLat([104.229, 1.7521]).addTo(map);
      
      // Event listener for marker click to show popup
      marker1.getElement().addEventListener('click', () => {
        this.showPopup = true;
        this.popupTitle = "Location 1";
        this.popupContent = "Details for Marker 1";
        const markerPos = marker1.getLngLat();
        this.popupTop = markerPos.lat + 100; // Adjust as needed
        this.popupLeft = markerPos.lng + 100; // Adjust as needed
      });

      marker2.getElement().addEventListener('click', () => {
        this.showPopup = true;
        this.popupTitle = "Location 2";
        this.popupContent = "Details for Marker 2";
        const markerPos = marker2.getLngLat();
        this.popupTop = markerPos.lat + 100; // Adjust as needed
        this.popupLeft = markerPos.lng + 100; // Adjust as needed
      });

      // Add styles for markers
      marker1.getElement().style.cursor = 'pointer';
      marker2.getElement().style.cursor = 'pointer';

      // Hover effect for markers
      marker1.getElement().addEventListener('mouseenter', () => {
        marker1.getElement().style.color = 'red'; // Change color on hover
      });
      marker1.getElement().addEventListener('mouseleave', () => {
        marker1.getElement().style.color = 'blue'; // Change color back on mouse leave
      });

      marker2.getElement().addEventListener('mouseenter', () => {
        marker2.getElement().style.color = 'red'; // Change color on hover
      });
      marker2.getElement().addEventListener('mouseleave', () => {
        marker2.getElement().style.color = 'blue'; // Change color back on mouse leave
      });
    },
    closePopup() {
      this.showPopup = false;
    }
  }
};
</script>

<style>
/* Your custom styles can go here */
#map {
  height: 70vh;
  width: 100%;
}
.popup {
  position: absolute;
  background-color: white;
  border: 1px solid #ccc;
  padding: 10px;
  z-index: 9999; /* Adjust as needed */
}
.popup button {
  display: block;
  margin-top: 10px;
  border: none;
  background: none;
  cursor: pointer;
}
</style>
