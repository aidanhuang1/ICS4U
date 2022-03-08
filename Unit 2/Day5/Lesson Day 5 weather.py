import glob
import csv

def find_current_month(filename):

    index = filename.find(",")
    print(index)
    if index == 31:
        return int(filename[30])
    else:
        return int(filename[30:32])

    
def convert_month_temp(value):
    if value != "":
        value = float(value)
    else:
        value = None
    return value

   
def read_parse_station_data(all_file_pointers):
    all_stations = {}

    for filename in all_file_pointers:
        current_month = find_current_month(filename)

        with open(filename) as file_in:
            for i in range(0, 32):
                file_in.readline()

            reader = csv.reader(file_in)

            for line in reader:

                station_id = line[24]
                month_temp = convert_month_temp(line[4])
                
                if (station_id not in all_stations):
                    all_stations[station_id] = {}
                all_stations[station_id][current_month] = month_temp

    return all_stations


def main():
    #use glob to generate the filenames
    file_pointers = glob.glob('eng*.csv') # file name starts with eng and ends with .csv
    all_stations = read_parse_station_data(file_pointers)

    #print to visually verify dictionary of stations is created.
    for key in all_stations:
        print(key, all_stations[key])
    

main()
