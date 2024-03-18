from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
complex_getbooking_url = "http://makebooking:5100"
ratings_url = "http://rating:5004"
user_booking_url = "http://userbooking:5010"

@app.route("/make_review", methods=["GET", "POST"])
def make_review():
    if request.method == "POST":
        # make sure the parameter name is the same as booking.vue one
        data = request.get_json()
        class_id = data.get("classId")
        selectedRating = data.get("selectedRating")
        user_id = data.get('user', {}).get('uid')
        
        # Fetch all ratings for the specific class from ratings.py
        all_ratings_response = requests.get(f"{ratings_url}/rating")
        
        if all_ratings_response.status_code == 200:
            all_ratings_data = all_ratings_response.json().get("data", {})
            
            class_ratings = [rating_entry["rating"] for rating_entry in all_ratings_data.get("rating", []) if rating_entry["class_id"] == str(class_id)]

            # Calculate the average rating
            if class_ratings:
                average_rating = sum(class_ratings + [selectedRating]) / (len(class_ratings) + 1)
            else:
                average_rating = 0  # Default to 0 if there are no ratings

            # Update the average rating in rating.py using a PUT request
            put_response = requests.put(f"{ratings_url}/update_average/{class_id}", json={"average_rating": average_rating})
            
            # Check if the PUT request was successful
            if put_response.status_code == 200:
                print(f"Class {class_id} average rating updated successfully.")
                
                # Send additional data to user_booking service
                user_booking_data = {
                    "user_id": user_id,
                    "class_id": class_id,
                    "unique_id": data.get("unique_id")
                }
                
                # Send a PUT request to user_booking service
                user_booking_response = requests.put(f"{user_booking_url}/update_rate_status", json=user_booking_data)
                
                if user_booking_response.status_code == 200:
                    print(f"Rate status updated successfully for user {user_id} and class {class_id}.")
                else:
                    print(f"Failed to update rate status for user {user_id} and class {class_id}. "
                          f"Status code: {user_booking_response.status_code}")

            else:
                print(f"Failed to update average rating for class {class_id}. Status code: {put_response.status_code}")

            return jsonify({"message": "Review submitted successfully.", "average_rating": average_rating})

        else:
            print(f"Failed to fetch ratings from {ratings_url}. Status code: {all_ratings_response.status_code}")
            return jsonify({"message": "Failed to fetch ratings.", "average_rating": 0})

    elif request.method == "GET":
        # Handle GET request
        return jsonify({"message": "This is a GET request."})
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
