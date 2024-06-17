class BusinessLogicLayer:
    def __init__(self, dal):
        self.dal = dal

    def create_scientist(self, scientist_data):
        scientists_collection = self.dal.get_collection('scientists')
        highest_id_scientist = scientists_collection.find_one(sort=[('id', -1)])
        new_id = int(highest_id_scientist['id']) + 1 if highest_id_scientist else 1
        scientist_data['id'] = new_id
        self.dal.insert_document('scientists', scientist_data)
        return scientist_data

    def get_scientist_by_id(self, scientist_id):
        print('id of get by Id in bl ', scientist_id)
        return self.dal.find_documents('scientists', {'id': scientist_id})

    def update_scientist(self, scientist_id, scientist_data):
        return self.dal.update_document('scientists', {'id': scientist_id}, {'$set': scientist_data})

    def delete_scientist(self, scientist_id):
        return self.dal.delete_document('scientists', {'id': scientist_id})
