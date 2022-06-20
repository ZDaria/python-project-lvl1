#!/usr/bin/env python
from brain_games.scripts.games.common import start_game
from brain_games.scripts.games import gcd


def main():
    start_game("Find the greatest common divisor of given numbers.", gcd)


if __name__ == "__main__":
    main()
