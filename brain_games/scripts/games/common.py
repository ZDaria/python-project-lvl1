import prompt
from brain_games.scripts.games import calc, prime, progression, gcd, even


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


def start_game(dialog_string, game_name):
    question = ""
    expr_result = ""
    name = get_user_name()
    print(dialog_string)
    counter = 0
    while counter != 3:
        if game_name == "calc":
            expr_result, question = calc.get_task()
        elif game_name == "even":
            expr_result, question = even.get_task()
        elif game_name == "gcd":
            expr_result, question = gcd.get_task()
        elif game_name == "prime":
            expr_result, question = prime.get_task()
        elif game_name == "progression":
            expr_result, question = progression.get_task()
        print(f"Question: {question}")
        user_result = prompt.string('Your answer: ')
        if get_response(user_result, expr_result, name):
            counter += 1
        else:
            return
    print(f"Congratulations, {name}!")
