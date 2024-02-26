from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Define a base URL for the fitness class microservice
base_fitness_class_url = "http://localhost:5000"

@app.route("/complex_booking", methods=["GET", "POST"])
def complex_booking():
    if request.method == "GET":
        try:
            # Make a request to get all fitness classes
            all_classes_response = requests.get(f"{base_fitness_class_url}/fitnessclass")
            all_classes_data = all_classes_response.json()

            # Include all fitness classes details in the response
            response_data = {
                "code": 200,
                "message": "Complex booking endpoint is up.",
                "all_fitness_classes": all_classes_data["data"]["fitnessclass"]
            }
            return jsonify(response_data), 200

        except Exception as e:
            # Log the exception for debugging
            app.logger.error(f"An error occurred: {str(e)}")
            return jsonify({"code": 500, "message": "Internal Server Error."}), 500

    try:
        data = request.get_json()

        # Validate if data is None
        if data is None:
            return jsonify({"code": 400, "message": "Invalid JSON format in the request body."}), 400

        # Validate required parameters
        if "class_id" not in data:
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        # Extract data from the request
        class_id = data["class_id"]

        # Get fitness class details from the fitness class microservice
        class_response = requests.get(f"{base_fitness_class_url}/fitnessclass/{class_id}")

        # Check if the fitness class microservice request was successful
        if class_response.status_code == 200:
            class_details = class_response.json()

            # Perform complex booking logic here
            # You can implement your specific booking logic based on class details and all classes data

            # Include all fitness classes details in the response
            response_data = {
                "code": 200,
                "message": "Complex booking successful.",
                "all_fitness_classes": all_classes_data["data"]["fitnessclass"]
            }
            return jsonify(response_data), 200
        else:
            # Handle the case where the fitness class details request failed
            return jsonify({"code": class_response.status_code, "message": "Failed to retrieve fitness class details."}), class_response.status_code

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
