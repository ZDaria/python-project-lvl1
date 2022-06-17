#!/usr/bin/env python
import prompt
import random

from brain_games.common import get_response, get_user_name


def get_arith_progression(progression_start, step):
    progression_length = random.randint(5, 11)
    hidden_num_position = random.randint(2, progression_length)
    hidden_num = 0
    progression_string = str(progression_start)
    while progression_length - 1 != 0:
        progression_start += step
        if progression_length == hidden_num_position:
            progression_string += " .."
            hidden_num = progression_start
        else:
            progression_string += f" {progression_start}"
        progression_length -= 1
    return progression_string, hidden_num


def main():
    name = get_user_name()
    print("Find the greatest common divisor of given numbers.")
    counter = 0
    while counter != 3:
        progression_start = random.randint(1, 100)
        step = random.randint(2, 10)
        progression_list, expr_result = get_arith_progression(
            progression_start, step)
        print(f"Question: {progression_list}")
        user_result = prompt.integer('Your answer: ')
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
