import random


def get_task():
    operation = random.choice(["+", "*", "-"])
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    if operation == "+":
        res = number_1 + number_2
    elif operation == "*":
        res = number_1 * number_2
    else:
        res = number_1 - number_2
    return res, f"{number_1} {operation} {number_2}"
