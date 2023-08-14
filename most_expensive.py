import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    f = open(file_path).read()
    dct = json.loads(f)
    most_expensive = 0
    for key, value in dct.items():
        if most_expensive < value:
            most_expensive = value
    return most_expensive

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)