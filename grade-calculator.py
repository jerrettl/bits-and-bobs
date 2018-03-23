import time

def isint(x):
    try:
        int(x)
        return True
    except:
        return False

def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False

def calculate_categorized():
    # we need to ask how many categories we're about to collect data for
    number_of_categories = ""
    while not isint(number_of_categories):
        input_value = input("What is the number of grade categories? ")
        if isint(input_value):
            number_of_categories = int(input_value)

    # Initialize variables
    total = 0
    weight = []
    points_achieved = []
    points_total = []

    # Time to ask about the category's weight, and points out of points total
    for x in range(number_of_categories):
        weight_input = float(input("[" + str(x + 1) + "/" + str(number_of_categories) + "] % weight of category #" + str(x + 1) + "? "))
        if isfloat(weight_input):
            weight.append(weight_input)
        else:
            print("This is not a valid number.")
            exit()

        points_achieved_input = float(input("[" + str(x + 1) + "/" + str(number_of_categories) + "] Points achieved in category #" + str(x + 1) + "? "))
        if isfloat(points_achieved_input):
            points_achieved.append(points_achieved_input)
        else:
            print("This is not a valid number.")
            exit()

        points_total_input = float(input("[" + str(x + 1) + "/" + str(number_of_categories) + "] Points total in category #" + str(x + 1) + "? "))
        if isfloat(points_total_input):
            points_total.append(points_total_input)
        else:
            print("This is not a valid number.")
            exit()

        print()

    for x in range(number_of_categories):
        value = float(points_achieved[x] / points_total[x] * weight[x] / 100)
        total = total + value

    print("Your calculated grade is: " + str(total * 100) + "%")

# print("Hey there! ever wanted to see how bad you're failing in school", end="\r")
# time.sleep(2)

# print("Hey there! ever wanted to calculate your grades               ")
# time.sleep(2)

# first ask which function we're dealing with
input_text = input("\nSelect the type of class:" + "\n(1) Categorized" +
                   "\n(2) Uncategorized\n\n")


if input_text == "1":
    class_type = "categorized"
elif input_text == "2":
    class_type = "uncategorized"
else:
    print("wrong")
    exit()



if class_type == "categorized":
    calculate_categorized()

elif class_type == "uncategorized":
    # we only need points/total
    print("Enter all the achieved points from each assignment separated with" +
          " enter: \n" +
          "Type anything that isn't a number when you are done.\n")
    achieved_points = 0
    total = 0
    x = True
    while x == True:
        value = input("")
        if isfloat(value):
            achieved_points = achieved_points + float(value)
        else:
            x = False

    print("\nNow enter the maximum possible scores of each assignment separated with enter:\n")
    x = True
    while x == True:
        value = input("")
        if isfloat(value):
           total = total + float(value)
        else:
            x = False

    print("Your calculated grade is: " + str(achieved_points / total * 100) + "%")


