import csv
import glob

files = glob.glob('regional-ca*.csv')
allsongs = {}

for file in files:
    with open(file) as file_in:
        file_in.readline()
        reader = csv.DictReader(file_in)
        for line in reader:
            artist = line['Artist']
            streams = int(line['Streams'])
            trackname = line['Track Name']
            song_key = f'{trackname} by {artist}'
            # print(f'{artist} {streams} {trackname}')
            if song_key not in allsongs:
                allsongs[song_key] = {}
            allsongs[song_key][date] = streams

