
def selectionsort(list):

    # repeat (numOfElements - 1) times
    for i in range(len(list)):
        #   set the first unsorted element as the minimum
        minimum = list[i]
        for j in range(i+1, len(list)):  # for each of the unsorted elements
            if list[j] < minimum:  # if element < currentMinimum
                minimum = list[j]  # set element as new minimum
        list[i], minimum = minimum, list[i]  # swap minimum with first unsorted position

l = [32 ,1 ,4 ,32 ,5 ,43 ,21 ,63 ,32]
selectionsort(l)

print(l)