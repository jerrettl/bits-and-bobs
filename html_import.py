#!/usr/bin/python3


from bs4 import BeautifulSoup
from data_extract import Class


def main(new):
    # Prompt to import file and wait for a proper file name
    while True:
        file_name = input("What is the name of the file you would"
                          + " like to import?\n")
        try:
            f = open(file_name, "r")
            break
        except FileNotFoundError:
            continue

    soup = BeautifulSoup(f.read(), 'html.parser')

    # If the table is found call it categorized
    if soup.find('table', id="Categories"):
        return categorized(file_name)
    else:
        return uncategorized(file_name)


def uncategorized(file_name):
    grades = Class("uncategorized")
    soup = BeautifulSoup(open(file_name, "r").read(), 'html.parser')

    grades.is_html = 1
    grades.points_achieved = 0
    grades.points_total = 0

    # Find the assignments table in the html
    assignment_list = soup.find("table", id="Assignments").find_all("tr")

    # Dig through each column of the table for data then add to the total
    for i in assignment_list:
        i_achieved = i.find('span', class_="points").string
        i_total = i.find('span', class_="max").string.split(' ')[1]

        # Assignments without an entered value do not count to the final grade
        if i_achieved is None:
            i_achieved = 0
            i_total = 0

        # X assignments are not counted to grades
        if i.find('div', class_='letter').string == "X":
            i_achieved = 0
            i_total = 0

        # Assignments with a Z are the same as a 0
        if i.find('div', class_='letter').string == "Z":
            i_achieved = 0

        # Add the assignment to the stack of total assignments
        grades.points_achieved += float(i_achieved)
        grades.points_total += float(i_total)

    # Calculate the resulting class average
    grades.get_class_average()

    return grades


def categorized(file_name):
    grades = Class("categorized")
    soup = BeautifulSoup(open(file_name, "r").read(), 'html.parser')

    category_list = soup.find("table", id="Categories").find_all("tr")

    grades.category_name = []
    grades.category_weight = []
    grades.category_achieved = []
    grades.category_total = []

    for i in category_list:
        i_name = i.find('td', class_='description').contents[0].strip()
        i_weight = float(i.find('span', class_='percent').contents[0].split()[0].split('%')[0])
        i_achieved = float(i.find('span', class_='points').string)
        i_total = float(i.find('span', class_='text-muted').string)

        # Take the extracted information and place them in their corresponding arrays
        grades.category_name.append(i_name)
        grades.category_weight.append(i_weight)
        grades.category_achieved.append(i_achieved)
        grades.category_total.append(i_total)

    grades.get_class_average()

    return grades
