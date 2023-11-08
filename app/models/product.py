from app import db
import locale

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    short_description = db.Column(db.Text, nullable=False)
    long_description = db.Column(db.Text, nullable=False)
    cover_photo = db.Column(db.String(255), nullable=True)
    photo_1 = db.Column(db.String(255), nullable=True)
    photo_2 = db.Column(db.String(255), nullable=True)
    photo_3 = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f'<Product {self.name}>'

    def formatted_cost(self):
        # Set the locale to your preferred one (e.g., en_US.UTF-8)
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        
        # Format the cost as currency
        return locale.currency(self.cost, grouping=True)