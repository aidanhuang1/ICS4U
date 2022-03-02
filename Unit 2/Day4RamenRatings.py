#Ramen Ratings solution

import csv

def get_current_ramen(line):
    if line['Stars'] != 'Unrated':
        line = [line['Brand'], line['Variety'], float(line['Stars'])]