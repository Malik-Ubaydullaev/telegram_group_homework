from read_data import read_data
import json

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    msg = []
    msg = data['messages']
    user_id = []
    idx = 0
    d = {}
    
    while idx < len(msg):
        #print(msg[idx])
        #stroka = " ".join(msg[idx])
        #print(stroka)
        #print(type(msg[idx]))
        d = msg[idx]
        for k,v in d.items():
            if k == "actor_id":
                user_id.append(v)
        idx += 1
        
        d = {}
        
    return user_id

data = read_data('data/result.json')
print(find_all_users_id(data))
