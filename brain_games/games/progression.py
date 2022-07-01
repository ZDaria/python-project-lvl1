import random
"""This module creates task for progression game."""

HIDDEN_START_NUM_POSITION_COUNT = 0

LOW_LIMIT_PROGRESSION_LEN = 5
UPPER_LIMIT_PROGRESSION_LEN = 11

LOW_LIMIT_PROGRESSION_START = 1
UPPER_LIMIT_PROGRESSION_START = 100

LOW_LIMIT_STEP = 1
UPPER_LIMIT_STEP = 10

TASK_STRING = "What number is missing in the progression?"


def get_task():
    progression_start = random.randint(LOW_LIMIT_PROGRESSION_START,
                                       UPPER_LIMIT_PROGRESSION_START)
    step = random.randint(LOW_LIMIT_STEP, UPPER_LIMIT_STEP)
    progression_length = random.randint(LOW_LIMIT_PROGRESSION_LEN,
                                        UPPER_LIMIT_PROGRESSION_LEN)
    hidden_num_position = random.randint(HIDDEN_START_NUM_POSITION_COUNT,
                                         progression_length)
    hidden_num = 0
    progression_string = ""
    while progression_length >= 0:
        progression_start += step
        if progression_length == hidden_num_position:
            progression_string += " .."
            hidden_num = progression_start
        else:
            progression_string += f" {progression_start}"
        progression_length -= 1
    return hidden_num, progression_string.strip()
