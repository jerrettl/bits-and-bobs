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


def append_to_array(array_name, x, prompt):
    while not isindex(array_name, x):
        input_value = input(prompt)
        if isfloat(input_value):
            array_name.append(float(input_value))
def get_class_type():
    class_type = ""
    while class_type != "1" and class_type != "2":
        class_type = input("\nSelect the type of class:" + "\n(1) Categorized"
                           + "\n(2) Uncategorized\n\n")
    return class_type


def get_action_type():
    action_type = ""
    while action_type != "1" and action_type != "2":
        action_type = input("What would you like to do with " +
                            "your grades?" +
                            "\n(1) Estimate the grade with a new assignment." +
                            "\n(2) Nothing.\n\n")
    return action_type


def calculate_categorized():
    # Initialize variables
    total = 0
    global number_of_categories
    global final_grade
    global weight
    global points_achieved
    global points_total
    number_of_categories = ""
    weight = []
    points_achieved = []
    points_total = []

    # we need to ask how many categories we're about to collect data for
    while not isint(number_of_categories):
        input_value = input("What is the number of grade categories? ")
        if isint(input_value):
            number_of_categories = int(input_value)

    # Time to ask about the category's weight, and points out of points total
    # append_to_array() takes the name of the array, the index, and what
    # prompt to show while waiting to get a proper value
    for i in range(number_of_categories):
        # TODO: Ask for the name of the category
        append_to_array(weight, i, "[" + str(i + 1) + "/" +
                        str(number_of_categories) + "] % weight of category #"
                        + str(i + 1) + "? ")

        append_to_array(points_achieved, i, "[" + str(i + 1) + "/" +
                        str(number_of_categories) + "] Points achieved in " +
                        "category #" + str(i + 1) + "? ")

        append_to_array(points_total, i, "[" + str(i + 1) + "/" +
                        str(number_of_categories) + "] Points total in " +
                        "category #" + str(i + 1) + "? ")

        # Space after every category
        print()

    # Calculate the total grade by taking the sum of the percents from each
    # category
    for i in range(number_of_categories):
        weighted_category = float(points_achieved[i] / points_total[i] *
                                  weight[i])
        total = total + weighted_category

    final_grade = total


def calculate_uncategorized():
    # Initialize variables
    global final_grade
    global points_achieved
    global points_total
    points_achieved = 0
    points_total = 0

    # we only need points and total
    print("Enter all the achieved points from each assignment separated with" +
          " enter: \n" +
          "Type anything that isn't a number when you are done.\n")
    x = True
    while x is True:
        value = input("")
        if isfloat(value):
            points_achieved = points_achieved + float(value)
        else:
            x = False

    print("\nNow enter the maximum possible scores of each assignment " +
          "separated with enter:\n")
    x = True
    while x is True:
        value = input("")
        if isfloat(value):
            points_total = points_total + float(value)
        else:
            x = False

    try:
        final_grade = points_achieved / points_total * 100
    except ZeroDivisionError:
        final_grade = 0


def add_assignment_categorized():
    print("\nWhich category do you want to modify?")
    for i in range(number_of_categories):
        print("(" + str(i + 1) + ") " + str(weight[i]) + "%")
        # This will also include the name of the category once it is asked
    print()

    # Make sure what the user types is a valid number before continuing
    i = True
    while i is True:
        value = input("")
        if isint(value):
            if int(value) >= 1 and int(value) <= number_of_categories:
                category_to_change = int(value) - 1
                i = False

    x = True
    while x is True:
        value = input("How many points is the new assignment worth? ")
        if isint(value):
            assignment_points = int(value)
            x = False

    # For every possible score out of the total, calculate the resulting total
    # average in the class
    for i in range(assignment_points + 1):
        # Reset the total percentage every time we finish calculating
        total = 0
        for j in range(number_of_categories):
            # When finding the weighted percents from all categories again, if
            # the category we get to is the one we need to change, add those
            # changes
            if category_to_change is j:
                weighted_category = float((points_achieved[j] + i) /
                                          (points_total[j] + assignment_points)
                                          * weight[j])
            else:
                weighted_category = float(points_achieved[j] / points_total[j]
                                          * weight[j])
            total = total + weighted_category
        # Show the score out of the total and then show the percent in the
        # class
        print(str(i) + "/" + str(assignment_points) + ": " + str(total) + "%")


def add_assignment_uncategorized():
    # TODO: Make this into a defined function
    x = True
    while x is True:
        value = input("How many points is the new assignment worth? ")
        if isint(value):
            assignment_points = int(value)
            x = False

    for i in range(assignment_points + 1):
        total = (points_achieved + i) / (points_total +
                                         assignment_points) * 100
        print(str(i) + "/" + str(assignment_points) + ": " + str(total) + "%")



def main():
    print("=" * 40 + "\n")
    print("     G R A D E   C A L C U L A T O R    ")
    print("\n" + "=" * 40 + "\n")
    class_type = get_class_type()
    if class_type == "1":
        calculate_categorized()
    elif class_type == "2":
        calculate_uncategorized()

    print("=" * 40 + "\n")
    print("   Your calculated grade is: " + str(final_grade) + "%")
    print("\n" + "=" * 40 + "\n")

    action_type = get_action_type()
    if action_type == "1":
        if class_type == "1":
            add_assignment_categorized()
        elif class_type == "2":
            add_assignment_uncategorized()
    elif action_type == "2":
        quit()


main()
