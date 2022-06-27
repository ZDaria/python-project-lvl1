import random


def get_task():
    operation = random.choices(["+", "*", "-"], k=1)[0]
    expr = f"{random.randint(1, 100)} {operation} {random.randint(1, 100)}"
    return eval(expr), expr
