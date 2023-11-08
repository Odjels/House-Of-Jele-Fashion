from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from app.models.product import Product
import os

UPLOAD_FOLDER = 'app/static/admin/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

def save_file(file):
    if file and allowed_file(file.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return filename.replace('app/static/', '')  # Store path relative to static folder
    return None

@app.route('/admin/edit_product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form.get('product_name')
        product.cost = float(request.form.get('cost'))
        product.short_description = request.form.get('short_description')
        product.long_description = request.form.get('long_description')

        # File uploads
        cover_photo = request.files['cover_photo'] if 'cover_photo' in request.files else None
        photo_1 = request.files['photo_1'] if 'photo_1' in request.files else None
        photo_2 = request.files['photo_2'] if 'photo_2' in request.files else None
        photo_3 = request.files['photo_3'] if 'photo_3' in request.files else None

        # Save files to the server and get their paths
        product.cover_photo = save_file(cover_photo) if cover_photo else product.cover_photo
        product.photo_1 = save_file(photo_1) if photo_1 else product.photo_1
        product.photo_2 = save_file(photo_2) if photo_2 else product.photo_2
        product.photo_3 = save_file(photo_3) if photo_3 else product.photo_3

        db.session.commit()
        flash('Product updated successfully', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/edit_product.html', product=product)
