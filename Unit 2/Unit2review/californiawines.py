californiaWines = {}
with open('winemag.txt') as file_in:
    file_in.readline()
    for entry in file_in:
        line = entry.split('\t')
        key = f'{line[7]} | {line[2]}'
        californiaWines[key] = line[4]