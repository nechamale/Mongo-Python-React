from flask_restx import fields

def create_scientist_model(api):
    return api.model('Scientist', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a scientist'),
    'first_name': fields.String(required=True, description='first Name of the scientist'),
    'last_name': fields.String(required=True, description='last Name of the scientist'),
    'telephone_number': fields.String(required=True, description='Phone of expertise'),
})