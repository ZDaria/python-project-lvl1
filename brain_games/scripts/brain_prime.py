#!/usr/bin/env python
from brain_games.scripts.games.common import start_game
from brain_games.scripts.games import prime


def main():
    start_game("Answer \"yes\" if given number is prime. "
               "Otherwise answer \"no\".", prime)


if __name__ == "__main__":
    main()
