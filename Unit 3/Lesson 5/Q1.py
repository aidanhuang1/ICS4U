

def Q1(list):
    spread = max(list) - min(list)
    offset_value = min(list)

    key = []
    for i in range(0, spread+1):
        key.append(0)

    for element in list:
        key[element-offset_value] += 1

    sorted_list = []
    for i in range(len(key)):
        counter = key[i]
        while counter > 0:
            value = i + offset_value
            sorted_list.append(value)
            counter -= 1

    return sorted_list


l = [600,601,602,603,641,601]
print(Q1(l))