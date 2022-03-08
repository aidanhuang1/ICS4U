#Ramen Ratings solution

import csv

def get_current_ramen(line):
    if line['Stars'] != 'Unrated':
        line = [line['Brand'], line['Variety'], float(line['Stars'])]
    else:
        line = [line['Brand'], line['Variety'], line['Stars']]
    return line

def read_parse_ramen_data():
    ramen_dictionary = {}
    with open("ramen-ratings.csv") as fileIn:
        reader = csv.DictReader(fileIn)

        for line in reader:
            if line['Country'] not in ramen_dictionary: # if there is not already one for that country, create one
                ramen_dictionary[line['Country']] = {}

            if line['Style'] not in ramen_dictionary[line['Country']]:
                ramen_dictionary[line['Country']][line['Style']] = []
            current_ramen = get_current_ramen(line)
            ramen_dictionary[line['Country']][line['Style']].append(current_ramen)
    return ramen_dictionary

def print_ramen_dictionary_console(ramen_dictionary):
    for key in ramen_dictionary:
        print(f'\n\n{key.upper()}\n{"-"*len(key)}')
        for style in ramen_dictionary[key]:
            print(f'\n{style}: {len(ramen_dictionary[key][style])} entries')
            print(f'A selection of them are:\n {ramen_dictionary[key][style][:10]}')

def main():
    ramen_dictionary = read_parse_ramen_data()
    print_ramen_dictionary_console(ramen_dictionary)

main()