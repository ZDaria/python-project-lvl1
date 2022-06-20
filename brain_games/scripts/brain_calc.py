#!/usr/bin/env python
from brain_games.scripts.games.common import start_game
from brain_games.scripts.games import calc


def main():
    start_game("What is the result of the expression?", calc)


if __name__ == "__main__":
    main()
