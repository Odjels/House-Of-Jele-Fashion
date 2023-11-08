from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
import os
from dotenv import load_dotenv
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_migrate import Migrate



# Load environment variables from .env file
load_dotenv()
app = Flask(__name__)
app.config.from_object(Config)


# Set the secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Set the database URI from the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize Flask extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'admin_login'  # Set the login view for Flask-Login
migrate = Migrate(app, db)


@login.user_loader
def load_user(user_id):
    from app.models.admin import Admin
    return Admin.query.get(int(user_id))


from app.routes.root import *
from app.routes.admin import *
from app.models import *


if __name__ == '__main__':
    app.run()
