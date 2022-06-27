import random


def get_task():
    number = random.randint(1, 100)
    counter = 0
    delim = 1
    while delim <= number:
        if number % delim == 0:
            counter += 1
        delim += 1
    return ("yes" if counter == 2 else "no"), number
