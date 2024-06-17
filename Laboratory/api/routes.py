from flask_restx import Resource
from config import db
from dal.data_access_layer import DataAccessLayer
from bl.business_logic_layer import BusinessLogicLayer

dal = DataAccessLayer(db)
bl = BusinessLogicLayer(dal)

def register_routes(ns, scientist_model):
    @ns.route('/')
    class ScientistList(Resource):
        @ns.doc('list_scientists')
        @ns.marshal_list_with(scientist_model)
        def get(self):
            scientists = list(bl.get_scientist_by_id({}))
            return scientists

        @ns.doc('create_scientist')
        @ns.expect(scientist_model)
        @ns.marshal_with(scientist_model, code=201)
        def post(self):
            new_scientist = bl.create_scientist(ns.payload)
            return new_scientist, 201

    @ns.route('/<int:scientist_id>')
    @ns.response(404, 'Scientist not found')
    class Scientist(Resource):
        @ns.doc('get_scientist')
        @ns.marshal_with(scientist_model)
        def get(self, scientist_id):
            scientist = bl.get_scientist_by_id(scientist_id)
            if scientist:
                print('in routes in api in getId', scientist)
                return scientist
            else:
                ns.abort(404, f"Scientist {scientist_id} doesn't exist")

        @ns.doc('update_scientist')
        @ns.expect(scientist_model)
        @ns.marshal_with(scientist_model)
        def put(self, scientist_id):
            updated_scientist = ns.payload
            result = bl.update_scientist(scientist_id, updated_scientist)
            if result.modified_count > 0:
                updated_scientist['id'] = scientist_id
                return updated_scientist
            else:
                ns.abort(404, f"Scientist {scientist_id} doesn't exist")

        @ns.doc('delete_scientist')
        @ns.response(204, 'Scientist deleted')
        def delete(self, scientist_id):
            result = bl.delete_scientist(scientist_id)
            if result.deleted_count > 0:
                return '', 204
            else:
                ns.abort(404, f"Scientist {scientist_id} doesn't exist")
