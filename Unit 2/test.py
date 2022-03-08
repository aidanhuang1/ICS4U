import csv

tt = ["abc", "def", "cdef"]

print(tt[1][:])

with open("flavors_of_cacao.csv") as csv_file:
    csv_reader = csv.reader(csv_file) #csv_reader is an object
    # print(csv_reader)
    beanEntry = []
    csv_dictreader = csv.DictReader(csv_file)
    for line in csv_dictreader: # row is a dictionary
        # print(line)
        beanEntry.append([line['bean_origin'], int(line['review_date']), float(line['cocoa_percent'][:-1]),
                     float(line['rating'])])
    for i in beanEntry:
        print(i)


line = "abcdefgaf: "
print(len(line))
line = line.strip().replace('a', '\n') #replace will replace all of them
print(line)


splittingstring = "0.994772 0.023164 -0.099456 28 4.61 3"
splittinglist = splittingstring.split(" ", 5) # optional parameter, how many delimiters do you want to count
print(splittinglist[:4])
print(splittinglist)

with open('stars.txt') as file_in:
    print(file_in.readlines()[0])