from app import db
from datetime import datetime

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    country = db.Column(db.String(255), nullable=False)
    address_street = db.Column(db.String(255), nullable=False)
    town_city = db.Column(db.String(255), nullable=False)
    postcode = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    note = db.Column(db.Text, nullable=True)
    product_name = db.Column(db.String(255), nullable=False)
    product_cost = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    date_ordered = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    status = db.Column(db.String(20), default='Pending', nullable=False)

    def __repr__(self):
        return f'<Order {self.id}>'
