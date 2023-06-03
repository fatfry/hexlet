#!/usr/bin/env python3
import prompt
from random import randint


def brain_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\"")
    count_win = 0
    while count_win < 3:
        items = randint(1, 100)
        print(f"Question: {items}")
        user_input = prompt.string("Your answer: ")
        if (items % 2 == 0 and user_input == "yes") or (items % 2 != 0 and user_input == "no"):
            count_win += 1
            print("Correct!")
        else:
            if items % 2 == 0:
                print(f"\'no\' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            else:
                print(f"\'yes\' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")

brain_even()







