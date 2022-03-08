import csv

with open('people.csv', 'r') as file:
    reader = csv.reader(file)  # default delimiter is ","
    for row in reader:
        print(row)
