from flask import Flask, render_template, request
import razorpay
import random
import os
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

app = Flask(__name__)

# Razorpay Test Credentials
RAZORPAY_KEY_ID = "rzp_test_Rwy1MYjDZ7UMxa"   # Replace with your Key ID
RAZORPAY_KEY_SECRET = "s6XcSx1hMR46nLliMeWFE022"   # Replace with your Key Secret

client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

@app.route("/")
def pay_page():
    return render_template("pay.html")

# Allow GET since we just render Razorpay page
@app.route("/create-order", methods=["GET"])
def create_order():
    amount = 10000  # ₹100 in paise
    currency = "INR"

    # Create Razorpay order
    order = client.order.create(dict(amount=amount, currency=currency, payment_capture='1'))

    return render_template("checkout.html", order=order, key_id=RAZORPAY_KEY_ID)

@app.route("/payment-success", methods=["POST"])
def payment_success():
    payment_id = request.form.get("razorpay_payment_id")
    token = f"TKN-{random.randint(1000,9999)}"
    return render_template("success.html", token=token, payment_id=payment_id)

