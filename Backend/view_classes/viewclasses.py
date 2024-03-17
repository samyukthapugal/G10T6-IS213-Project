from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Put the different simple microservice URL
base_fitness_class_url = "http://fitnessclass:5500"
ratings_url = "http://rating:5004"


@app.route("/view_classes", methods=["GET"])
def get_fitness_classes():
    try:
        # Make a request to the fitness class microservice
        class_response = requests.get(f"{base_fitness_class_url}/fitnessclass")

        # Check if the request was successful (status code 200)
        if class_response.status_code == 200:
            # Get the fitness class details from the response
            fitness_classes = class_response.json().get('data', {}).get('fitnessclass', [])
            
            # Return the fitness class details as a JSON response
            return jsonify({"code": 200, "data": {"fitnessclass": fitness_classes}})
        
        else:
            # If there's an error, return an error response with the status code and message
            return jsonify({"code": class_response.status_code, "message": "Error fetching fitness class details"}), class_response.status_code
    
    except Exception as e:
        # If an exception occurs during the request or JSON parsing, handle it
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return jsonify({"code": 500, "message": f"Internal Server Error: {error_message}"}), 500

    

@app.route("/view_rating", methods=["GET"])
def get_rating():
    try:
        # Make a request to the ratings microservice
        get_ratings = requests.get(f"{ratings_url}/rating")
        
        # Check if the request to the ratings microservice was successful
        if get_ratings.status_code == 200:
            # Get the ratings from the response
            get_all_ratings = get_ratings.json().get('data', {}).get('rating', [])  # Update property name to 'rating'
            
            print(get_all_ratings)
            return jsonify({"code": 200, "data": {"rating": get_all_ratings}})
        
        else:
            # If there's an error, return an error response with the status code and message
            return jsonify({"code": get_ratings.status_code, "message": "Error fetching fitness class details"}), get_ratings.status_code
    
    except Exception as e:
        # If an exception occurs during the request or JSON parsing, handle it
        error_message = f"An error occurred: {str(e)}"
        print(error_message)
        return jsonify({"code": 500, "message": f"Internal Server Error: {error_message}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5200, debug=True)

