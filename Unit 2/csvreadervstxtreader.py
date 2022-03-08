import csv

with open('ramen-ratings.csv') as file_in:
    reader = csv.reader(file_in)
    for line in reader:
        print(line)
    for line in file_in:
        print(line)