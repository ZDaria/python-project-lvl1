#!/usr/bin/env python
import random
from brain_games.common import get_response, get_user_name
import prompt


def get_expr():
    expr_list = ["+", "*", "-"]
    expr = random.choices(expr_list, k=1)[0]
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    if expr == "+":
        res = number1 + number2
    elif expr == "*":
        res = number1 * number2
    else:
        res = number1 - number2
    return f"{number1} {expr} {number2}", res


def main():
    name = get_user_name()
    print("What is the result of the expression?")
    counter = 0
    while counter != 3:
        expr, expr_result = get_expr()
        print(f"Question: {expr}")
        user_result = prompt.integer('Your answer: ')
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
