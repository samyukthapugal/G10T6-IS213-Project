

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

    return render_template('stripeUI.html', public_key=public_key, class_id=class_id)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(port=4242, debug=True)
