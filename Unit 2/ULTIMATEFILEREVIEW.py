# opening the file, file_in is the pointer
import csv

file_in_txt = open('allStudents.txt')
file_in_csv = open('ramen-ratings.csv')

# If it is a .txt file ------------------------------------------------------------------

# returns the line that it is being pointed to and moves on to the next line.
print(file_in_txt.readline())

# returns the entire file as a list of strings and pointer moves to the end
file_in_txt.readlines()

# returns the entire file as strings
file_in_txt.read()

# If it is a .csv file ------------------------------------------------------------------

# difference between csv.reader vs iterating line by line is that the csv.reader returns a list, while the iterating
# method returns strings

reader1 = csv.reader(file_in_csv)

#DO NOT USE .readline() IF THE HEADER IS ALREADY AT THE TOP. csv.DictReader already takes the header and knows
# reader2 = csv.DictReader(file_in_csv)


for line in reader1:
    print(line)
# for line in reader2:
#     print(line)

file_in_csv.close()
file_in_txt.close()

# Writing to file ------------------------------------------------------

file_out_txt = open('ultimatefilereview.txt', 'w')  # .txt file
file_out_csv = open('ultimatefilereview.csv', 'w')  # .csv file

# using .txt writer
writing = "test"
file_out_txt.write(writing)
file_out_txt.write(writing)

file_out_txt.write(writing)


# using .csv writer
# writer = csv.writer(file_out_csv)
# writinglist = ["hey", "hello", "there"]
# writer.writerow(writinglist)  # .csv writes lists or tuples

file_out_csv.close()
file_out_txt.close()

# s = glob.glob('')
