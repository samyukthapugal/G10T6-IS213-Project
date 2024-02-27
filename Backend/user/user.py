from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import requests

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
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(64), nullable=False)
    schedule = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)

    def __init__(self, userid, description, instructor, schedule, price):
        self.userid = userid
        self.description = description
        self.instructor = instructor
        self.schedule = schedule
        self.price = price

    def json(self):
        return {
            "id": self.id,
            "userid": self.userid,
            "description": self.description,
            "instructor": self.instructor,
            "schedule": self.schedule,
            "price": float(self.price),  # Convert price to float if needed
        }

@app.route('/user', methods=['POST'])
def receive_user_id():
    try:
        data = request.get_json()
        user_id = data.get('userId')
        selected_fitness_classes = data.get('selectedFitnessClasses')

        if not user_id or not selected_fitness_classes:
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        # Assuming selected_fitness_classes is a list of class ids
        classes = []
        for class_id in selected_fitness_classes:
            # Fetch the fitness class details from the complex booking service
            class_response = requests.get(f"http://localhost:5000/fitnessclass/{class_id}")

            if class_response.status_code == 200:
                class_details = class_response.json()

                # Save the fetched details to the database
                user = User(
                    userid=user_id,
                    description=class_details.get("description", ""),
                    instructor=class_details.get("instructor", ""),
                    schedule=class_details.get("schedule", ""),
                    price=class_details.get("price", 0.0)
                )
                db.session.add(user)
                classes.append(user.json())

                # Update availability in fitness class service
                update_availability_response = requests.post(
                    f"http://localhost:5000/book_fitness_class",
                    json={"class_id": class_id, "user_id": user_id}
                )

                if update_availability_response.status_code != 200:
                    app.logger.error(f"Failed to update fitness class availability: {update_availability_response.json()}")
                    return jsonify({
                        "code": update_availability_response.status_code,
                        "message": f"Failed to update fitness class availability: {update_availability_response.json()['message']}"
                    }), update_availability_response.status_code

            else:
                app.logger.error(f"Failed to fetch fitness class details for class_id {class_id}. "
                                 f"Status code: {class_response.status_code}, "
                                 f"Message: {class_response.json().get('message', '')}")
                return jsonify({
                    "code": class_response.status_code,
                    "message": f"Failed to fetch fitness class details: {class_response.json().get('message', '')}"
                }), class_response.status_code

        db.session.commit()

        return jsonify({"message": "User's selected fitness classes updated successfully", "classes": classes}), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": f"Internal Server Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
