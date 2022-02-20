import math

n = int(input())
bestbid = 0
bestname = ""
for i in range(n):
    name = input()
    bid = int(input())
    if bid>bestbid:
        bestbid = bid
        bestname = name
print(bestname)