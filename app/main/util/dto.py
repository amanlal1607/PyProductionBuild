from flask_restplus import Namespace,fields

# This is the Data transfer Utility
# This will be used for marshalling data for API calls

class UserDto:
    # creates a namespace for user related operations
    api = Namespace('user', description='user related operations')
    #
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })