from flask import render_template
from app import app
from app.models.product import Product

@app.route('/product/<int:product_id>')
def product_details(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("root/product_details.html", product=product)