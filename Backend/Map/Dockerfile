# Use the official httpd image as the base
FROM httpd:latest

# Copy your HTML, CSS, and JavaScript files into the appropriate directory
COPY index.html /usr/local/apache2/htdocs/
COPY location_data.json /usr/local/apache2/htdocs/

# Expose port 80 (the default port used by Apache HTTP Server)
EXPOSE 80
