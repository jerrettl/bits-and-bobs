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
    points_achieved = 0
    points_total = 0
    global final_grade

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


def add_assignment():
    print("\nWhich category do you want to modify?")
    for i in range(number_of_categories):
        print("(" + str(i + 1) + ") " + str(weight[i]) + "%")
        # This will also include the name of the category once it is asked
    print()

    i = True
    while i is True:
        value = input("")
        if isint(value):
            if int(value) >= 1 and int(value) <= number_of_categories:
                category_to_change = int(value) - 1
                i = False

    print(str(category_to_change))

    # Ask for the points in the assignment
    # for i in range(assignment_points):
    # re-run the calculation formula (see lines 75-80)
    # with i out of assignment_points added to the
    # acheived_points and total_points arrays
    # then print the resulting percentage for the class


# first ask which function we're dealing with
class_type = ""
while class_type != "1" and class_type != "2":
    class_type = input("\nSelect the type of class:" + "\n(1) Categorized" +
                       "\n(2) Uncategorized\n\n")

if class_type == "1":
    calculate_categorized()
elif class_type == "2":
    calculate_uncategorized()

print("\nYour calculated grade is: " + str(final_grade) + "%")


# Now it's time to do something with these numbers!
action_type = ""
while action_type != "1" and action_type != "2":
    action_type = input("\nWhat would you like to do with " +
                        "your grades?" +
                        "\n(1) Nothing." +
                        "\n(2) Estimate the grade with a new assignment\n\n")

if action_type == "1":
    quit()
elif action_type == "2":
    add_assignment()
