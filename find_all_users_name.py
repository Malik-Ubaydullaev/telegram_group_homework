from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    msg = []
    msg = data['messages']
    name = []
    idx = 0
    d = {}
    
    while idx < len(msg):
        #print(msg[idx])
        #stroka = " ".join(msg[idx])
        #print(stroka)
        #print(type(msg[idx]))
        d = msg[idx]
        for k,v in d.items():
            if k == "actor":
                name.append(v)
        idx += 1    
        d = {}
        name2 = []
        for item in name:
            if item not in name2:
                name2.append(item)
    return name2

data = read_data('data/result.json')
print(find_all_users_name(data))