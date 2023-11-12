# This code is defining a route in this Flask web application for displaying an "about" page
from flask import render_template
from app import app

@app.route('/about')
def about_page():
    return render_template("root/about.html")