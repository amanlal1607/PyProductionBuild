import uuid
import datetime

from app.main import db
from app.main.model.user import User

# The code below creates a new user by first checking if the user already exists.
# Returns a success response_object if the user doesnt exist
# Returns a failure response_object if the user exists
# Require a method to verify the JWT token and use the user details for LDAP lookup
def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            public_id=str(uuid.uuid4()),
            email=data['email'],
            username=data['username'],
            password=data['password'],
            registered_on=datetime.datetime.utcnow()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

# Returns a list of all registered users - Probably need to be replaced by an LDAP lookup
def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

# This method needs to be deleted. We will not be storing users in the DB
def save_changes(data):
    db.session.add(data)
    db.session.commit()