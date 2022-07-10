import prompt

WINS_COUNT = 3


def start_game(game_name):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game_name.TASK_STRING)
    counter = 0
    while counter != WINS_COUNT:
        expr_result, question = game_name.get_task()
        print(f'Question: {question}')
        user_result = prompt.string('Your answer: ')
        if user_result == expr_result:
            print('Correct!')
            counter += 1
        else:
            print(f'{user_result} is wrong answer;(. '
                  f'Correct answer was {expr_result}.')
            print(f'Let\'s try again, {name}!')
            return
    print(f'Congratulations, {name}!')
