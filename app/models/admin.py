from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#generate_password_hash and check_password_hash:
#  Functions from Werkzeug for securely hashing and checking passwords.

# A mixin class provided by Flask-Login that includes default implementations
 # for the methods required by the User class


class Admin(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    #Admin class inherits from UserMixin and db.Model. 
    # UserMixin provides default implementations for the methods required by Flask-Login, 
    # and db.Model indicates that this class is a model for the database.

    def __repr__(self):
        return f'<Admin {self.email}>'
    #This method provides a string representation of the object.
    #  When you print an instance of the Admin class, it will display the email address.

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    #This method takes a password as input, hashes it using generate_password_hash from Werkzeug,
    #  and sets the hashed password in the password_hash attribute.

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    #This method is used for checking if a given password matches the hashed password stored in the database.
    #  It uses check_password_hash from Werkzeug.