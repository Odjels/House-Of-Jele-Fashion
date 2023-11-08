from flask import render_template, redirect, url_for, request
from app import app, db
from app.models.checkout import Order
from flask_login import login_required


@app.route('/admin/view_orders/<int:order_id>', methods=['GET', 'POST'])
@login_required
def view_order(order_id):
    order = Order.query.get_or_404(order_id)

    if request.method == 'POST':
        new_status = request.form.get('new_status')
        if new_status == 'completed':
            order.status = 'completed'
        elif new_status == 'canceled':
            order.status = 'canceled'
        
        db.session.commit()
        return redirect(url_for('view_orders'))

    return render_template('admin/view_order.html', order=order)
