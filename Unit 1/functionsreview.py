# 1

def right_justify(s, n):
    for space in range(n):
        print(' ', end='')
    print(s)


print(right_justify("allen", 5))


# 2
def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod


def a(x, y):
    x = x + 1
    return x * y


def c(x, y, z):
    sum = x + y + z
    pow = b(sum) ** 2
    return pow


x = 1
y = x + 1
print(c(x, y + 3, x + y))


# 3

# def isDigit(s):
#     for letter in s:
#         if (ord(letter) - 57) > 9:
#             return False
#     return True

def isDigit(num):
    for i in range(0, len(num)):
        if num[i] not in "0123456789":
            return False


print(isDigit("3219047329432789524789427"))


def isFloat(s):
    if type(s) == float:
        return True
    else:
        return False


print(isFloat(1239942394395328954289.23))


# 4
def isLeapYear(someyear):
    if someyear % 100 == 0 and someyear % 400 == 0:
        return True
    elif someyear % 100 == 0:
        return False
    elif someyear % 4 == 0:
        return True
    else:
        return False


print(isLeapYear(1992))
