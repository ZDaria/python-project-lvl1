import random


def get_task():
    progression_start = random.randint(1, 100)
    step = random.randint(2, 10)
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
    return hidden_num, progression_string
