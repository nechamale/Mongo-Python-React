from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from config import client, db
from api import ns

app = Flask(__name__)
CORS(app)
api = Api(app, version='1.0', title='Laboratory API',
          description='API for Laboratory operations')

api.add_namespace(ns)

if __name__ == '__main__':
    app.run(debug=True)
