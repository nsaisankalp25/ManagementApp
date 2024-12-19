from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form.get('email')
        pwd = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, pwd):
                flash('Logged in successfully!', category='success')
                #login_user(user, remember=True)
                # 
                print("\n \n USER LOGGED IN SUCCESSFULLY \n \n ")
                return redirect(url_for('views.home_page'))
            else:
                flash('Incorrect password, try again.', category='email_error')
        else:
            flash('Email does not exist.', category='email_error')

    return render_template("loginFile.html", user=current_user)


@auth.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('email')
        fname = request.form.get("firstName")
        pwd1 = request.form.get('password1')
        pwd1_rep = request.form.get('password2')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='email_error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='email_error')
        elif len(fname) < 2:
            flash('First name must be greater than 1 character.', category='email_error')
        elif pwd1  != pwd1_rep:
            flash('Passwords don\'t match.', category='email_error')
        elif len(pwd1) < 2:
            flash('Password must be at least 7 characters.', category='email_error')
        else:
            new_user = User(email=email, Fname = fname,
                password=generate_password_hash(
                pwd1, method='pbkdf2:sha256', salt_length=8))
            db.session.add(new_user)
            db.session.commit()
            
            flash("ACC CREATED", category = 'success')
            return redirect(url_for("views.home_page"))
    
    return render_template("signupFile.html")

@auth.route('/logout')
def logout():
    return "LOGOUT HERE"
