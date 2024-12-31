from werkzeug.security import generate_password_hash, check_password_hash
from .user_authfier import Find_User  # Assuming this is the method you use to find users in your DB

class User:
    def __init__(self, email, fname, lname):
        self.email = email
        self.fname = fname
        self.lname = lname

    # Flask-Login requires this method to be implemented for loading the user from the session
    def get_id(self):
        return self.email  # This can be user email or ID, whichever works for your logic

    # Implementing is_active method for Flask-Login
    def is_active(self):
        return True  # Return True for active users (Modify as per your logic)

    # Implementing is_authenticated method for Flask-Login
    def is_authenticated(self):
        return True  # Return True since the user is authenticated once logged in

    # Implementing is_anonymous method for Flask-Login
    def is_anonymous(self):
        return False  # Return False for regular users (not anonymous)

    @classmethod
    def get(cls, user_id):
        # Retrieve the user based on their email (user_id)
        user_db = Find_User(user_id)  # Assuming Find_User returns a dictionary with user details
        if user_db:
            return User(user_db['Mail'], user_db['Fname'], user_db['Lname'])
        return None

    # Optionally, you can define methods for password hashing if you are managing that inside the User class
    @classmethod
    def create_user(cls, email, fname, lname, password):
        hashed_password = generate_password_hash(password)
        return cls(email, fname, lname)  # You may want to store the password hash in the DB, adjust as needed
    
    def check_password(self, password):
        # Simulate checking the password (You can retrieve and compare with the hashed password from the DB)
        user_db = Find_User(self.email)
        if user_db:
            return check_password_hash(user_db['Pwd'], password)  # Compare hashed password
        return False
