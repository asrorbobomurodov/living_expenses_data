import json

def total_expenses(file_path: str) -> float:
    """
    get total expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: total expenses
    """
    dct = json.loads(f)
    total = 0
    for key, value in dct.items():
        total += value
    return total


# test
file  = open('data.json')
f = file.read()
print(total_expenses(f))
