from flask_restx import Namespace, Resource, fields
from services.scientist_service import get_all_scientists, create_scientist, get_scientist_by_id, update_scientist, delete_scientist

ns = Namespace('Scientists', description='Scientists operations')

scientist_model = ns.model('Scientist', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a scientist'),
    'first_name': fields.String(required=True, description='First name of the scientist'),
    'last_name': fields.String(required=True, description='Last name of the scientist'),
    'telephone_number': fields.String(required=True, description='Phone number of the scientist'),
})

@ns.route('/')
class ScientistList(Resource):
    @ns.doc('list_scientists')
    @ns.marshal_list_with(scientist_model)
    def get(self):
        '''List all scientists'''
        return get_all_scientists()

    @ns.doc('create_scientist')
    @ns.expect(scientist_model)
    @ns.marshal_with(scientist_model, code=201)
    def post(self):
        '''Create a new scientist'''
        return create_scientist(ns.payload), 201

@ns.route('/<int:scientist_id>')
@ns.response(404, 'Scientist not found')
class Scientist(Resource):
    @ns.doc('get_scientist')
    @ns.marshal_with(scientist_model)
    def get(self, scientist_id):
        '''Fetch a scientist given its identifier'''
        scientist = get_scientist_by_id(scientist_id)
        if scientist:
            return scientist
        ns.abort(404, f"Scientist {scientist_id} doesn't exist")

    @ns.doc('update_scientist')
    @ns.expect(scientist_model)
    @ns.marshal_with(scientist_model)
    def put(self, scientist_id):
        '''Update a scientist given its identifier'''
        updated_scientist = update_scientist(scientist_id, ns.payload)
        if updated_scientist:
            return updated_scientist
        ns.abort(404, f"Scientist {scientist_id} doesn't exist")

    @ns.doc('delete_scientist')
    @ns.response(204, 'Scientist deleted')
    def delete(self, scientist_id):
        '''Delete a scientist given its identifier'''
        if delete_scientist(scientist_id):
            return '', 204
        ns.abort(404, f"Scientist {scientist_id} doesn't exist")
