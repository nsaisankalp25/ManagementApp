# auth.py
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from .user_authfier import check_user, check_if_user_registered, register_user
from .DBCon import Find_User
from .models import User  # Assuming User is defined in models.py

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        pwd = request.form.get('password1').strip()

        # Use check_user from user_authfier.py to verify user
        if check_user(email, pwd):
            user_db = Find_User(email)
            # Create the User object for Flask-Login
            user = User(email=user_db["Mail"], fname=user_db["Fname"], lname=user_db["Lname"])
            login_user(user)  # Log the user in using Flask-Login
            flash('Logged in successfully!', category='success')
            return redirect(url_for('views.Portal'))  # Redirect to a protected page (e.g., Portal)
        else:
            flash('Incorrect email or password.', category='email_error')
    return render_template("loginFile.html", user=current_user)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email').strip()
        fname = request.form.get("firstName").strip()
        lname = request.form.get("LastName").strip()
        pwd1 = request.form.get('password1').strip()
        pwd1_rep = request.form.get('password2').strip()

        if check_if_user_registered(email):
            flash('Email already exists.', category='email_error')
        elif pwd1 != pwd1_rep:
            flash('Passwords don\'t match.', category='email_error')
        else:
            # Prepare new user credentials
            new_user = {"Fname": fname, "Lname": lname, "pwd1": pwd1, "email": email}
            if register_user(new_user):
                flash("ACCOUNT CREATED", category='success')
                return redirect(url_for("auth.login"))
    return render_template("signupFile.html")

@auth.route('/logout')
def logout():
    logout_user()  # Flask-Login logout
    flash("You have been logged out.", "success")
    return redirect(url_for('auth.login'))  # Redirect to login page after logout
