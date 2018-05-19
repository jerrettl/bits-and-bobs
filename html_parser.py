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
