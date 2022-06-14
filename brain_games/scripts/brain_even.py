#!/usr/bin/env python
from brain_games.common import get_response, get_user_name
import random
import prompt


def get_even_flag(number):
    if number % 2 == 0:
        even_flag = "yes"
    else:
        even_flag = "no"
    return even_flag


def main():
    name = get_user_name()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    counter = 0
    while counter != 3:
        number = random.randint(1, 100)
        even_flag = get_even_flag(number)
        print(f"Question: {number}")
        user_result = prompt.string('Your answer: ')
        if get_response(user_result, even_flag, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
