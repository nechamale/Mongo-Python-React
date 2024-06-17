from flask_restx import Namespace
from api.models.scientist import create_scientist_model
from api.routes import register_routes

ns = Namespace('Scientists', description='Scientists operations')
scientist_model = create_scientist_model(ns)
register_routes(ns, scientist_model)
