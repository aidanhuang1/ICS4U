import csv


def generate_country_ratings(country_dictionary):
    country_ratings = {}

    for key in country_dictionary:

        country_average = 0

        for chocolate in country_dictionary[key]:
            country_average += chocolate[3]

        country_average /= len(country_dictionary[key])

        country_ratings[key] = country_average

    return country_ratings


def print_country_ratings(rating_dict):
    for key in sorted(rating_dict):
        average = rating_dict[key]
        print(f'{key:>20} as an average rating of {average:>3.1f}')


# This time we are using a dictionary reader, instead of the csv.reader
def read_parse_chocolate_data(filename):
    country_rating_dictionary = {}

    with open(filename) as fileIn:

        reader = csv.DictReader(fileIn)

        for line in reader:
            ##            print(line, "\n")

            beanEntry = [line['bean_origin'], int(line['review_date']), float(line['cocoa_percent'][:-1]),
                         float(line['rating'])]

            if line['country'] not in country_rating_dictionary:
                country_rating_dictionary[line['country']] = []

            country_rating_dictionary[line['country']].append(beanEntry)

    return country_rating_dictionary


def main():
    country_dictionary = read_parse_chocolate_data("flavors_of_cacao.csv")

    ##    print("First 10 entries for each country")
    ##    for country in country_dictionary:
    ##        print(country)
    ##        print(country_dictionary[country][:10])

    generate_country_ratings(country_dictionary)

    # potential application data set
    country_rating_dictionary = generate_country_ratings(country_dictionary)
    print_country_ratings(country_rating_dictionary)


main()
