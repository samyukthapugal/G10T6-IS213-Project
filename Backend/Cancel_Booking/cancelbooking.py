# it will get the payment_intent_id, maybe user id or unique id and it will need user_bookings.py url 

#  it will call the server.py where this service sends the needed details over to server.py to process refund and return code 200 and then after that it will either remove the booking from user_bookings,

# thinking if we should add another microservice to store all the cancel booking for user to see the refund status and stuff.

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

import os, sys
import pika
import json
import amqp_connection

app = Flask(__name__)
CORS(app)

# put the different simple microservice URL
# base_fitness_class_url = "http://localhost:5000"

user_booking_url = "http://userbooking:5010"
stripe_url = "http://stripe:4242"

exchangename = "order_topic" # exchange name
exchangetype="topic" # use a 'topic' exchange to enable interaction

connection = amqp_connection.create_connection()  
channel = connection.channel()

#if the exchange is not yet created, exit the program
if not amqp_connection.check_exchange(channel, exchangename, exchangetype):
    print("\nCreate the 'Exchange' before running this microservice. \nExiting the program.")
    sys.exit(0)  # Exit with a success status

@app.route("/get_refund/<user_id>", methods=["POST"])
def get_refund(user_id):
    try:
        data = request.get_json()
        payment_intent_id = data.get("payment_intent_id")
        unique_id = data.get("unique_id")

        if not payment_intent_id or not unique_id:
            return jsonify({"error": "Payment intent ID and unique ID are required"}), 400

        refund_data = {"payment_intent_id": payment_intent_id, "unique_id": unique_id}
        refund_response = requests.post(f"{stripe_url}/refund", json=refund_data)
        print("refunded")
        if refund_response.status_code == 200:
            print("refuneded2")
            # Call the delete_booking endpoint to delete the booking entry
            delete_booking_response = requests.delete(f"http://userbooking:5010/delete_booking", json={"unique_id": unique_id})
            
            if delete_booking_response.status_code == 200:
                message = {
                        "email": data["user"]["email"],
                        "subject": "Booking has been canceled",
                        "message": { "data": {
                            "name": "the booking made on fitness app",
                            "schedule": "date",}
                        }
                    }
                print(message)
                channel.basic_publish(
                    exchange=exchangename,
                    routing_key="order.info",
                    body=json.dumps(message),
                    properties=pika.BasicProperties(content_type="text/plain", delivery_mode=2)
                )
                return jsonify({"message": "Refund processed successfully and booking entry deleted"}), 200
            else:
                return jsonify({"error": "Failed to process refund or delete booking entry"}), 500
        else:
            return jsonify({"error": "Failed to process refund"}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5105, debug=True)
