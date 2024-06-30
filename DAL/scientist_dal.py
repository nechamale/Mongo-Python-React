from config import db

scientists_collection = db['scientists']

def find_all_scientists(sort=None, limit=0):
    if sort:
        return scientists_collection.find().sort(sort).limit(limit)
    return scientists_collection.find()

def insert_scientist(data):
    result = scientists_collection.insert_one(data)
    data['_id'] = str(result.inserted_id)
    return data

def find_scientist_by_id(scientist_id):
    return scientists_collection.find_one({'id': scientist_id})

def update_scientist_by_id(scientist_id, data):
    result = scientists_collection.update_one({'id': scientist_id}, {'$set': data})
    return result.modified_count > 0

def delete_scientist_by_id(scientist_id):
    result = scientists_collection.delete_one({'id': scientist_id})
    return result.deleted_count > 0
