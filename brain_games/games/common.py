import prompt
from brain_games.games import progression, prime, calc, even, gcd


def get_user_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def get_response(user_result, expr_result, name):
    if user_result == str(expr_result):
        print("Correct!")
        return True
    else:
        print(f"{user_result} is wrong answer;(. "
              f"Correct answer was {expr_result}.")
        print(f"Let's try again, {name}!")
        return False


def start_game(game_name):
    task_string = {calc: "What is the result of the expression?",
                   even: "Answer \"yes\" if the number is even, "
                         "otherwise answer \"no\".",
                   gcd: "Find the greatest common divisor of given numbers.",
                   prime: "Answer \"yes\" if given number is prime. "
                          "Otherwise answer \"no\".",
                   progression: "What number is missing in the progression?"}

    name = get_user_name()
    print(task_string[game_name])
    counter = 0
    while counter != 3:
        expr_result, question = game_name.get_task()
        print(f"Question: {question}")
        user_result = prompt.string('Your answer: ')
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")
