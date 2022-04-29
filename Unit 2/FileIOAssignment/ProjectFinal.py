# Grade 12 Computer Science File I/O Assignment
# Aidan Huang
# Tuesday, March 22, 2022

# Data Structure:
# {'country'} : {year} : [GDP, Gold, Silver, Bronze]

import csv

def read_country_names():

    country_code_to_name = {}

    with open('noc_regions.csv', 'r', encoding='utf-8', errors='ignore') as file_in:

        reader = csv.DictReader(file_in)

        for line in reader:
            country_code = line['NOC']
            country_name = line['region']

            if country_code not in country_code_to_name:
                country_code_to_name[country_code] = country_name

    return country_code_to_name


def read_athelete_events(country_code_to_name):

    main_dict = {}

    with open('athlete_events.csv', 'r', encoding='utf-8', errors='ignore') as file_in:

        reader = csv.DictReader(file_in)

        for line in reader:
            year = int(line['Year'])
            medal = line['Medal']
            country_code = line['NOC']

            if year >= 1960:
                country_name = country_code_to_name[country_code]

                if country_name not in main_dict:
                    main_dict[country_name] = {}

                if year not in main_dict[country_name]:
                    main_dict[country_name][year] = [-1, 0, 0, 0]  # gdp, # of gold medals, # of silver medals, # of bronze medals


                if medal == 'Gold':
                    main_dict[country_name][year][1] = main_dict[country_name][year][1] + 1

                elif medal == 'Silver':
                    main_dict[country_name][year][2] = main_dict[country_name][year][2] + 1

                elif medal == 'Bronze':
                    main_dict[country_name][year][3] = main_dict[country_name][year][3] + 1

    return main_dict


def read_gdp(main_dict):
    with open('gdp_1960_2020.csv', 'r', encoding='utf-8', errors='ignore') as file_in:

        reader = csv.DictReader(file_in)

        for line in reader:
            year = int(line['year'])
            country_name = line['country']
            gdp = int(line['gdp'])

            if country_name in main_dict:
                if year in main_dict[country_name]:
                    main_dict[country_name][year][0] = gdp


def print_noc_regions(nocregions):
    print("\n\n----- Printing Country Codes -----\nCountry Code -> Country Name\n")

    for key in nocregions:
        print(f'{key} -> {nocregions[key]}')

    print('\n')


def print_main_dict(main_dict):
    print('\n\nMAIN DICTIONARY')

    for country_name in sorted(main_dict): # alphabetical order

        print(f'\n---------------- {country_name:>5} ----------------\n')

        for year in sorted(main_dict[country_name]): # numerical order

            print(f'Olympic Game Year: {year}'
                  f'\nGDP: {main_dict[country_name][year][0]}'
                  f'\nGold: {main_dict[country_name][year][1]}, Silver: {main_dict[country_name][year][2]}, '
                  f'Bronze: {main_dict[country_name][year][3]}\n')

    print(f'\n{main_dict}')


# Main --
country_code_to_name = read_country_names()

main_dict = read_athelete_events(country_code_to_name)

read_gdp(main_dict)

print_noc_regions(country_code_to_name) # prints the supporting dictionary; converting country codes to country names

print_main_dict(main_dict) # prints the main dictionary

