from flask import Flask, render_template, request,redirect, url_for
import stripe

app = Flask(__name__)

public_key = "pk_test_51O80cKAiq4yrhPzN2PUYNeNcgSOwgf2qp9aoCs3V7t8KAujWuAgziue9nQWst01sHjKz3YaxT9ZdOjxbb40CP4th00ZLcjfGli"

stripe.api_key = "sk_test_51O80cKAiq4yrhPzNJXibooQ2FeM9d014UZ6fSZRY0llUG5WL25nvCUKMtQMIphhZr8rzGKJHXywGyE5tEN5TQDxR00H9zpiSjI"

@app.route('/')
def index():
    return render_template('index.html',public_key=public_key)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


@app.route('/payment', methods=['POST'])
def payment():
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])
    

    charge = stripe.Charge.create(
        customer=customer.id,
        amount = 1999,
        currency= 'usd',
        description= 'Donation'
    )
    return redirect(url_for('thankyou'))

if __name__ == '__main__':
    app.run(debug=True)