#!/usr/bin/python3

from basics import single_input_int, isint, isfloat
import copy


def new_assignment(data):
    # Adds a hypothetical new assignment to the class and
    # determines how it impacts the final grade.

    # Define the maximum points the assignment can add.
    new = single_input_int("How many points is the new assignment worth? ")

    # For every possibiliy on this assignment, show the result.
    if data.type == "uncategorized":
        for i in range(new + 1):
            total = (data.points_achieved + i) / (data.points_total + new) * 100
            print(str(i) + "/" + str(new) + ": " + str(round(total, 3)) + "%")


    if data.type == "categorized":
        # Ask the user which category to add to
        print("\nWhich category do you want to modify?")
        for i in range(len(data.category_name)):
            print(f"({str(i)}) {data.category_name[i]} - {str(data.category_weight[i])}%")
        print()

        # Make sure what the user types is a valid number before continuing
        while True:
            value = single_input_int("")
            if 0 <= value <= (len(data.category_name) - 1):
                changed_category = value
                break

        # For every possibiliy on this assignment, show the result.
        for i in range(new + 1):
            # Create a copy of the data class and change it to simulate that scenario
            data_mod = copy.deepcopy(data)
            data_mod.category_achieved[changed_category] += i
            data_mod.category_total[changed_category] += new

            # Re-calculate the class average
            data_mod.get_class_average()

            # Show the outcome for that possibility
            print(f"{str(i)}/{str(new)}: {data_mod.class_average}%")


    # Warn the user if there was a lot of output
    if new > 30:
        print("\nWarning! Your screen may be filled too much to see all the "
              "possible scores! You may need to scroll back to see them all.")


def points_to_threshold(data):
    # Takes a given desired grade and determines the minimum number of points needed to achieve that

    # Ask the user how far to keep checking
    max_points = ""
    while not isint(max_points):
        max_points = input("How many points would you like to check to? "
                           "(Default: 120) ")
        if max_points == "":
            max_points = 120
            break
    max_points = int(max_points)

    # Ask the user for their desired grade
    threshold = ""
    while not isfloat(threshold) or float(threshold) > 1:
        threshold = input("What grade are you aiming for? "
                          "(Default: 0.895) ")
        if threshold == "":
            threshold = 0.895
            break
    threshold = float(threshold)


    if data.type == "uncategorized":
        possible = False
        for i in range(max_points + 1):
            for j in range(i + 1):
                if ((data.points_achieved + j) / (data.points_total + i)) >= threshold:
                    print(f"{str(j)}/{str(i)}: {str((data.points_achieved + j) / (data.points_total + i))}")
                    possible = True
                    break


    if data.type == "categorized":
        # Prompt for which category to change
        print("\nWhich category do you want to modify?")
        for i in range(len(data.category_name)):
            print(f"({str(i)}) {data.category_name[i]} - {str(data.category_weight[i])}%")
        print()

        # Make sure what the user types is a valid number before continuing
        while True:
            value = single_input_int("")
            if 0 <= value <= (len(data.category_name) - 1):
                changed_category = value
                break

        possible = False
        for i in range(max_points + 1):
            for j in range(i + 1):
                if ((data.category_achieved[changed_category] + j) / (data.category_total[changed_category] + i)) >= threshold:
                    print(f"{str(j)}/{str(i)}: {str(round((data.category_achieved[changed_category] + j) / (data.category_total[changed_category] + i) * 100, 3))}%")
                    possible = True
                    break


    if possible is False:
        print(f"It is not possible to add another assignment and get a {str(threshold * 100)}% in the class (up to {str(max_points)} points).")
