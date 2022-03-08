import csv

marksDict = {}

with open('courseMarks.txt') as file_in:
    for course in file_in:
        line = course.split(",")
        studentID = line[0].strip()
        courseID = line[1].strip()
        finalmark = line[2].strip()
        if courseID not in marksDict:
            marksDict[courseID] = {}
        marksDict[courseID][studentID] = finalmark
print(marksDict)