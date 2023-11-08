from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required
from app import app, db
from app.models.product import Product  # Make sure to import the Product model

# ... (your existing routes)

# Add New Product route
@app.route('/admin/add_product', methods=['GET', 'POST'])
@login_required
def add_product():
    if request.method == 'POST':
        # Retrieve data from the form
        product_name = request.form.get('product_name')
        cost = float(request.form.get('cost'))
        short_description = request.form.get('short_description')
        long_description = request.form.get('long_description')
        
        # Handle file uploads
        cover_photo = request.files['cover_photo']
        photo_1 = request.files['photo_1']
        photo_2 = request.files['photo_2']
        photo_3 = request.files['photo_3']

        # Save uploaded files
        cover_photo_path = f"static/uploads/{cover_photo.filename}"
        cover_photo.save(f"app/{cover_photo_path}")

        photo_1_path = f"static/uploads/{photo_1.filename}"
        photo_1.save(f"app/{photo_1_path}")

        photo_2_path = f"static/uploads/{photo_2.filename}"
        photo_2.save(f"app/{photo_2_path}")

        photo_3_path = f"static/uploads/{photo_3.filename}"
        photo_3.save(f"app/{photo_3_path}")

        # Create a new Product instance and add it to the database
        new_product = Product(
            name=product_name,
            cost=cost,
            short_description=short_description,
            long_description=long_description,
            cover_photo=cover_photo_path,
            photo_1=photo_1_path,
            photo_2=photo_2_path,
            photo_3=photo_3_path
        )
        db.session.add(new_product)
        db.session.commit()

        flash('Product added successfully!', 'success')
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/add_product.html')
