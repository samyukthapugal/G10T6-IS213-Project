from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
base_fitness_class_url = "http://localhost:5000"
user_booking_url = "http://localhost:5001"


@app.route("/complex_booking", methods=["POST"])
def make_booking():
    try:
        data = request.get_json()

        if data is None or "class_id" not in data or "user_id" not in data:
            return jsonify({"code": 400, "message": "Invalid or missing parameters."}), 400

        class_id = data["class_id"]   #pass in from success.html
        user_id = data["user_id"]    #pass in from success.html

        # Perform complex booking logic here
        # You can add any additional logic you need for complex booking

        # Make a request to the user booking service to update selected fitness classes
        user_booking_response = requests.post(
            f"{user_booking_url}/user",
            json={"userId": user_id, "selectedFitnessClasses": [class_id]}
        )

        if user_booking_response.status_code == 200:
            # If updating user booking is successful, return the response
            response_data = {
                "code": 200,
                "message": "User booking update successful.",
                "class_id": class_id,
                "user_id": user_id,
            }
            return jsonify(response_data), 200
        else:
            # If updating user booking fails, log the error and return the error response
            app.logger.error(f"Failed to update user booking: {user_booking_response.json()}")
            return jsonify({
                "code": user_booking_response.status_code,
                "message": f"Failed to update user booking: {user_booking_response.json()['message']}"
            }), user_booking_response.status_code

    except Exception as e:
        # Log any other unexpected exceptions
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5100, debug=True)
