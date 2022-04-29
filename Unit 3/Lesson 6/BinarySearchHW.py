def binarysearch(aList, T):
    if T < min(aList):
        return 0
    elif T > max(aList):
        return len(aList)

    list.sort(aList)
    L = 0
    R = len(aList) - 1
    m = (L + R) // 2  # the final value of m will be the index that you want

    while R >= L:
        m = (L + R) // 2  # the final value of m will be the index that you want
        if T < aList[m]:
            R = m - 1
        elif T > aList[m]:
            L = m + 1
        else:
            return m


    return m  # return m+1, not just m because you are inserting at position m

def inserttolist(list, x):
    list.insert(binarysearch(list, x+1), x)

a = [3, 4, 4, 6, 8, 10, 14, 14]
# a = [ 1, 3, 4, 4, 6, 8, 10, 14, 14 ]
inserttolist(a, 1)
print(a)

b = [3, 4, 4, 6, 8, 10, 14, 14]
# b = [ 3, 4, 4, 5, 6, 8, 10, 14, 14 ]
inserttolist(b, 4)
print(b)
