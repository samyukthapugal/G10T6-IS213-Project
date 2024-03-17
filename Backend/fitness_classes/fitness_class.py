from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS
from sqlalchemy.sql import text


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    environ.get("dbURL") or "mysql+mysqlconnector://root@localhost:3306/fitnessclass"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 299}

db = SQLAlchemy(app)

CORS(app)

class FitnessClass(db.Model):
    __tablename__ = "fitnessclass"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructor = db.Column(db.String(64), nullable=False)
    schedule = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    availability = db.Column(db.Integer)

    def __init__(self, name, description, instructor, schedule, price, availability):
        self.name = name
        self.description = description
        self.instructor = instructor
        self.schedule = schedule
        self.price = price
        self.availability = availability

    def json(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "instructor": self.instructor,
            "schedule": self.schedule,
            "price": float(self.price),  # Convert price to float if needed
            "availability": self.availability,
        }

# This function is to get all the fitnessclass data that is in the database
@app.route("/fitnessclass")
def get_all():
    try:
        fitness_classes = FitnessClass.query.all()
        return jsonify({"code": 200, "data": {"fitnessclass": [fc.json() for fc in fitness_classes]}})
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving fitness classes: {str(e)}")
        return jsonify({"code": 500, "message": "Failed to retrieve fitness class details."}), 500

# This function is to get a specific fitness class data details from the database
@app.route("/fitnessclass/<string:id>")
def find_by_id(id):
    try:
        fitness_class = FitnessClass.query.get(id)

        if fitness_class:
            return jsonify({"code": 200, "data": fitness_class.json()})
        else:
            return jsonify({"code": 404, "message": "Fitness class not found."}), 404
    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error."}), 500


# This function is to update the number of classes available 
@app.route("/book_fitness_class", methods=["POST"])
def book_fitness_class():
    try:
        data = request.get_json()

        # Validate required parameters
        if "class_id" not in data or "user_id" not in data:
            return jsonify({"code": 400, "message": "Missing required parameters."}), 400

        # Extract data from the request
        class_id = data["class_id"]
        user_id = data["user_id"]

        # Check if the class exists
        fitness_class = FitnessClass.query.get(class_id)
        if not fitness_class:
            return jsonify({"code": 404, "message": "Fitness class not found."}), 404

        # Check if there are available slots
        if fitness_class.availability > 0:
            # If there are available slots, decrement the availability and save to the database
            fitness_class.availability -= 1
            db.session.commit()

            # Implement your logic to store the booking information, e.g., in a separate table

            return jsonify({"code": 200, "message": "Booking successful."}), 200
        else:
            return jsonify({"code": 403, "message": "No available slots for this class."}), 403

    except Exception as e:
        # Log the exception for debugging
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error."}), 500

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
