from brain_games.games.common import get_number

TASK_STRING = 'Answer \"yes\" if given number is prime. " \
              "Otherwise answer \"no\".'


def get_task():
    """This is prime game.
    This function provides number and flag for it.
    YES - if this number is prime and
    NO - if it is not so."""

    number = get_number()
    delim = 2
    if number == 0 or number == 1:
        return 'no'
    while delim < number:
        if number % delim == 0:
            return 'no', number
        delim += 1
    return 'yes', str(number)
