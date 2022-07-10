import random
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_number():
    """ This function returns integer positive number in range
    from 1 up to 100. """

    return str(random.randint(LOWER_LIMIT, UPPER_LIMIT))
