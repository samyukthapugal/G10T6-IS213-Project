from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
complex_getbooking_url = "http://localhost:5101"
ratings_url = "http://localhost:5004"

@app.route("/make_review", methods=["GET", "POST"])
def make_review():
    if request.method == "POST":
        # make sure the parameter name is the same as booking.vue one
        data = request.get_json()
        class_id = data.get("classId")
        selectedRating = data.get("selectedRating")
        user_id = data.get('user', {}).get('uid')
        # print(data)
        print(class_id)
        print(selectedRating)
        print(user_id)

        # Fetch all ratings for the specific class from ratings.py
        all_ratings_response = requests.get(f"{ratings_url}/rating")
        
        print(all_ratings_response.text)
        
        if all_ratings_response.status_code == 200:
            
            all_ratings_data = all_ratings_response.json().get("data", {})
            
            class_ratings = [rating_entry["rating"] for rating_entry in all_ratings_data.get("rating", []) if rating_entry["class_id"] == str(class_id)]

            
            print(class_ratings)
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
            else:
                print(f"Failed to update average rating for class {class_id}. Status code: {put_response.status_code}")

            # Your remaining logic here
            # FROM HERE should call the get

            return jsonify({"message": "Review submitted successfully.", "average_rating": average_rating})

        else:
            print(f"Failed to fetch ratings from {ratings_url}. Status code: {all_ratings_response.status_code}")
            return jsonify({"message": "Failed to fetch ratings.", "average_rating": 0})

    elif request.method == "GET":
        # Handle GET request
        return jsonify({"message": "This is a GET request."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
