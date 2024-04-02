#! /usr/bin/env python3.8

"""
server.py
Stripe Sample.
Python 3.6 or newer required.
"""

import stripe
import json
import os
import secrets

from flask import Flask, render_template, jsonify, request, send_from_directory, redirect, session
from dotenv import load_dotenv, find_dotenv
from flask_cors import CORS
from dotenv import load_dotenv, find_dotenv
import requests
# Setup Stripe python client library.
load_dotenv(find_dotenv())



# Ensure environment variables are set.
price = os.getenv('PRICE')
if price is None or price == 'price_12345' or price == '':
    print('You must set a Price ID in .env. Please see the README.')
    exit(0)

# For sample support and debugging, not required for production:
stripe.set_app_info(
    'stripe-samples/accept-a-payment/prebuilt-checkout-page',
    version='0.0.1',
    url='https://github.com/stripe-samples')

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')
stripe.api_version = '2020-08-27'

static_dir = str(os.path.abspath(os.path.join(
    __file__, "..", os.getenv("STATIC_DIR"))))
app = Flask(__name__, static_folder=static_dir,
            static_url_path="", template_folder=static_dir)
app.secret_key = secrets.token_hex(16)

CORS(app)
# @app.route('/', methods=['GET'])
# def get_example():
#     return render_template('index.html')
@app.route('/', methods=['GET'])
def get_example():
    html_content = """
   <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />

        <title>Stripe Checkout Process</title>

        <link rel="icon" href="favicon.ico" type="image/x-icon" />
        <link rel="stylesheet" href="css/normalize.css" />
        <link rel="stylesheet" href="css/global.css" />
        <script src="https://js.stripe.com/v3/"></script>
        
        <style>
        /* Add your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            color: #333;
            text-align: center;
        }

        h4 {
            color: #666;
            text-align: center;
        }

        .pasha-image {
            text-align: center;
            margin-bottom: 20px;
        }

        .pasha-image img {
            border-radius: 5px;
            box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
        }

        button {
            display: block;
            width: 100%;
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        button:hover {
            background-color: #0056b3;
        }

        #error-message {
            color: red;
            text-align: center;
            margin-top: 20px;
        }
        </style>
    </head>

    <body>
        <div class="sr-root">
        <div class="sr-main">
            <section class="container">
            <h1>Payment Process</h1>
            <h4>Click on the buy button when you are ready</h4>

            <div class="pasha-image">
                <img
                src="https://picsum.photos/280/320?random=4"
                width="140"
                height="160"
                alt="Pasha Original"
                />
            </div>

            <form action="/create-checkout-session" method="POST" id="checkout-form">
                <!-- Use simpler JavaScript to set user id and class id in the hidden input fields -->
                <input type="hidden" name="userId" id="userId" />
                <input type="hidden" name="classId" id="classId" />
                <input type="hidden" name="email" id="email" />
                
                <button id="submit">Buy Now</button>
            </form>
            </section>

            <div id="error-message"></div>
        </div>
        </div>

        <script>
        // Use URLSearchParams to extract query parameters from the URL
        const urlParams = new URLSearchParams(window.location.search);
        const userId = urlParams.get('userId');
        const classId = urlParams.get('classId');
        const email = urlParams.get('email');

        // Set user id and class id in the hidden input fields when the page loads
        document.getElementById('userId').value = userId;
        document.getElementById('classId').value = classId;
        document.getElementById('email').value = email;
        </script>
    </body>
    </html>

    """
    return html_content
# @app.route('/', methods=['GET'])
# def get_example():
#     # Redirect to youtube.com
#     return render_template("index.html")

# Fetch the Checkout Session to display the JSON result on the success page
@app.route('/checkout-session', methods=['GET'])
def get_checkout_session():
    id = request.args.get('sessionId')
    checkout_session = stripe.checkout.Session.retrieve(id)
    return jsonify(checkout_session)

