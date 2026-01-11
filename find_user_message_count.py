from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: list)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    s={}
    for j in  users_id:
        x = 0
        for i in data['messages']:
            if  i.get('actor_id')!=None:
                if i['actor_id']==j:
                    x+=1
            else:
                if i['from_id']==j:
                    x+=1
        s[j] = x  
    return s
# data=read_data('data/result.json')
# users_id = find_all_users_id(data)

# print(find_user_message_count(data, list(users_id)))