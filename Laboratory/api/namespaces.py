from flask_restx import Namespace
from api.models.scientist import create_scientist_model
from api.routes import register_routes

api_namespace = Namespace('Scientists', description='Scientists operations')

def init_api(api):
    scientist_model = create_scientist_model(api)
    register_routes(api_namespace, scientist_model)
    api.add_namespace(api_namespace)
