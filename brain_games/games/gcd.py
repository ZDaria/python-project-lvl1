import math
from brain_games.games.common import get_number

TASK_STRING = "Find the greatest common divisor of given numbers."


def get_task():
    """This function response for "the greatest common divisor" game.
    It returns the greatest common divisor and string with two numbers."""

    number1 = get_number()
    number2 = get_number()
    return math.gcd(number1, number2), f"{number1} {number2}"
