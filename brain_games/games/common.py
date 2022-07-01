import random


def get_number():
    """ This function returns integer positive number in range
    from 1 up to 100. """

    lower_limit = 1
    upper_limit = 100
    return random.randint(lower_limit, upper_limit)
