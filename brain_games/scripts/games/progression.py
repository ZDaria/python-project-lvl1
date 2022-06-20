import random


def get_task():
    progression_start = random.randint(1, 100)
    step = random.randint(2, 10)
    progression_length = random.randint(5, 11)
    hidden_num_position = random.randint(2, progression_length)
    hidden_num = 0
    position_counter = 0
    progression_string = ""
    for x in range(progression_start, progression_start +
                   step * progression_length, step):
        if hidden_num_position == position_counter:
            progression_string += " .."
            hidden_num = x
        else:
            progression_string += f" {x}"
        position_counter += 1

    return hidden_num, progression_string
