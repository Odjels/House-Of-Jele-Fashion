from flask import render_template, request
from flask_login import login_required
from app import app
from app.models.checkout import Order

# View all orders route
@app.route('/admin/view_orders')
@login_required
def view_orders():
    status_filter = request.args.get('status', 'all')  # Default to 'all' if no status is provided

    if status_filter == 'all':
        orders = Order.query.all()
    elif status_filter == 'completed':
        orders = Order.query.filter_by(status='completed').all()
    elif status_filter == 'Pending':
        orders = Order.query.filter_by(status='Pending').all()
    elif status_filter == 'canceled':
        orders = Order.query.filter_by(status='canceled').all()
    else:
        return "Invalid status filter"

    return render_template('admin/view_orders.html', orders=orders, selected_tab=status_filter)
