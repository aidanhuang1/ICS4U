#Exercise 1

with open('allStudents.txt') as file_in:
    gr9 = []
    gr10 = []
    gr11 = []
    gr12 = []
    for line in file_in:
        line = line.strip()
        if line[0:2] == "09":
            stn_data = line.split("\t")
            student_name = ""
            student_name += stn_data[2].lower().capitalize() + " " + stn_data[1].lower().capitalize()
            gr9.append(student_name)
        elif line[0:2] == "10":
            stn_data = line.split("\t")
            student_name = ""
            student_name += stn_data[2].lower().capitalize() + " " + stn_data[1].lower().capitalize()
            gr10.append(student_name)
        elif line[0:2] == "11":
            stn_data = line.split("\t")
            student_name = ""
            student_name += stn_data[2].lower().capitalize() + " " + stn_data[1].lower().capitalize()
            gr11.append(student_name)
        elif line[0:2] == "12":
            stn_data = line.split("\t")
            student_name = ""
            student_name += stn_data[2].lower().capitalize() + " " + stn_data[1].lower().capitalize()
            gr12.append(student_name)
    print(gr9)
    print(gr10)
    print(gr11)
    print(gr12)
print()

#Exercise 2
with open('emailAddresses.txt') as file_in:
    yahoo = []
    hotmail = []
    gmail = []
    hdsb = []
    for line in file_in:
        line = line.strip()
        if "@fake" not in line and "@mail" not in line:
            if "@yahoo" in line:
                yahoo.append(line)
            elif "@hotmail" in line:
                hotmail.append(line)
            elif "@gmail" in line:
                gmail.append(line)
            elif "@hdsb" in line:
                hdsb.append(line)

    print(yahoo)
    print(hotmail)
    print(gmail)
    print(hdsb)

#Exercise 3

with open('Contra.txt') as line_in:
    for line in line_in:
        print(line[10], end='')