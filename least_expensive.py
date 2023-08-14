import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    dct = json.loads(file)
    mn = list(dct.values())[0]
    for key, value in dct.items():
        if value < mn:
            mn = value
    return mn
    

# test
file_path = "data.json"
file = open(file_path).read()
print(least_expensive(file))
