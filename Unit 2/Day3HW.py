with open('universityPrograms.txt') as file_in:
    finallist = []
    for file in file_in:
        file = file.strip()
        s = file.split(",")

        # <-- Getting the first program separately because it has the province -->
        universities = []
        # Getting just the university name
        university = s[0].split(" ")
        result = ""
        for word in university:
            if word != "University" and word != "of":
                result += word + " "
        universities.append(result.strip())

        universities.append(s[1].strip())  # appending the city

        # appending the province
        firstprogram = s[2].split(":")
        universities.append(firstprogram[0].strip())
        universities.append(firstprogram[1].strip())
        finallist.append(universities)
        # <!-- -->

        for program in s[3:]:
            universities = []
            # Getting just the university name
            university = s[0].split(" ")
            result = ""
            for word in university:
                if word != "University" and word != "of":
                    result += word + " "
            universities.append(result.strip())

            universities.append(s[1].strip())  # appending the city

            # appending the province
            firstprogram = s[2].split(":")
            universities.append(firstprogram[0].strip())

            universities.append(program.strip())
            finallist.append(universities)

    for element in finallist:
        print(element)