@app.route('/test', methods=['GET'])
def get_payment_intent_id():
    try:
        session_id = request.args.get('session_id')
        # Your code to retrieve payment_intent_id based on session_id
        session = stripe.checkout.Session.retrieve(session_id)
        
        payment_intent_id = session.payment_intent
        
        # Example response
        return payment_intent_id
    except Exception as e:
        return jsonify(error=str(e)), 500


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    
    
    domain_url = "http://localhost/ESD_Project/G10T6_Project/G10T6-IS213-Project/Backend/html"
    #dont need above, just redirect to html
    try:
        # Get the class ID from the request
        class_id = request.form.get('classId')
        USER_ID = request.form.get('userId')
        email = request.form.get('email')
        print(class_id)
        print(USER_ID)
        print(email)
        # Map class ID to corresponding price
        if class_id == '1':
            price_data = {
                'currency': 'SGD',
                'product_data': {
                    'name': 'High-Intensity Interval Training (HIIT)',
                },
                'unit_amount': 3000,  # Adjust the amount as needed
            }
        elif class_id == '2':
            price_data = {
                'currency': 'SGD',
                'product_data': {
                    'name': 'YOGA',
                },
                'unit_amount': 5000,  # Adjust the amount as needed
            }
        elif class_id == '3':
            price_data = {
            'currency': 'SGD',
            'product_data': {
                'name': 'Spinning/Cycling',
            },
            'unit_amount': 2500,  # Adjust the amount as needed
        }
        elif class_id == '4':
            price_data = {
            'currency': 'SGD',
            'product_data': {
                'name': 'Strength Training',
            },
            'unit_amount': 4000,  # Adjust the amount as needed
        }
        elif class_id == '5':
            price_data = {
            'currency': 'SGD',
            'product_data': {
                'name': 'Dance Fitness',
            },
            'unit_amount': 3500,  # Adjust the amount as needed
        }
        else:
            price_data = {
                'currency': 'SGD',
                'product_data': {
                    'name': 'Pilates',
                },
                'unit_amount': 2500,  # Adjust the amount as needed
            }

        # Create new Checkout Session for the order
        checkout_session = stripe.checkout.Session.create(
            # change domain url to localhost wamp
            success_url=f"{domain_url}/success.html?session_id={{CHECKOUT_SESSION_ID}}&userId={USER_ID}&classId={class_id}&email={email}&payment_intent={{PAYMENT_INTENT_ID}}",
            cancel_url=domain_url + '/canceled.html',
            mode='payment',
            line_items=[{
                'price_data': price_data,
                'quantity': 1,
            }]
        )

        
        return redirect(checkout_session.url, code=303)
    except Exception as e:
        return jsonify(error=str(e)), 403

# @app.route('/webhook', methods=['POST'])
# def webhook_received():
#     # You can use webhooks to receive information about asynchronous payment events.
#     # For more about our webhook events check out https://stripe.com/docs/webhooks.
#     webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
#     request_data = json.loads(request.data)

#     if webhook_secret:
#         # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
#         signature = request.headers.get('stripe-signature')
#         try:
#             event = stripe.Webhook.construct_event(
#                 payload=request.data, sig_header=signature, secret=webhook_secret)
#             data = event['data']
#         except Exception as e:
#             return e
#         # Get the type of webhook event sent - used to check the status of PaymentIntents.
#         event_type = event['type']
#     else:
#         data = request_data['data']
#         event_type = request_data['type']
#         data_object = data['object']

#     print('event ' + event_type)

#     if event_type == 'checkout.session.completed':
#         print('🔔 Payment succeeded!')
#         payment_intent_id = data['object']['payment_intent']
#         payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
#         print('Payment Intent ID:', payment_intent_id)
#         return jsonify({
#             'status': 'success',
#             'payment_intent': payment_intent
#         })
#         # Read more about expand here: https://stripe.com/docs/expand
#     return jsonify({'status': 'success'})

@app.route("/refund", methods=["POST"])
def process_refund():
    try:
        # Get the payment_intent_id from the request data
        data = request.get_json()
        payment_intent_id = data.get("payment_intent_id")
        print(payment_intent_id)
        if not payment_intent_id:
            return jsonify({"error": "Payment intent ID is required"}), 400

        # Retrieve the payment intent from Stripe
        payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

        print(payment_intent)
        # Check if the payment intent is eligible for a refund
        if payment_intent.status == "succeeded":
            # Create a refund for the payment intent
            refund = stripe.Refund.create(
                payment_intent=payment_intent_id
            )

            # Log the refund details
            print("Refund processed successfully:", refund)

            return jsonify({"message": "Refund processed successfully"}), 200
        else:
            return jsonify({"error": "Payment intent is not eligible for refund"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242, debug=True)
