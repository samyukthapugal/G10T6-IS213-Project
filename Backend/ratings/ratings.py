from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    environ.get("dbURL") or "mysql+mysqlconnector://root@localhost:3306/classRatings"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 299}

db = SQLAlchemy(app)

CORS(app)

class ClassRatings(db.Model):
    __tablename__ = "classRatings"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_id = db.Column(db.Integer, nullable=False)
    rating = db.Column('rating', db.Integer, nullable=False)  # Explicitly specify the column name
    
    def __init__(self, class_id, rating):
        self.class_id = class_id
        self.rating = rating
    
    def json(self):
        return {
            "id": self.id,
            "class_id": self.class_id,
            "rating": self.rating
        }


@app.route("/rating", methods=["GET"])
def get_all_class_ratings():
    try:
        all_ratings = ClassRatings.query.all()
        print(all_ratings)
        response_data = {"code": 200, "data": {"rating": [fc.json() for fc in all_ratings]}}
        print(response_data)  # Add this line to print the response data
        return jsonify(response_data)
    except Exception as e:
        app.logger.error(f"An error occurred while retrieving rating for fitness classes: {str(e)}")
        return jsonify({"code": 500, "message": "Failed to retrieve rating for fitness class details."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)