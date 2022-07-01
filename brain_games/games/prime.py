import random

TASK_STRING = "Answer \"yes\" if given number is prime. " \
              "Otherwise answer \"no\"."


def get_task():
    number = random.randint(1, 100)
    delim = 2
    while delim < number:
        if number % delim == 0:
            return "no", number
        delim += 1
    return "yes", number
