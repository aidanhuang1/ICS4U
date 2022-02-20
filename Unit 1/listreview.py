# Q4

def is_sorted(lis):
    prevelement = lis[0]
    for element in lis:
        if element < prevelement:
            return False
        prevelement = element
    return True


print(is_sorted(['b', 'b']))


# Q5
def has_duplicates(lis):
    for element in lis:
        if (lis.count(element) > 1):
            return True
    return False


print(has_duplicates([1, 2, 3, 4, 5]))

#Q6
