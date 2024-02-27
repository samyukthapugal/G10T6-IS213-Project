# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# # Define a base URL for the fitness class microservice
# base_fitness_class_url = "http://localhost:5000"
# # userdatabase = "http://localhost:5001/user"

# @app.route("/complex_booking", methods=["GET", "POST"])
# def complex_booking():
#     # Check if the request method is GET
#     if request.method == "GET":
#         try:
#             # Make a request to get all fitness classes
#             all_classes_response = requests.get(f"{base_fitness_class_url}/fitnessclass")
#             all_classes_data = all_classes_response.json()

#             # Include all fitness classes details in the response for the GET request
#             response_data = {
#                 "code": 200,
#                 "message": "Complex booking endpoint is up.",
#                 "all_fitness_classes": all_classes_data["data"]["fitnessclass"]
#             }
#             return jsonify(response_data), 200

#         except Exception as e:
#             # Log the exception for debugging and return an error response for the GET request
#             app.logger.error(f"An error occurred: {str(e)}")
#             return jsonify({"code": 500, "message": "Internal Server Error."}), 500

#     # If the request method is POST
#     try:
#         data = request.get_json()

#         # Validate if data is None
#         if data is None:
#             return jsonify({"code": 400, "message": "Invalid JSON format in the request body."}), 400

#         # Validate required parameters for the POST request
#         if "class_id" not in data:
#             return jsonify({"code": 400, "message": "Missing required parameters."}), 400

#         # Extract data from the request
#         class_id = data["class_id"]

#         # Get fitness class details from the fitness class microservice
#         class_response = requests.get(f"{base_fitness_class_url}/fitnessclass/{class_id}")

#         # Check if the fitness class microservice request was successful
#         if class_response.status_code == 200:
#             class_details = class_response.json()

#             # Perform complex booking logic here
#             # You can implement your specific booking logic based on class details and all classes data

#             # Include all fitness classes details in the response for the successful POST request
#             response_data = {
#                 "code": 200,
#                 "message": "Complex booking successful.",
#                 "all_fitness_classes": all_classes_data["data"]["fitnessclass"]
#             }
#             return jsonify(response_data), 200
#         else:
#             # Handle the case where the fitness class details request failed for the POST request
#             return jsonify({"code": class_response.status_code, "message": "Failed to retrieve fitness class details."}), class_response.status_code

#     except Exception as e:
#         # Log the exception for debugging and return an error response for the POST request
#         app.logger.error(f"An error occurred: {str(e)}")
#         return jsonify({"code": 500, "message": "Internal Server Error."}), 500

# if __name__ == "__main__":
#     # Run the Flask app on host 0.0.0.0 and port 5100 in debug mode
#     app.run(host="0.0.0.0", port=5100, debug=True)

# # able to book
# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import requests

# app = Flask(__name__)
# CORS(app)

# # Define a base URL for the fitness class microservice
# base_fitness_class_url = "http://localhost:5000"

# @app.route("/complex_booking", methods=["POST"])
# def complex_booking():
#     try:
#         data = request.get_json()

#         if data is None or "class_id" not in data or "user_id" not in data:
#             return jsonify({"code": 400, "message": "Invalid or missing parameters."}), 400

#         class_id = data["class_id"]
#         user_id = data["user_id"]

#         # Get fitness class details from the fitness class microservice
#         class_response = requests.get(f"{base_fitness_class_url}/fitnessclass/{class_id}")

#         if class_response.status_code == 200:
#             class_details = class_response.json()

#             # Perform complex booking logic here

#             response_data = {
#                 "code": 200,
#                 "message": "Complex booking successful.",
#                 "class_details": class_details,
#             }
#             return jsonify(response_data), 200
#         else:
#             return jsonify({"code": class_response.status_code, "message": "Failed to retrieve fitness class details."}), class_response.status_code

#     except Exception as e:
#         app.logger.error(f"An error occurred: {str(e)}")
#         return jsonify({"code": 500, "message": "Internal Server Error."}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5100, debug=True)


# trying to update the fitnessclass number when its booked


from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Define a base URL for the fitness class microservice
base_fitness_class_url = "http://localhost:5000"

@app.route("/complex_booking", methods=["POST"])
def complex_booking():
    try:
        data = request.get_json()

        if data is None or "class_id" not in data or "user_id" not in data:
            return jsonify({"code": 400, "message": "Invalid or missing parameters."}), 400

        class_id = data["class_id"]
        user_id = data["user_id"]

        # Get fitness class details from the fitness class microservice
        class_response = requests.get(f"{base_fitness_class_url}/fitnessclass/{class_id}")

        if class_response.status_code == 200:
            class_details = class_response.json()

            # Perform complex booking logic here

            # Make a request to update availability in fitnessclass service
            update_availability_response = requests.post(
                f"{base_fitness_class_url}/book_fitness_class",
                json={"class_id": class_id, "user_id": user_id}
            )

            if update_availability_response.status_code == 200:
                # If updating availability is successful, continue with complex booking logic
                response_data = {
                    "code": 200,
                    "message": "Complex booking successful.",
                    "class_details": class_details,
                }
                return jsonify(response_data), 200
            else:
                # If updating availability fails, return the error response
                return jsonify({
                    "code": update_availability_response.status_code,
                    "message": f"Failed to update fitness class availability: {update_availability_response.json()['message']}"
                }), update_availability_response.status_code

        else:
            return jsonify({"code": class_response.status_code, "message": "Failed to retrieve fitness class details."}), class_response.status_code

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error."}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
