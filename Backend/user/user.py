from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root@localhost:3306/userdatabase"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    selected_fitness_classes = db.Column(db.Text)

    def __init__(self, selected_fitness_classes):
        self.selected_fitness_classes = selected_fitness_classes

    def json(self):
        return {
            "id": self.id,
            "selected_fitness_classes": self.selected_fitness_classes,
        }

# Your existing route to update user's selected fitness classes
@app.route('/user', methods=['POST'])
def receive_user_id():
    data = request.get_json()
    user_id = data.get('userId')
    selected_fitness_classes = data.get('selectedFitnessClasses')

    if not user_id or not selected_fitness_classes:
        return jsonify({"code": 400, "message": "Missing required parameters."}), 400

    try:
        user = User.query.filter_by(id=user_id).first()

        if user:
            user.selected_fitness_classes = selected_fitness_classes
        else:
            new_user = User(selected_fitness_classes=selected_fitness_classes)
            db.session.add(new_user)

        db.session.commit()

        return jsonify({"message": "User ID and selected fitness classes updated successfully"}), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"code": 500, "message": "Internal Server Error."}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
