import random

occupations = []
names = []

with open('occupations.txt') as file_in:
    for line in file_in:
        occupations.append(line.strip())
with open('randomnames.txt') as file_in:
    for line in file_in:
        names.append(line.strip())
print(occupations)
print(names)
with open('ficticiouspeople.txt', 'w') as file_out:
    for name in names:
        idnumber = random.randint(0, 9999)
        salary = random.randint(25000, 125000)
        file_out.write(f'{idnumber}-{name}-{salary}\n')