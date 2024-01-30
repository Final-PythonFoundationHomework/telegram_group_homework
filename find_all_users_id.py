from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    s=set()
    for i in data['messages']:
        if i.get('actor_id')!=None:
            s.add(i['actor_id'])
        else:
            s.add(i['from_id'])
    return s
# data=find_all_users_id(read_data('data/result.json'))
# print(read_data('data/result.json'))

# print(data)