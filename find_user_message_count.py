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
    user_message_count = {}

    for user_id in users_id:
        user_message_count[user_id] = 0

    for message in data["messages"]:
        from_id = message["from_id"]
        if from_id in user_message_count:
            user_message_count[from_id] += 1

    return user_message_count
    
