#!/usr/bin/python3

from bs4 import BeautifulSoup


def calculate_html_uncategorized():
    # Initialize variables
    points_achieved = 0
    points_total = 0

    # Prompt to import file and wait for a proper file name
    while True:
        file_name = input("What is the name of the file you would"
                          + " like to import?\n")
        try:
            f = open(file_name, "r")
            break
        except FileNotFoundError:
            continue

    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find the assignments table in the html
    assignments = soup.find('table', id="Assignments")
    assignment_list = assignments.find_all('tr')

    # Dig through each column for the point values in them
    for i in assignment_list:
        points_achieved_temp = i.find('span', class_="points").string
        points_total_temp = i.find('span', class_="max").string.split(' ')[1]

        # Assignments without an entered value do not count
        if points_achieved_temp is None:
            points_achieved_temp = 0
            points_total_temp = 0

        # X assignments are not counted to grades
        if i.find('div', class_='letter').string == "X":
            points_achieved_temp = 0
            points_total_temp = 0

        points_achieved += float(points_achieved_temp)
        points_total += float(points_total_temp)

    try:
        final_grade = points_achieved / points_total * 100
    except ZeroDivisionError:
        final_grade = 0

    return points_achieved, points_total, final_grade


def calculate_html_categorized():
    # Initialize variables
    name = []
    weight = []
    points_achieved = []
    points_total = []

    # Prompt to import file and wait for a proper file name
    while True:
        file_name = input("What is the name of the file you would"
                          + " like to import?\n")
        try:
            f = open(file_name, "r")
            break
        except FileNotFoundError:
            continue

    html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    categories = soup.find('table', id="Categories")
    category_list = categories.find_all('tr')

    final_grade = 0
    for i in category_list:
        name_temp = i.find('td', class_='description').contents[0].strip()
        weight_temp = i.find('span', class_='percent').contents[0]\
            .split()[0].split('%')[0]
        points_achieved_temp = i.find('span', class_='points').string
        points_total_temp = i.find('span', class_='text-muted').string

        name.append(name_temp)
        weight.append(float(weight_temp))
        points_achieved.append(float(points_achieved_temp))
        points_total.append(float(points_total_temp))

    number_of_categories = len(name)
    for i in range(number_of_categories):
        try:
            weighted_category = float(points_achieved[i] / points_total[i] *
                                      weight[i])
        except ZeroDivisionError:
            weighted_category = 0

        final_grade += weighted_category

    return number_of_categories, name, weight, points_achieved,\
        points_total, final_grade
