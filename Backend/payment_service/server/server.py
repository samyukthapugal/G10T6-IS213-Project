# #! /usr/bin/env python3.6
# import stripe
# import json
# import os

# from flask import Flask, render_template, jsonify, request, send_from_directory
# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

# # For sample support and debugging, not required for production:
# stripe.set_app_info(
#     'stripe-samples/your-sample-name',
#     version='0.0.1',
#     url='https://github.com/stripe-samples')

# stripe.api_version = '2020-08-27'
# stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# static_dir = str(os.path.abspath(os.path.join(__file__ , "..", os.getenv("STATIC_DIR"))))
# app = Flask(__name__, static_folder=static_dir, static_url_path="", template_folder=static_dir)

# @app.route('/', methods=['GET'])
# def get_root():
#     return render_template('index.html')

# @app.route('/config', methods=['GET'])
# def get_config():
#     return jsonify({'publishableKey': os.getenv('STRIPE_PUBLISHABLE_KEY')})


# @app.route("/create-payment-intent", methods=["POST"])
# def create_payment_intent():
#     # lookup the product in db and calculate the min amt
#     payment_intent = stripe.PaymentIntent.create(
#       amount=1000,
#       currency="sgd",
#       automatic_payment_methods={'enabled': True},
#     )
#     return jsonify(clientSecret=payment_intent.client_secret)

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
#     data_object = data['object']

#     if event_type == 'payment_intent.succeeded':
#         print('💰 Payment received!')


#     return jsonify({'status': 'success'})


# if __name__ == '__main__':
#     app.run(port=4242, debug=True)



#!/usr/bin/env python3.6

# Import necessary libraries and modules
import stripe
import json
import os
from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv, find_dotenv

# Load environment variables from a .env file
load_dotenv(find_dotenv())

# Set up Stripe API key and version
stripe.set_app_info(
    'stripe-samples/your-sample-name',
    version='0.0.1',
    url='https://github.com/stripe-samples')
stripe.api_version = '2020-08-27'
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

# Set up static directory and initialize Flask app
static_dir = str(os.path.abspath(os.path.join(__file__, "..", os.getenv("STATIC_DIR"))))
app = Flask(__name__, static_folder=static_dir, static_url_path="", template_folder=static_dir)

# Define a route for the root URL ('/') that renders the index.html template
@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')

# Define a route for the '/config' endpoint that returns the publishable key
@app.route('/config', methods=['GET'])
def get_config():
    return jsonify({'publishableKey': os.getenv('STRIPE_PUBLISHABLE_KEY')})

# Define a route for creating a payment intent at '/create-payment-intent'
@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    # Create a payment intent with a fixed amount, currency, and automatic payment methods
    payment_intent = stripe.PaymentIntent.create(
      amount=1000,
      currency="sgd",
      automatic_payment_methods={'enabled': True},
    )
    # Return the client secret of the created payment intent
    return jsonify(clientSecret=payment_intent.client_secret)

# Define a route for the '/webhook' endpoint to handle Stripe webhook events
@app.route('/webhook', methods=['POST'])
def webhook_received():
    # Retrieve the webhook secret from environment variables
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

    # Parse the incoming JSON data from the webhook request
    request_data = json.loads(request.data)

    if webhook_secret:
        # If a webhook secret is configured, verify the signature and construct the event
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event and data object
        event_type = event['type']
    else:
        # If no webhook secret is configured, use the data from the request directly
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    # Check if the event type is 'payment_intent.succeeded'
    if event_type == 'payment_intent.succeeded':
        print('💰 Payment received!')

    # Return a success response to the webhook event
    return jsonify({'status': 'success'})

# Run the Flask app on port 4242 in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(port=4242, debug=True)
