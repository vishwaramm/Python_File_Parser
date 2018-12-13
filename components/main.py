from . import people_analyzer as pa
from . import file_parser as fp
from . import person
from pathlib import Path


def main():
    path = Path("input")
    csvFile = path / "comma.txt"
    pipeFile = path / "pipe.txt"
    spaceFile = path / "space.txt"

    parser = fp.FileParser()
    analyzer = pa.PeopleAnalyzer()
    people = parser.parse(csvFile)
    people.extend(parser.parse(pipeFile))
    people.extend(parser.parse(spaceFile))

    printOutputs(people, analyzer)


def printOutputs(people, analyzer):
    peopleByGender = analyzer.sortByGender(people)
    peopleByDob = analyzer.sortByDateOfBirth(people)
    peopleByLastNameDescending = analyzer.sortByLastNameDescending(people)

    printList(peopleByGender, "Output 1 by gender and last name:")
    printList(peopleByDob, "Output 2 by date of birth and last name:")
    printList(peopleByLastNameDescending, "Output 3 by last name descending:")
    print("")


def printList(people, header):
    print(header)

    if people == None:
        print("No people to print")
        return

    for p in people:
        gender = ""

        if p.gender == "M" or p.gender == "Male":
            gender = "Male"
        elif p.gender == "F" or p.gender == "Female":
            gender = "Female"

        print("{0} {1} {2} {3} {4}".format(p.lastName, p.firstName,
                                           gender, p.dateOfBirth.replace("-", "/"), p.favoriteColor))

    print("")


# execute main
if __name__ == '__main__':
    main()
