import math
from datetime import datetime

width = 17
height = 12.0
delimiter = '.'
print(width / 2)
print(type(width / 2))

print(width / 2.0)
print(type(width / 2.0))

print(height / 3)
print(type(height / 3))

print(1 + 2 * 5)
print(type(1 + 2 * 5))

print(delimiter * 5)
print(type(delimiter * 5))


# Exercise 2

def vol(r):
    return (4 / 3) * math.pi * math.pow(r, 3)


print(vol(5))


def wholesalecost(coverprice, copies):
    discounted = coverprice - (coverprice * 0.4)
    totalcost = 0
    for i in range(copies - 1):
        totalcost += (0.75 + discounted)
    totalcost += 3
    return totalcost


print(wholesalecost(24.95, 60))

# startTime = 6*60*60 +52*60
# easyPace = 8*60 + 15#seconds



startTime = datetime.datetime(1, 1, 1, 6, 52, 0)
easyPace = datetime.timedelta(minutes=8, seconds=15)
tempoPace = datetime.timedelta(minutes=7, seconds=12)
print(startTime+easyPace*2+tempoPace*3)



# 3
p = 110000
r = 0.0725 / 12
n = 30 * 12
m = p * (r / (1 - (pow(1 + r, -n))))
print(m)

test = 10
print(f'Hey {test:>10.2f}')