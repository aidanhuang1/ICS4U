def bubble_sort(a_list):
    swapped = True
    index_of_last_unsorted_item = len(a_list)

    while swapped:
        swapped = False

        for i in range(0, index_of_last_unsorted_item - 1):

            ##  if left_element > right_element
            if a_list[i] > a_list[i + 1]:
                # swap(left_element, right_element)
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]

            ## swapped = true
            swapped = True
        index_of_last_unsorted_item -= 1


a = [5, 4, 6, 2, 4, 6, 7, 8, 1]
bubble_sort(a)
print(a)
