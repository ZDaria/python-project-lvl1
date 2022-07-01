import random

TASK_STRING = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_task():
    question = random.randint(1, 100)
    return ("yes" if question % 2 == 0 else "no"), question
