# from flask import Flask, render_template, request, redirect, url_for
# import stripe
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)
# public_key = "pk_test_6pRNASCoBOKtIshFeQd4XMUh"
# stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     return render_template('index.html', public_key=public_key)

# @app.route('/thankyou')
# def thankyou():
#     return render_template('thankyou.html')

# @app.route('/payment', methods=['POST'])
# def payment():

#     # CUSTOMER INFO
#     customer = stripe.Customer.create(email=request.form['stripeEmail'],
#                                       source=request.form['stripeToken'])

#     # PAYMENT INFO
#     charge = stripe.Charge.create(
#         customer=customer.id,
#         amount=5000, 
#         currency='usd',
#         description='Donation'
#     )

#     return redirect(url_for('thankyou'))

# if __name__ == '__main__':
    # app.run(port=4242, debug=True)


from flask import Flask, render_template, request, redirect, url_for
import stripe
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
public_key = "pk_test_6pRNASCoBOKtIshFeQd4XMUh"
stripe.api_key = "sk_test_BQokikJOvBiI2HlWgH4olfQ2"

@app.route('/', methods=['GET', 'POST'])
def index():
    # Log classId and userId to the console
    class_id = request.args.get('classId')
    user_id = request.args.get('userId')
    print('Class ID:', class_id)
    print('User ID:', user_id)

    return render_template('index.html', public_key=public_key, class_id=class_id)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

# @app.route('/payment', methods=['POST'])
# def payment():
#     # Extract classId from the form data
#     class_id = request.form['classId']

#     # Determine price and details based on classId
#     if class_id == '1':
#         price = 5000  # Set the price for classId 1
#         description = 'Class 1 - test'
#     elif class_id == '2':
#         price = 6000  # Set the price for classId 2
#         description = 'Class 2 - Jogging'
#     # Add more conditions for other classIds as needed

#     # CUSTOMER INFO
#     customer = stripe.Customer.create(email=request.form['stripeEmail'],
#                                       source=request.form['stripeToken'])

#     # PAYMENT INFO
#     charge = stripe.Charge.create(
#         customer=customer.id,
#         amount=price,
#         currency='SGD',
#         description=description  # Use the determined description
#     )

#     return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(port=4242, debug=True)
