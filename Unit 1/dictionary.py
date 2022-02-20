import random

# Q1
freq1 = {}

for i in range(1000):
    n = random.randint(1, 10)
    if n not in freq1:
        freq1[n] = 1
    else:
        freq1[n] += 1
for i in range(1, 10):
    print(f'num {i}, chosen {freq1[i] / 10}% time')

# Q2
monthtonumber = {'JAN': 0, 'FEB': 1, 'MAR': 2, 'APR': 3, 'MAY': 4, 'JUN': 5, 'JUL': 6, 'AUG': 7, 'SEP': 8, 'OCT': 9,
                 'NOV': 10, 'DEC': 11}


def datedecoder(s):
    temp = (s.split("-"))
    temp[1] = monthtonumber[temp[1]]
    if int(temp[2]) > 22:
        temp[2] = "20" + temp[2] % 100
    else:
        temp[2] = "19" + temp[2]%100
    print(temp)


# for i in range()
print(datedecoder("8-MAR-85"))
