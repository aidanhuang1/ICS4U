
def insertionsort(list):
    # mark first element as sorted

    for i in range(1, len(list)):
        if list[i-1]>list[i]:# for each unsorted element X
            #  'extract' the element X
            for j in range(i, 0, -1): #  for j = lastSortedIndex down to 0
                #    if current element j > X
                if list[j-1] > list[j]:
                    list[j], list[j-1] = list[j-1], list[j] # move sorted element to the right by 1
                else:
                    break #break loop and insert X here

l = [12,43,54,32,5,76,43,32,1243,564]
insertionsort(l)
print(l)
