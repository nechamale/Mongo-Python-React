from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from config import db
from controllers.scientist_controller import ns as scientist_ns

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Laboratory', description='A simple Laboratory API')

api.add_namespace(scientist_ns)

if __name__ == '__main__':
    app.run(debug=True)
