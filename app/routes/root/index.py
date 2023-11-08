from flask import render_template
from app import app
from app.models.product import Product
from sqlalchemy import desc

@app.route('/')
@app.route('/home')
def home_page():
    # Fetch 8 products from the database
    per_page = 8
    products = Product.query.order_by(desc(Product.id)).limit(per_page).all()

    return render_template("root/index.html", products=products)
