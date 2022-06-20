#!/usr/bin/env python
from brain_games.scripts.games.common import start_game
from brain_games.scripts.games import even


def main():
    start_game("Answer \"yes\" if the number is even, "
               "otherwise answer \"no\".", even)


if __name__ == "__main__":
    main()
