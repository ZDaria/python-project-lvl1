import random

TASK_STRING = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_task():
    """This function provides task and solution for even game.
    Returns: flag does int value even or not and question - this int number."""

    question = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    return ('yes' if question % 2 == 0 else 'no'), question
