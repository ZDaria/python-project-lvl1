#!/usr/bin/env python
import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def get_even_flag(number):
    if number % 2 == 0:
        even_flag = "yes"
    else:
        even_flag = "no"
    return even_flag


def main():
    name = welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    counter = 0
    while counter != 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input()
        even_flag = get_even_flag(number)
        if answer.strip().lower() == even_flag:
            print("Correct!")
            counter += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was "
                  f"'{even_flag}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()
