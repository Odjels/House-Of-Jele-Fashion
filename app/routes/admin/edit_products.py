from flask import render_template, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from app.models.product import Product

@app.route('/admin/edit_products', methods=['GET'])
@login_required
def edit_products():
    products = Product.query.all()
    return render_template('admin/edit_products.html', products=products)


@app.route('/admin/delete_product/<int:product_id>')
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully', 'success')
    return redirect(url_for('edit_products'))