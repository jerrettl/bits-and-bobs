#!/usr/bin/python3


"""
generate.py

This script generates passwords given the length of the password
desired and the number of passwords the user wishes to generate.

This can either be entered through the built-in inputs or with the
two optional parameters:
    1st parameter: length of password(s)
    2nd parameter: number of passwords
"""

import random
import sys


# Check to make sure the user types a real number into the input(s).
def check_input(x):
    try:
        x = int(x)
        return x
    except ValueError:
        print("Sorry, that's not a valid number.")
        quit()


# Check to make sure the user types a real number into the argument(s).
def check_arg(x):
    try:
        i = int(sys.argv[x])
        return i
    except IndexError:
        return None
    except ValueError:
        print("The value entered for argument "
              + str(x) + " is not a number; ignoring.")


# If the user uses arguments, process them to be used later.
length = check_arg(1)
number_of_generates = check_arg(2)


# Define the character set available for generation.
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"


# If the user hasn't used arguments, go ahead and get them now.
if number_of_generates is None:
    number_of_generates = input("\nHow many passwords would you "
                                + "like to generate? ")
    number_of_generates = check_input(number_of_generates)
if length is None:
    length = input("How long would you like to make your password? ")
    length = check_input(length)


"""
The actual generation part

NOTE: This script currently uses random.randint() to pick a character,
however it should be known that this is not the most secure and
completely random way to make a password.
"""
print()
for i in range(number_of_generates):
    for j in range(length):
        selected_character = random.randint(0, len(characters) - 1)
        print(characters[selected_character], end="")
    print("\n", end="")
