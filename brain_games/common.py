import prompt


def get_user_name():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def get_response(user_result, expr_result, name):
    if user_result == expr_result:
        print("Correct!")
        return True
    else:
        print(f"{user_result} is wrong answer;(. "
              f"Correct answer was {expr_result}.")
        print(f"Let's try again, {name}!")
        return False
