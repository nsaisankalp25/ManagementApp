# DbCon.py
from pymongo.mongo_client import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

p = os.getenv("DBPWD")
a = os.getenv("DBUSN")

uri = f"mongodb+srv://{a}:{p}@cpusers.hettx.mongodb.net/?retryWrites=true&w=majority&appName=CpUsers"
client = MongoClient(uri)

# Get the database and collection for users
UsersAdmin_db = client.UsersAdmin
collection = UsersAdmin_db.Users_Admin_Identities

def Create_User(Fname, Lname, UsID, Pwd, Mail):
    """
    Inserts a new user into the database.
    """
    doc = {
        "Fname": Fname,
        "Lname": Lname,
        "UsID": UsID,
        "Mail": Mail,
        "Pwd": Pwd  # Pwd should be a hashed password before inserting
    }
    ins_id = collection.insert_one(doc).inserted_id
    print(f"User created with ID: {ins_id}")

def Find_User(mail):
    """
    Find a user by their email address in the database.
    Returns None if no user is found.
    """
    user = collection.find_one({"Mail": mail})
    return user

def Users_Registered():
    """
    Retrieve all registered users.
    """
    users = collection.find()
    return list(users)
