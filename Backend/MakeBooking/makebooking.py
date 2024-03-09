from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
base_fitness_class_url = "http://localhost:5000"
user_booking_url = "http://localhost:5001"


@app.route("/complex_booking", methods=["POST"])

def complex_booking():
    try:
        data = request.get_json()

        if data is None or "class_id" not in data or "user_id" not in data:
            return jsonify({"code": 400, "message": "Invalid or missing parameters."}), 400

        class_id = data["class_id"]   #pass in from mainpage.vue
        user_id = data["user_id"]    #pass in from mainpage.vue

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

                # Make a request to the user booking service to update selected fitness classes
                user_booking_response = requests.post(
                    f"{user_booking_url}/user",
                    json={"userId": user_id, "selectedFitnessClasses": [class_id]}
                )

                if user_booking_response.status_code == 200:
                    # If updating user booking is successful, return the response
                    response_data = {
                        "code": 200,
                        "message": "Complex booking and user booking update successful.",
                        "class_details": class_details,
                    }
                    return jsonify(response_data), 200
                else:
                    # If updating user booking fails, log the error and return the error response
                    app.logger.error(f"Failed to update user booking: {user_booking_response.json()}")
                    return jsonify({
                        "code": user_booking_response.status_code,
                        "message": f"Failed to update user booking: {user_booking_response.json()['message']}"
                    }), user_booking_response.status_code

            else:
                # If updating availability fails, log the error and return the error response
                app.logger.error(f"Failed to update fitness class availability: {update_availability_response.json()}")
                return jsonify({
                    "code": update_availability_response.status_code,
                    "message": f"Failed to update fitness class availability: {update_availability_response.json()['message']}"
                }), update_availability_response.status_code

        else:
            # If failed to retrieve fitness class details, log the error and return the error response
            app.logger.error(f"Failed to retrieve fitness class details. Status code: {class_response.status_code}")
            return jsonify({"code": class_response.status_code, "message": "Failed to retrieve fitness class details."}), class_response.status_code

    except Exception as e:
        # Log any other unexpected exceptions
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
