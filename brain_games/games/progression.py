import random

TASK_DESCRIPTION = 'What number is missing in the progression?'
STEP_LOWER_LIMIT = 2
STEP_UPPER_LIMIT = 10
PROGRESSION_LENGTH_LOWER_LIMIT = 5
PROGRESSION_LENGTH_UPPER_LIMIT = 10
LOWER_LIMIT = 1
UPPER_LIMIT = 100


def get_task():
    """This function creates progression game.
    As a result it provides progression string with one missed number
    (replaced with ..) and a solution for this game - the number which were
    hidden."""

    progression_start = random.randint(LOWER_LIMIT, UPPER_LIMIT)
    step = random.randint(STEP_LOWER_LIMIT, STEP_UPPER_LIMIT)
    progression_length = random.randint(PROGRESSION_LENGTH_LOWER_LIMIT,
                                        PROGRESSION_LENGTH_UPPER_LIMIT)
    hidden_num_position = random.randint(0, progression_length)
    hidden_num = 0
    progression_string = ''
    while progression_length >= 0:
        progression_start += step
        if progression_length == hidden_num_position:
            progression_string += ' ..'
            hidden_num = progression_start
        else:
            progression_string += f' {progression_start}'
        progression_length -= 1
    return str(hidden_num), progression_string.strip()
