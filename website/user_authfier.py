# user_authfier.py
from werkzeug.security import check_password_hash, generate_password_hash
from .DBCon import Find_User, Users_Registered, Create_User
from random import randint

def check_user(mail, pwd):
    """
    Verifies user credentials by checking the email and password.
    """
    user_db = Find_User(mail)
    
    if user_db:
        # Check if the provided password matches the stored hashed password
        if check_password_hash(user_db["Pwd"], pwd):
            return True
    return False

def register_user(creds):
    """
    Registers a new user.
    Hashes the password before storing it.
    """
    # Extract credentials from the dictionary
    fname = creds["Fname"]
    lname = creds["Lname"]
    pwd = creds["pwd1"]
    email = creds["email"]

    # Hash the password before storing it
    hashed_pwd = generate_password_hash(pwd, method='pbkdf2:sha256', salt_length=8)
    
    # Generate a user ID (you can modify this logic based on your needs)
    UID = randint(101, 501)
    
    # Create the new user in the database
    Create_User(fname, lname, UID, hashed_pwd, email)
    return True

def check_if_user_registered(mail):
    """
    Checks if the email is already registered.
    """
    users = Users_Registered()
    for user in users:
        if user["Mail"] == mail:
            return True  # User exists
    return False  # User does not exist
