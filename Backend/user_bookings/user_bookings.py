
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/userbooking"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "userbooking"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userid = db.Column(db.String(64), nullable=False)
    class_id = db.Column(db.Integer, nullable=False)
    rate_status = db.Column(db.String(64), nullable=False)
    unique_id = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(64))

    def __init__(self, userid, class_id, rate_status, unique_id, email):
        self.userid = userid
        self.class_id = class_id
        self.rate_status = rate_status
        self.unique_id = unique_id
        self.email = email
        
    def json(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "class_id": self.class_id,
            "rate_status": self.rate_status,
            "unique_id": self.unique_id,
            "email": self.email
        }


import uuid  # Add this import for generating unique IDs

@app.route('/user', methods=['POST'])
def add_Booked_Class():
    try:
        data = request.get_json()
        user_id = data.get('userId')
        email = data.get("email")
        selected_fitness_classes = data.get('selectedFitnessClasses')

        print(f"Received data: {data}") 
        if not user_id or not selected_fitness_classes:
            print("Missing required parameters.")
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        classes = []
        for class_id in selected_fitness_classes:
            # Generate a unique_id using UUID
            unique_id = str(uuid.uuid4())  # Convert UUID to string

            # Save the provided details to the database with default rate_status "NO" and generated unique_id
            user = User(userid=user_id, class_id=class_id, rate_status="NO", unique_id=unique_id,email=email)
            db.session.add(user)
            classes.append(user.json())

            print(f"User details added for class_id {class_id} with unique_id {unique_id}")

        db.session.commit()

        return jsonify({"message": "User's selected fitness classes updated successfully", "classes": classes}), 200

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500



@app.route('/user/bookedClasses/<user_id>', methods=['GET'])
def get_booked_classes(user_id):
    try:
        # Query the database to get all booked classes for the specified user
        booked_classes = User.query.filter_by(userid=user_id).all()

        # Check if there are any booked classes
        if not booked_classes:
            return jsonify({"code": 404, "message": "No booked classes found for the user."}), 404

        # List to store details of booked classes
        booked_classes_details = []

        # Iterate through booked classes and fetch class IDs and unique IDs
        for booked_class in booked_classes:
            class_id = booked_class.class_id
            unique_id = booked_class.unique_id

            # Append class ID and unique ID to the list
            booked_classes_details.append({"class_id": class_id, "unique_id": unique_id})

        return jsonify({"code": 200, "data": {"booked_classes": booked_classes_details}})

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500


@app.route('/update_rate_status', methods=['PUT'])
def update_rate_status():
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        class_id = data.get('class_id')
        unique_id = data.get('unique_id')

        # Check if all required parameters are present
        if not user_id or not class_id or not unique_id:
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        # Query the database to get the user_booking entry with the specified unique_id
        user_booking_entry = User.query.filter_by(userid=user_id, class_id=class_id, unique_id=unique_id).first()

        # Check if the user_booking entry is found
        if not user_booking_entry:
            return jsonify({"code": 404, "message": "User booking entry not found."}), 404

        # Update the rate_status to "YES"
        user_booking_entry.rate_status = "YES"
        db.session.commit()

        return jsonify({"message": "Rate status updated successfully.", "user_id": user_id, "class_id": class_id, "unique_id": unique_id}), 200

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
