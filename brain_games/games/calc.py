import random

TASK_STRING = 'What is the result of the expression?'
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_operator():
    """ This function returns one of mathematics operators."""

    operators_for_expression = ["+", "*", "-"]
    return random.choice(operators_for_expression)


def get_expected_result(num1, num2, operation):
    """ Provides expected result for this game according to input values. """

    if operation == '+':
        res = num1 + num2
    elif operation == '*':
        res = num1 * num2
    else:
        res = num1 - num2
    return res


def get_task():
    """ This function responsible for "math result expression game".
    It returns string with simple math expression
    e.g 10 + 2
    and expected result for this particular expression."""

    operation = get_operator()
    number_1 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    number_2 = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    res = get_expected_result(number_1, number_2, operation)
    return str(res), f"{number_1} {operation} {number_2}"
