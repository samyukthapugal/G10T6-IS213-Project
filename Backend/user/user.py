from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



@app.route('/api/user', methods=['POST'])
def receive_user_id():
    data = request.get_json()
    user_id = data.get('userId')

    # Do something with the received user ID, e.g., store it in a database
    print(f"Received user ID: {user_id}")

    return jsonify({"message": "User ID received successfully"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)