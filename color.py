#!/usr/bin/python3

from termcolor import cprint

colors = {
    1: "red",
    2: "yellow",
    3: "green",
    4: "cyan",
    5: "blue",
    6: "magenta",
    7: "white"
}

for x in range(1, 8):
    color_select = colors.get(x)
    cprint("it's " + color_select + "!", color=color_select)
