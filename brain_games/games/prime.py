import random

TASK_STRING = 'Answer \"yes\" if given number is prime. ' \
              'Otherwise answer \"no\".'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_task():
    """This is prime game.
    This function provides number and flag for it.
    YES - if this number is prime and
    NO - if it is not so."""

    number = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    delim = 2
    if number == 0 or number == 1:
        return 'no'
    while delim < number:
        if number % delim == 0:
            return 'no', number
        delim += 1
    return 'yes', str(number)
