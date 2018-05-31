#!/usr/bin/python3


"""
estimate_amount_of_points() takes data in and returns a list with all
the points needed out of any hypothetical total points
"""


def estimate_amount_of_points(class_type, data):
    # Grab variables from data
    if class_type == "1":  # Categorized
        number_of_categories = data[0]
        name = data[1]
        weight = data[2]
        points_achieved = data[3]
        points_total = data[4]
    elif class_type == "2":  # Uncategorized
        points_achieved = data[0]
        points_total = data[1]

    if class_type == "1":  # Categorized
        print("There are", number_of_categories, "categories called",
              name, "with weights", weight)

    elif class_type == "2":  # Uncategorized
        print("You have", points_achieved, "out of", points_total)

        # How far will we check for hypothetical grades?
        max_points = 200

    elif class_type == "3" or class_type == "4":
        print(data)
