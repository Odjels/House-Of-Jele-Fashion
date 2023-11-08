from flask import render_template
from app import app

@app.route('/contact')
def contact_page():
    return render_template("root/contact.html")