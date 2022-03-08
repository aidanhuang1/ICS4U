import csv

def create_colour_data(filename):
    
    colourDict = {}

    with open(filename) as fileIn:
        print(type(fileIn), fileIn)

        fileIn.readline()
        
        reader = csv.reader(fileIn)
        print(type(reader), reader)
        
        for line in reader:

            #create the dictionary entry #HEX : List of data
            colourData = [int(line[0]), line[1]]
            if line[3] == 'f':
                colourData.append(False)
            else:
                colourData.append(True)
                
            colourDict["#"+line[2]] = colourData

    return colourDict


def print_dict(some_dict):
    
    for key in some_dict:
        print(key, some_dict[key])



colour_dict = create_colour_data("colors.csv")
print_dict(colour_dict)
