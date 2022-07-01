from brain_games.games.common import get_number

TASK_STRING = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def get_task():
    """This function provides task and solution for even game.
    Returns: flag does int value even or not and question - this int number."""

    question = get_number()
    return ("yes" if question % 2 == 0 else "no"), question
