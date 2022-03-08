import csv

with open('unit2review.txt') as file_in:  # .txt file
    file_in.readline()  # skips the first line
    print(file_in.read())



with open('unit2review.csv') as file_in:
    ratingentry = [] # create the list that you want of all the information
    reader = csv.DictReader(file_in) # create the reader pointer for the .csv file
    for line in reader: # iterate through all the lines
        ratingentry = [line["Review #"], line["Brand"], line['Stars']] # Case sensitive and letter sensitive; make sure the headers
        # are spelled correctly!
        print(ratingentry)