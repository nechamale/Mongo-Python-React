from DAL.scientist_dal import find_all_scientists, insert_scientist, find_scientist_by_id, update_scientist_by_id, delete_scientist_by_id

def get_all_scientists():
    return list(find_all_scientists())

def create_scientist(data):
    max_id_scientist = find_all_scientists(sort=[('id', -1)], limit=1)
    new_id = int(max_id_scientist[0]['id']) + 1 if max_id_scientist else 1
    data['id'] = new_id
    return insert_scientist(data)

def get_scientist_by_id(scientist_id):
    return find_scientist_by_id(scientist_id)

def update_scientist(scientist_id, data):
    if update_scientist_by_id(scientist_id, data):
        data['id'] = scientist_id
        return data
    return None

def delete_scientist(scientist_id):
    return delete_scientist_by_id(scientist_id)
