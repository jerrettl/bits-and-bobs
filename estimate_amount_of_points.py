#!/usr/bin/python3

from basic_checks import isfloat, isint

"""
estimate_amount_of_points() takes data in and returns a list with all
the points needed out of any hypothetical total points
"""


def est_points_calculation(points_achieved, points_total):
    max_points = ""
    threshold = ""
    while not isint(max_points):
        max_points = input("How many points would you like to check to?" +
                           " (Default: 120) ")
        if max_points == "":
            max_points = 120
            break
    while not isfloat(threshold) or float(threshold) > 1:
        threshold = input("What grade are you aiming for?" +
                          " (Default: 0.895) ")
        if threshold == "":
            threshold = 0.895
            break
    max_points = int(max_points)
    threshold = float(threshold)
    print("Calculating...")

    possible = False
    for i in range(max_points + 1):
        for j in range(i + 1):
            if ((points_achieved + j) / (points_total + i)) >= threshold:
                print(str(j) + "/" + str(i) + ": " +
                      str((points_achieved + j) / (points_total + i)))
                possible = True
                break

    if possible is False:
        print("It is not possible to add another assignment and get" +
              " a " + str(threshold * 100) + "% in the class" +
              " (up to " + str(max_points) + " points).")


def estimate_amount_of_points(class_type, data):
    # Grab variables from data
    if class_type == "1" or class_type == "3":  # Categorized
        number_of_categories = data[0]
        name = data[1]
        weight = data[2]
        points_achieved = data[3]
        points_total = data[4]

        print("There are", number_of_categories, "categories called",
              name, "with weights", weight)
    elif class_type == "2" or class_type == "4":  # Uncategorized
        points_achieved = data[0]
        points_total = data[1]

        est_points_calculation(points_achieved, points_total)
