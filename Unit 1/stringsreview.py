# Q1
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False


# if the letter is uppercase, then the function returns, but it should check the entire string instead of ending
# whenever it sees an uppercase letter.


def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


# 'c' is not a valid variable name

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag


# flag is outside the scope of the for loop

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag


# the boolean flag will never change its value (it will always remain false)

def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True


# the function will return whenever it reaches a letter that is uppercase, but it should keep iterating through
# the string

def is_palindrome(s):
    temp_s = s
    return s[:: -1] == temp_s


print(is_palindrome("anana"))


def rotate_word(s, shift):
    newword = ""

    for letter in s:
        if letter.islower():
            temp = (ord(letter) + shift)
            if temp > 122:
                temp %= 122
                newword += chr(96 + temp)
            else:
                newword += chr(temp)
        else:
            temp = (ord(letter) + shift)
            if temp > 90:
                temp %= 90
                newword += chr(64 + temp)
            else:
                newword += chr(temp)
    return newword


print(ord("a"), ord("z"), ord("A"), ord("Z"))
print(rotate_word("abcdefzABCDEFZ", 2))
