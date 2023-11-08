from flask import render_template
from flask_login import login_required
from app import app
from app.models.product import Product
from app.models.checkout import Order
from flask_login import login_required, current_user


# Admin dashboard route
@app.route('/admin/dashboard')
@login_required
def admin_dashboard():
    
    num_products = Product.query.count()
    num_orders = Order.query.count() 
    num_completed_orders = Order.query.filter_by(status='completed').count()
    num_cancelled_orders = Order.query.filter_by(status='canceled').count()

    return render_template('admin/dashboard.html', num_products=num_products, num_orders=num_orders, num_completed_orders=num_completed_orders, num_cancelled_orders=num_cancelled_orders, admin_email=current_user.email) 
