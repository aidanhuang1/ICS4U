import csv


def read_nba_without_csv_module():
    with open("NBAEasternConference.csv", "r") as fileIn:
        # ignoring the first two lines
        fileIn.readline()
        fileIn.readline()

        for line in fileIn:
            line = line.split(",")
            print(len(line), line)


def read_nba_with_csv_module():
    with open("NBAEasternConference.csv", "r") as fileIn:
        fileIn.readline()
        fileIn.readline()

        reader = csv.reader(fileIn)

        for line in reader:
            print(len(line), line)


read_nba_without_csv_module()
print("\n\n")
read_nba_with_csv_module()
