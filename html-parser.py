#!/usr/bin/python3

from bs4 import BeautifulSoup

f = open("english.html", "r")
html = f.read()
soup = BeautifulSoup(html, 'html.parser')


assignments = soup.find('table', id="Assignments")
assignment_list = assignments.find_all('tr')

for i in assignment_list:
    for j in i.find("td", class_="numeric"):
        for k in j.find("span"):
            print(k.string)
