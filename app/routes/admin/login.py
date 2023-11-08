from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from app import app, db
from app.models.admin import Admin

# Admin login route
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    # Check if there's already an admin
    existing_admin = Admin.query.first()

    if existing_admin:
        if request.method == 'POST':
            email = request.form.get('signin-email')
            password = request.form.get('signin-password')

            # Validate the credentials
            if existing_admin.check_password(password) and existing_admin.email == email:
                login_user(existing_admin)
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Invalid email or password', 'danger')

        return render_template('admin/login.html')

    # If there's no admin, create one
    elif request.method == 'POST':
        email = request.form.get('signin-email')
        password = request.form.get('signin-password')

        # Create and store the admin
        new_admin = Admin(email=email)
        new_admin.set_password(password)
        db.session.add(new_admin)
        db.session.commit()

        # Log in the new admin
        login_user(new_admin)
        return redirect(url_for('admin_dashboard'))

    return render_template('admin/login.html')



@app.route('/admin/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('admin_login'))