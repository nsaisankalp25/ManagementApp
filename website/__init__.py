# __init__.py
from flask import Flask
from flask_login import LoginManager
from .models import User  # Import the User model
from .DBCon import Find_User  # Import the Find_User function from DBCon
from dotenv import load_dotenv
import os

def create_app():
    app = Flask(__name__)
    SecKey = os.getenv("SECRET_KEY")
    app.config['SECRET_KEY'] = SecKey

    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'  # Redirect to login page if not authenticated

    # Register Blueprints
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # Define the user loader function
    @login_manager.user_loader
    def load_user(user_id):
        # The `user_id` here is the email (passed as a string)
        user_db = Find_User(user_id)  # Now it will use the imported Find_User function
        if user_db:
            return User(user_db['Mail'], user_db['Fname'], user_db['Lname'])
        return None

    return app
