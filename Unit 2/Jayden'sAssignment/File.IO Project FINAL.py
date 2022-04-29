import csv

## NEWEST Data Structure -

## {riding} : {election_id} : {ballot_num} : ['Party',num_of_votes]

def read_candidates_file():

    main_dict = {}

    with open('Candidates.CSV', 'r', encoding='utf-8', errors='ignore') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            if line['election_id'] == 'GE.40.2008' or line['election_id'] == 'GE.41.2011' or line['election_id'] == 'GE.42.2015' or line['election_id'] == 'GE.43.2019':

                Election_ID = line['election_id']
                ballot_num = int(line['ballot_sequence_number'])
                riding = line['electoral_district_number']
                party = line['party_abbreviation_english_anglais']

                if riding not in main_dict:
                    main_dict[riding] = {}

                if Election_ID not in main_dict[riding]:
                    main_dict[riding][Election_ID] = {}

                if ballot_num not in main_dict[riding][Election_ID]:
                    main_dict[riding][Election_ID][ballot_num] = [party]

    return main_dict

def read_results_file(main_dict):

    with open('Results.CSV','r',encoding='utf-8', errors='ignore') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            if line['election_id'] == 'GE.40.2008' or line['election_id'] == 'GE.41.2011' or line['election_id'] == 'GE.42.2015' or line['election_id'] == 'GE.43.2019':

                Election_ID = line['election_id']
                riding = line['electoral_district_number']
                ballot_num = int(line['ballot_sequence_number'])
                num_of_votes = int(line['candidate_poll_votes_count'])

                if num_of_votes != 0:

                    main_dict[riding][Election_ID][ballot_num].append(num_of_votes)

                else:
                    continue

    return main_dict

def read_ridings_file():

    riding_lookup = {}

    with open('Ridings.CSV','r',encoding='utf-8', errors='ignore') as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:

            if line['redistribution_boundaries'] == '2005':

                riding_code = line['electoral_district_number']
                riding_name = line['electoral_district_name_english_anglais']

                if riding_code not in riding_lookup:
                    riding_lookup[riding_code] = ''

                riding_lookup[riding_code] = riding_name

    return riding_lookup

def printing_riding_lookup(riding_lookup):

    print('\nThis is my Riding lookup Dictionary: \n')
    for riding_code in riding_lookup:
        print(riding_code)

        print(riding_lookup[riding_code])

def printing_main_dict(main_dict):

    print('\nThis is my main Dictionary: \n')

    for riding in main_dict:
        print(riding)

        for election_id in main_dict[riding]:
            print(election_id)

            for ballot_num in main_dict[riding][election_id]:
                print(ballot_num)

                print(main_dict[riding][election_id][ballot_num][0:])

# MAIN - Calling Functions

main_dict = read_candidates_file()

read_results_file(main_dict)

riding_lookup = read_ridings_file()

printing_riding_lookup(riding_lookup) #prints the riding look up dictionary

printing_main_dict(main_dict) #prints the actual
