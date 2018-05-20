#!/usr/bin/python3


# append_to_array() takes the name of the array, the index, and what
# prompt to show while waiting to get a proper value


from basic_checks import isindex, isfloat


def append_to_array(array_name, x, prompt, array_type):
    while not isindex(array_name, x):
        input_value = input(prompt)
        if array_type is "float":
            if isfloat(input_value):
                array_name.append(float(input_value))
        elif array_type is "string":
            array_name.append(input_value)
