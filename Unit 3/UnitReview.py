# NOTE: TEST WILL COVER PRETTY EASY SORT AND SEARCH ALGORITHMS, AND IT WILL BE ON EASIER RECURSION PROBLEMS,
# LIKE THE ONE WITH PUTTING COMMAS, NOT THE ONE WITH FLATTENING LIST
import random

lista = [5, 4, 3, 6, 3]
listb = []

# print(random.randint(1,2))

a = [1,2,3,4,5,6,7,8,9]
for i in range(len(a)-1, 0, -1):
    print(a[i])


def isHexa(s):
    return True

def IPV(s):
    s = s.split(':')
    if len(s) != 8:
        return False
    else:
        for group in s:
            if len(group) != 4:
                return False
            for character in group:
                if not isHexa(character):
                    return False
    return True

print(IPV("2001:1000:1000:1000:1000:1000:1000:1000"))