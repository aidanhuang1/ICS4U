def money_counting_sort_using_set(a_list): # just using a different data structure
    unique_money_values = set(a_list)
    unique_money_values = sorted(unique_money_values)
    counting_key = {}
    for value in unique_money_values:
        counting_key[value] = 0
    for value in a_list:
        counting_key[value] += 1

    sorted_list = []
    for value in counting_key:
        counter = counting_key[value]

        while counter > 0:
            sorted_list.append(value)
            counter -= 1

    return sorted_list


def money_counting_sort(a_list):
    counting_key = {}
    money_values = [0.05, 0.10, 0.15, 0.25, 1.00, 2.00, 5.00, 10.00, 20.00, 50.00, 100.00]

    for value in money_values:
        counting_key[value] = 0

    for value in a_list:
        counting_key[value] += 1

    sorted_list = []
    for value in counting_key:
        counter = counting_key[value]

        while counter > 0:
            sorted_list.append(value)
            counter -= 1

    return sorted_list


file_in = open('lotsOfMoney.txt')
money_list = []
for line in file_in:
    money_list.append(float(line.strip()))

money_list = money_counting_sort(money_list)
print(money_list)
