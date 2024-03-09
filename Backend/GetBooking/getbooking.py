from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
base_fitness_class_url = "http://localhost:5000"
user_booking_url = "http://localhost:5001"

@app.route("/get_booking/<user_id>", methods=["GET"])
def get_booking(user_id):
    try:
        # Query the database to get all booked classes for the specified user
        booked_classes_response = requests.get(f"{user_booking_url}/user/bookedClasses/{user_id}")

        if booked_classes_response.status_code == 200:
            booked_classes_data = booked_classes_response.json().get("data", {})
            booked_classes = booked_classes_data.get("booked_classes", [])

            # List to store details of booked classes
            booked_classes_details = []

            for booked_class in booked_classes:
                class_id = booked_class.get("class_id")
                unique_id = booked_class.get("unique_id")

                # Fetch the fitness class details from the FitnessClass microservice
                fitness_class_response = requests.get(f"{base_fitness_class_url}/fitnessclass/{class_id}")

                if fitness_class_response.status_code == 200:
                    fitness_class_details = fitness_class_response.json().get("data", {})
                    # Append fitness class details along with unique_id to the list
                    booked_classes_details.append({
                        "class_id": class_id,
                        "unique_id": unique_id,
                        "fitness_class_details": fitness_class_details
                    })
                else:
                    print(f"Failed to fetch fitness class details for class_id {class_id}. "
                          f"Status code: {fitness_class_response.status_code}")
                    
            return jsonify({"code": 200, "data": {"booked_classes": booked_classes_details}})
        else:
            return jsonify({"code": booked_classes_response.status_code, "message": "Error fetching booked classes"}), booked_classes_response.status_code

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5101, debug=True)
