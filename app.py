
from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

BUSINESS_NAME = "OLEKC Tax Services"
PHONE = "(773) 677-8783"
EMAIL = "olekcsgoods@gmail.com"
PAYMENT_LINK = os.getenv("OLEKC_PAYMENT_LINK", "#")

@app.context_processor
def inject_globals():
    return dict(BUSINESS_NAME=BUSINESS_NAME, PHONE=PHONE, EMAIL=EMAIL, PAYMENT_LINK=PAYMENT_LINK)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/services')
def services():
    return render_template('services.html', title="Services & Pricing")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

@app.route('/referrals')
def referrals():
    return render_template('referrals.html', title="Referral Program")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

@app.route('/pay')
def pay():
    return render_template('pay.html', title="Pay Now")

if __name__ == '__main__':
    app.run(debug=True)
