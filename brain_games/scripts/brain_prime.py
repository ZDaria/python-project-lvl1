#!/usr/bin/env python
import prompt
import random

from brain_games.common import get_response, get_user_name


def is_prim_num(number):
    counter = 0
    delim = 1
    while delim <= number:
        if number % delim == 0:
            counter += 1
        delim += 1
    if counter == 2:
        return "yes"
    else:
        return "no"


def main():
    name = get_user_name()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    counter = 0
    while counter != 3:
        number1 = random.randint(1, 100)
        print(f"Question: {number1}")
        user_result = prompt.string('Your answer: ')
        expr_result = is_prim_num(number1)
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
