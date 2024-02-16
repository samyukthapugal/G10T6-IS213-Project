#! /usr/bin/env python3.6
import stripe
import json
import os

from flask import Flask, render_template, jsonify, request, send_from_directory
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# For sample support and debugging, not required for production:
stripe.set_app_info(
    'stripe-samples/your-sample-name',
    version='0.0.1',
    url='https://github.com/stripe-samples')

stripe.api_version = '2020-08-27'
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

static_dir = str(os.path.abspath(os.path.join(__file__ , "..", os.getenv("STATIC_DIR"))))
app = Flask(__name__, static_folder=static_dir, static_url_path="", template_folder=static_dir)

@app.route('/', methods=['GET'])
def get_root():
    return render_template('index.html')

@app.route('/config', methods=['GET'])
def get_config():
    return jsonify({'publishableKey': os.getenv('STRIPE_PUBLISHABLE_KEY')})


@app.route("/create-payment-intent", methods=["POST"])
def create_payment_intent():
    # lookup the product in db and calculate the min amt
    payment_intent = stripe.PaymentIntent.create(
      amount=1000,
      currency="sgd",
      automatic_payment_methods={'enabled': True},
    )
    return jsonify(clientSecret=payment_intent.client_secret)

@app.route('/webhook', methods=['POST'])
def webhook_received():
    # You can use webhooks to receive information about asynchronous payment events.
    # For more about our webhook events check out https://stripe.com/docs/webhooks.
    webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')
    request_data = json.loads(request.data)

    if webhook_secret:
        # Retrieve the event by verifying the signature using the raw body and secret if webhook signing is configured.
        signature = request.headers.get('stripe-signature')
        try:
            event = stripe.Webhook.construct_event(
                payload=request.data, sig_header=signature, secret=webhook_secret)
            data = event['data']
        except Exception as e:
            return e
        # Get the type of webhook event sent - used to check the status of PaymentIntents.
        event_type = event['type']
    else:
        data = request_data['data']
        event_type = request_data['type']
    data_object = data['object']

    if event_type == 'payment_intent.succeeded':
        print('💰 Payment received!')


    return jsonify({'status': 'success'})


if __name__ == '__main__':
    app.run(port=4242, debug=True)
