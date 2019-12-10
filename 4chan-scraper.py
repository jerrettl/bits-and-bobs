#!/usr/bin/python3

from bs4 import BeautifulSoup
from os import listdir
from re import sub, findall
import csv

files = listdir("./specimens/")
files_to_scrape = []
# files_to_scrape = ["file12.html"]
word_list = []
word_freq = {}
total_word_count = 0

most_common_words = ["the", "be", "to", "of", "and", "a", "in", "that", "have", "i", "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", "back", "after", "use", "two", "how", "our", "work", "first", "well", "way", "even", "new", "want", "because", "any", "these", "give", "day", "most", "us"]

# Scan for all the html files in the specimens folder.
for file in files:
	if ".html" in file:
		files_to_scrape.append(file)

for file in files_to_scrape:
	try:
		f = open(f"./specimens/{file}", "r")
	except FileNotFoundError:
		continue

	print(f"Scraping file {files_to_scrape.index(file) + 1} / {len(files_to_scrape)} ({file})")

	# Gather a list of all the posts in the html file.
	soup = BeautifulSoup(f.read(), 'html.parser')
	posts = soup.find_all("blockquote", class_="postMessage")

	raw_data = []
	for post in posts:
		# Clean up the posts.
		post = sub(r">>[0-9]{6,10}", "", post.get_text())
		post = sub(r">", "", post)
		post = sub(r"''", "", post)

		# Dump the data into one spot.
		raw_data.append(findall(r"[\w']+", post))

	# raw_data is a list of a list of words.
	# This needs to be "flattened" into simply a list of words.
	flattened_data = []
	for sublist in raw_data:
		for item in sublist:
			flattened_data.append(item)

	# Set all the words to lowercase to avoid creating multiple entries for the same word.
	for i in range(len(flattened_data)):
		flattened_data[i] = flattened_data[i].lower()

	# print(flattened_data)

	# Every word is counted then placed into a master word list and a dict with word frequencies.
	for word in flattened_data:
		total_word_count += 1
		if word not in word_list:
			word_list.append(word)
			word_freq[word] = 1
		else:
			word_freq[word] += 1

print("Data scraped. Exporting to CSV...")

# Sort the word dict and put it in a new array.
sorted_count = [(i, word_freq[i]) for i in sorted(word_freq, key=word_freq.get, reverse=True)]

# print(sorted_count)

# Open a csv file to edit.
try:
	csvfile = open('data.csv', 'w')
except PermissionError:
	print("Permission to edit 'data.csv' denied. Perhaps you have it open in another program?")
	quit()
csvwriter = csv.writer(csvfile)

try:
	csvfile2 = open('data-no-common-words.csv', 'w')
except PermissionError:
	print("Permission to edit 'data-no-common-words.csv' denied. Perhaps you have it open in another program?")
	quit()
csvwriter2 = csv.writer(csvfile2)

try:
	csvfile3 = open('bad-words.csv', 'w')
except PermissionError:
	print("Permission to edit 'bad-words.csv' denied. Perhaps you have it open in another program?")
	quit()
csvwriter3 = csv.writer(csvfile3)

# Write all the data to a csv file.
for i in sorted_count:
	csvwriter.writerow([i[0], i[1], (i[1] / total_word_count) * 100])
	if i[0] not in most_common_words:
		csvwriter2.writerow([i[0], i[1], (i[1] / total_word_count) * 100])
	if "fuck" in i[0]:
		csvwriter3.writerow(["fuck", i[1], (i[1] / total_word_count) * 100])
	if "shit" in i[0]:
		csvwriter3.writerow(["shit", i[1], (i[1] / total_word_count) * 100])
	if "white" in i[0]:
		csvwriter3.writerow(["white", i[1], (i[1] / total_word_count) * 100])
	if "boomer" in i[0]:
		csvwriter3.writerow(["boomer", i[1], (i[1] / total_word_count) * 100])
	if "fag" in i[0]:
		csvwriter3.writerow(["fag", i[1], (i[1] / total_word_count) * 100])
	if "jew" in i[0]:
		csvwriter3.writerow(["jew", i[1], (i[1] / total_word_count) * 100])
	if "retard" in i[0]:
		csvwriter3.writerow(["retard", i[1], (i[1] / total_word_count) * 100])
	if "nigg" in i[0]:
		csvwriter3.writerow(["nigg", i[1], (i[1] / total_word_count) * 100])
	if "ass" in i[0]:
		csvwriter3.writerow(["ass", i[1], (i[1] / total_word_count) * 100])
	if "trann" in i[0]:
		csvwriter3.writerow(["trann", i[1], (i[1] / total_word_count) * 100])
	if "kike" in i[0]:
		csvwriter3.writerow(["kike", i[1], (i[1] / total_word_count) * 100])

print("Completed successfully.")
