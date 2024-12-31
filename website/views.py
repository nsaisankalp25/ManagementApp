from flask import Blueprint, render_template, session, redirect, url_for, flash
from flask_login import login_required, current_user  # Import login_required and current_user

views = Blueprint('views', __name__)

@views.route('/')
def home_page():
    return render_template('home.html')

@views.route('/Portal')
@login_required  # Protect the route with login_required decorator
def Portal():
    # The user is guaranteed to be authenticated here because of the login_required decorator
    return render_template('Portal.html', user=current_user)  # You can access the current_user object here

@views.route('/Portal/AddStudent')
@login_required  # Protect the route with login_required decorator
def AddStudent():
    # The user is guaranteed to be authenticated here because of the login_required decorator
    return render_template('PortalFiles/AddStudent.html', user=current_user)  # Render the AddStudent page

@views.route('/Portal/MarksLodger')
@login_required  # Protect the route with login_required decorator
def MarksLodger():
    # The user is guaranteed to be authenticated here because of the login_required decorator
    return render_template('PortalFiles/MarksLodger.html', user=current_user)  # Render the AddStudent page

@views.route('/Portal/Students')
@login_required  # Protect the route with login_required decorator
def Students():
    # The user is guaranteed to be authenticated here because of the login_required decorator
    return render_template('PortalFiles/Students.html', user=current_user)  # Render the AddStudent page

@views.route('/Portal/FeeLodger')
@login_required  # Protect the route with login_required decorator
def FeeLodger():
    # The user is guaranteed to be authenticated here because of the login_required decorator
    return render_template('PortalFiles/FeeLodger.html', user=current_user)  # Render the AddStudent page
