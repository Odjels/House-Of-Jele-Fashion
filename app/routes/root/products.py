from flask import render_template, request
from app import app
from app.models.product import Product
from sqlalchemy import desc

@app.route('/products')
def product_page():
    # Pagination
    page = request.args.get('page', 1, type=int)
    per_page = 12

    # Fetch products from the database
    products = Product.query.order_by(desc(Product.id)).paginate(page=page, per_page=per_page, error_out=False)

    return render_template("root/products.html", products=products)
