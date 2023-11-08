from app import app
from flask import render_template


@app.route('/success')
def success_page():
    return render_template('root/success.html')