# checkout.py

from flask import render_template, request, redirect, url_for
from app import app, db
from app.models.product import Product
from app.models.checkout import Order  # Import the Order model

@app.route('/checkout', methods=['GET', 'POST'])
def checkout_page():
    # Ensure that product_id and quantity are present in the query parameters
    product_id = request.args.get('product_id', type=int)
    quantity = request.args.get('quantity', type=int)

    # If any of them is missing, redirect to an error page or handle appropriately
    # if product_id is None or quantity is None:
    #     return render_template("root/error.html", error_message="Invalid request")

    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        # Retrieve form data
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        country = request.form.get('country')
        address_street = request.form.get('address_street')
        town_city = request.form.get('town_city')
        postcode = request.form.get('postcode')
        phone = request.form.get('phone')
        email = request.form.get('email')
        note = request.form.get('order_notes')

        # Calculate subtotal
        subtotal = product.cost * quantity

        # Save the order to the database
        order = Order(
            first_name=first_name,
            last_name=last_name,
            country=country,
            address_street=address_street,
            town_city=town_city,
            postcode=postcode,
            phone=phone,
            email=email,
            note=note,
            product_name=product.name,
            product_cost=product.cost,
            quantity=quantity,
            subtotal=subtotal
        )
        db.session.add(order)
        db.session.commit()


        return redirect(url_for('success_page'))

    # If it's a GET request, render the checkout page
    subtotal = product.cost * quantity

    return render_template("root/checkout.html", product=product, quantity=quantity, subtotal=subtotal)
