from pymongo import MongoClient

# Requires the PyMongo package.
# https://api.mongodb.com/python/current
from pymongo import MongoClient

# MongoDB connection URI
MONGO_URI = 'mongodb+srv://yehuditk33:1234@labcluster.poloqwc.mongodb.net/'

# Create MongoClient instance
client = MongoClient(MONGO_URI)

# Database and collection
db = client['Laboratory']

