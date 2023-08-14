import json

def average_expenses(file_path: str) -> float:
    """
    get average expenses from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        float: average expenses
    """
    total = 0
    dct = json.loads(file_path)
    for key, value in dct.items():
        total += value
    return total/len(dct)

# test
file_path = open("data.json").read()
average = average_expenses(file_path)
print(average)
