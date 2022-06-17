#!/usr/bin/env python
import math
import prompt
import random

from brain_games.common import get_response, get_user_name


def main():
    name = get_user_name()
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while counter != 3:
        number1 = random.randint(1, 100)
        number2 = random.randint(1, 100)
        print(f"Question: {number1} {number2}")
        user_result = prompt.integer('Your answer: ')
        expr_result = math.gcd(number1, number2)
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
