#!/usr/bin/env python
from brain_games.scripts.games.common import start_game
from brain_games.scripts.games import progression


def main():
    start_game("What number is missing in the progression?", progression)


if __name__ == "__main__":
    main()
