import math
import random

TASK_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_task():
    """This function response for "the greatest common divisor" game.
    It returns the greatest common divisor and string with two numbers."""

    number_1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number_2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    return str(math.gcd(number_1, number_2)), f'{number_1} {number_2}'
