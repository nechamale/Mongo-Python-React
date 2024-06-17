class DataAccessLayer:
    def __init__(self, db):
        self.db = db

    def get_collection(self, collection_name):
        return self.db[collection_name]

    def insert_document(self, collection_name, document):
        collection = self.get_collection(collection_name)
        collection.insert_one(document)

    def find_documents(self, collection_name, query):
        collection = self.get_collection(collection_name)
        print('query in find_documents in DAL', query)
        return collection.find(query)

    def update_document(self, collection_name, query, update):
        collection = self.get_collection(collection_name)
        return collection.update_one(query, update)

    def delete_document(self, collection_name, query):
        collection = self.get_collection(collection_name)
        return collection.delete_one(query)
