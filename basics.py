#!/usr/bin/python3


def isint(x):
    try:
        int(x)
        return True
    except ValueError:
        return False


def isfloat(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


def isindex(name, index):
    try:
        name[index]
        return True
    except IndexError:
        return False


def single_input_float(prompt):
    # Take an input and only accept it when it is a float.
    # This prevents the user from entering non-numbers where numbers
    # are needed.

    while True:
        value = input(prompt)
        if isfloat(value):
            return float(value)


def single_input_int(prompt):
    # Take an input and only accept it when it is a float.
    # This prevents the user from entering non-numbers where numbers
    # are needed.

    while True:
        value = input(prompt)
        if isint(value):
            return int(value)


def list_input_float(var):
    # Starting at var (usually set to 0), continuously prompt the user
    # for numbers, adding those values to var until the user types
    # something that isn't a number.

    while True:
        value = input("")
        if isfloat(value):
            var += float(value)
        else:
            return var


def list_input_string():
    # Prompt the user for strings until an empty string is entered.
    # For each string, add it to an array to be output.

    array = []

    while True:
        value = input("")
        if value != "":
            array.append(value)
        else:
            return array
