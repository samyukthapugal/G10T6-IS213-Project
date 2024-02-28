from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy
# this is the connection to sql database
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/userbooking"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "userbooking"
    # id here is for numbering 
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # this userid is to track which user this belongs too that login with the firebase thing
    userid = db.Column(db.String(64), nullable=False)
    # the class id is the fitness class id between 1-6 
    class_id = db.Column(db.Integer, nullable=False)  # Add this line for class_id
    # the description here is just the content details of the fitness class
    description = db.Column(db.Text, nullable=False)
    # instructor that is teaching
    instructor = db.Column(db.String(64), nullable=False)
    # the schedule available 
    schedule = db.Column(db.String(255), nullable=False)
    # the price of the class
    price = db.Column(db.Float(precision=2), nullable=False)
    
    

    def __init__(self, class_id, userid, description, instructor, schedule, price):
        self.class_id = class_id
        self.userid = userid
        self.description = description
        self.instructor = instructor
        self.schedule = schedule
        self.price = price

    def json(self):
        return {
            "id": self.id,
            "class_id": self.class_id,  # Include class_id in the JSON representation
            "userid": self.userid,
            "description": self.description,
            "instructor": self.instructor,
            "schedule": self.schedule,
            "price": float(self.price),  # Convert price to float if needed
        }


# below this function is for when the complex booking microservice pass in the selected class id and user id to record the booking to the user database
@app.route('/user', methods=['POST'])
def receive_user_id():
    try:
        data = request.get_json()
        user_id = data.get('userId')
        selected_fitness_classes = data.get('selectedFitnessClasses')

        print(f"Received data: {data}") 
        if not user_id or not selected_fitness_classes:
            print("Missing required parameters.")  # Add this line to print the error message
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        # Assuming selected_fitness_classes is a list of class ids
        classes = []
        for class_id in selected_fitness_classes:
            # Fetch the fitness class details from the complex booking service
            class_response = requests.get(f"http://localhost:5000/fitnessclass/{class_id}").json()  #using .json() to get the fitness class details otherwise if dont have it returns <Response[200]>
            print(class_response)
            print(f"Fetching class details for class_id {class_id}")  # Add this line to print class_id

            if class_response.get('code') == 200: # check if can get the url data stuff
                class_details = class_response.get('data')

                # Save the fetched details to the database
                user = User(
                    class_id=class_id, # this is pass in from complexbooking
                    userid=user_id, # this is pass in from complexbooking
                    description=class_details.get("description", ""),
                    instructor=class_details.get("instructor", ""),
                    schedule=class_details.get("schedule", ""),
                    price=class_details.get("price", 0.0)
                )

                db.session.add(user)
                classes.append(user.json())

                print(f"User details added for class_id {class_id}")  # Add this line to print class_id

            else:
                print(f"Failed to fetch fitness class details for class_id {class_id}. "
                     f"Status code: {class_response.get('code', '')}, "
                     f"Message: {class_response.get('message', '')}")
                return jsonify({
                    "code": class_response.get('code', ''),
                    "message": f"Failed to fetch fitness class details: {class_response.get('message', '')}"
                }), class_response.get('code', '')

        db.session.commit() # adding the data to database

        return jsonify({"message": "User's selected fitness classes updated successfully", "classes": classes}), 200

    except Exception as e:
        print(f"An error occurred: {str(e)}")  # Add this line to print the error message
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
