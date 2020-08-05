#!/usr/bin/python3


import basics


class Class:
    def __init__(self, type):
        self.type = type


    def get_class_average(self):
        # Simple division to get a class average
        if self.type == "uncategorized":
            try:
                self.class_average = round(self.points_achieved / self.points_total * 100, 3)
            except ZeroDivisionError:
                self.class_average = 0

        # Calculate the total grade by taking the sum of the percents from each category
        if self.type == "categorized":
            total = 0
            for i in range(len(self.category_name)):
                try:
                    weighted_category = float(self.category_achieved[i] /
                                              self.category_total[i] * self.category_weight[i])
                except ZeroDivisionError:
                    weighted_category = 0
                total += weighted_category
            self.class_average = round(total, 3)


def uncategorized(new, data = None):
    if new == 1:
        # Create a new class where its data will be saved as its attributes
        grades = Class("uncategorized")
    else:
        # If there is an existing class, use that one
        grades = data

    # Set the points earned in the class
    print("\nEnter all the achieved points from each assignment separated "
          "with enter.\nType anything that isn't a number when you "
          "are done.\n")
    grades.points_achieved = basics.list_input_float(0)

    # Set the points possible in the class
    print("Now enter the maximum possible scores of each assignment "
          "separated with enter:\n")
    grades.points_total = basics.list_input_float(0)

    # Calculate the resulting class average
    grades.get_class_average()

    return grades


def categorized(new, data = None):
    if new == 1:
        # Create a new class where its data will be saved as its attributes
        grades = Class("categorized")
    else:
        # If there is an existing class, use that one
        grades = data

    # Ask the user for the names of each category
    print("List the names of categories in this class. Finish with a blank name.")
    grades.category_name = basics.list_input_string()

    # Then ask the user for the % weight, points achieved, and points total
    # for each category.
    grades.category_weight = []
    grades.category_achieved = []
    grades.category_total = []

    for i in range(len(grades.category_name)):
        grades.category_weight.append(basics.single_input_float(f"[{str(i+1)}/{str(len(grades.category_name))}] % weight of {grades.category_name[i]}? "))

        grades.category_achieved.append(basics.single_input_float(f"[{str(i+1)}/{str(len(grades.category_name))}] Points achieved in {grades.category_name[i]}? "))

        grades.category_total.append(basics.single_input_float(f"[{str(i+1)}/{str(len(grades.category_name))}] Points total in {grades.category_name[i]}? "))

        # Space after every category
        print()

    # Calculate the resulting class average
    grades.get_class_average()

    return grades


def edit(data):
    if data.type == "uncategorized":
        return uncategorized(0, data)
    if data.type == "categorized":
        return categorized(0, data)
    else:
        exit()
