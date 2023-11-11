# TODO решите задачу
import json
filename = 'input.json'
def task() -> float:
    with open(filename) as file:
        data = json.load(file)
    return round(sum(elem['score'] * elem['weight'] for elem in data), 3)


print(task())
