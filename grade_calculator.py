#!/usr/bin/python3


import data_extract, data_manipulate, html_import


def class_average_output(data):
    print("=" * 40 + "\n")
    print(f"   Your calculated grade is: {data.class_average}%\n")
    print("=" * 40 + "\n")


def process_data(data):
    # Ask the user what to do with the data
    action_type = ""
    while action_type not in ("0", "1", "2", "3"):
        action_type = input("\nWhat would you like to do with your data?"
                            "\n(0) Edit data"
                            "\n(1) Add hypothetical assignment"
                            "\n(2) Estimate the points needed for a desired grade"
                            "\n(3) Nothing, exit\n\n")
    action_type = int(action_type)

    # Define what the different options will do
    data_manipulation_methods = {
        0: data_extract.edit,
        1: data_manipulate.new_assignment,
        2: data_manipulate.points_to_threshold,
        3: exit
    }

    # Perform the user's action
    data_manipulation_methods.get(action_type)(data)

    # If the data was changed, redisplay the class average
    if action_type == 0:
        class_average_output(data)

    # Ask to do something else with the data
    process_data(data)


def main():
    print("=" * 40 + "\n")
    print("    G R A D E   C A L C U L A T O R\n")
    print("=" * 40 + "\n")

    # Ask the user what kind of data should be asked for
    class_type = ""
    while class_type not in ("0", "1", "2"):
        class_type = input("\nSelect the type of class:"
                           + "\n(0) Import HTML"
                           + "\n(1) Uncategorized"
                           + "\n(2) Categorized\n\n")
    class_type = int(class_type)

    # The type of grade structure determines the method of data extraction
    data_extraction_methods = {
        0: html_import.main,
        1: data_extract.uncategorized,
        2: data_extract.categorized
    }

    # Get all the data and save it (the parameter 1 says this will be a new class)
    data = data_extraction_methods.get(class_type)(1)

    if data is None:
        exit()

    # Display the class average
    class_average_output(data)

    # Do something with the data
    process_data(data)


main()
