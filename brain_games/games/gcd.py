import random
import math


def get_task():
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    return math.gcd(number1, number2), f"{number1} {number2}"
