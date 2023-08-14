import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    dct = json.loads(data)
    return dct
# test
file_path = "data.json"
data = open(file_path).read()
print(get_data(data))
