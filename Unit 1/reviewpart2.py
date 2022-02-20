import random


def evenoddlist(number_values, lowest, highest):
    list = []
    evencount = 0
    oddcount = 0
    while evencount < number_values / 2 or oddcount < number_values / 2:
        temp = random.randint(lowest, highest)
        if temp % 2 == 0 and evencount < number_values / 2:
            evencount += 1
            list.append(temp)
        elif temp % 2 != 0 and oddcount < number_values / 2:
            oddcount += 1
            list.append(temp)
    print(list)


print(evenoddlist(8, 0, 10))


def create_school_dictionary(school_codes, school_names):
    dict = {}
    for school in range(len(school_codes)):
        dict[school_codes[school]] = school_names[school]
    return dict

print(create_school_dictionary(['aph', 'irhs'], ['Abbey park', 'Iroquois Ridge']))

word = "yellowstone"
print( word[-11] )


number1 = int(input("input a number"))
print(f'{number1:>10.2f} is the inputted number')


import math

r = 5

print(f'Arc length in a circle with radius {r} units')

for degree in range(30, 360, 30):
   arc = (degree / 360) * (2 * math.pi * r)

   print(f'{r:>6} units {degree:>7} degree {arc:>10.2f} units')

# print(0/30)