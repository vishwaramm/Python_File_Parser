import random
import datetime


class FileGenerator:

    def __init__(self):
        self.initials = ['A', 'B', 'C', 'D', 'E', "F", 'G', 'H', 'I', 'J', 'K',
                         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.firstNames = [
            "Mark",
            "Eric",
            "Dan",
            "Russ",
            "Brad",
            "Audie",
            "Will",
            "Peter",
            "Paul",
            "Tim",
            "John",
            "Alex",
            "Abraham",
            "Mathew",
            "Luke",
            "Conor",
            "Dana",
            "Maria",
            "Mary",
            "Stephanie",
            "Debra",
            "Ashley",
            "Asha",
            "Megan",
            "Cindy",
            "Ryan",
            "Alexa",
            "Siri",
            "Brittney",
            "Vanessa",
            "Renessa",
            "Angella",
            "Derrick",
            "Louis",
            "Vince",
            "Roman",
            "Sal",
            "Brian",
            "James",
            "Joe",
            "Joseph",
            "Brandon",
            "Sean"
        ]

        self.lastNames = [
            "Coleman",
            "Lewis",
            "Smith",
            "Cardona",
            "Boone",
            "Johnson",
            "Williams",
            "Jones",
            "Brown",
            "Davis",
            "Miller",
            "Wilson",
            "Moore",
            "Taylor",
            "Anderson",
            "Thomas",
            "Jackson",
            "White",
            "Harris",
            "Martin",
            "Thompson",
            "Garcia",
            "Martinez",
            "Robinson",
            "Clark",
            "Lee",
            "Walker",
            "Hall",
            "Allen",
            "Young",
            "King",
            "Wright",
            "Hill",
            "Scott",
            "Green",
            "Adams",
            "Baker",
            "Nelson"
        ]

        self.colors = [
            "Red",
            "Orange",
            "Green",
            "Gray",
            "Orange",
            "Blue",
            "Purple",
            "Tan",
            "Baby Blue",
            "Indigo",
            "Yellow",
            "Brown",
            "Silver",
            "Gold",
            "Black"
        ]

        self.gender = [
            "Male",
            "Female"
        ]

    def generate(self, filename, entries, delimiter):
        with open(filename, "w+") as file:
            for _ in range(entries):
                line = self.newLine(delimiter)
                if line != "":
                    file.write(line)

    def newLine(self, delimiter):
        fNameIndex = random.randint(0, len(self.firstNames)-1)
        lNameIndex = random.randint(0, len(self.lastNames)-1)
        randomAge = random.randint(24, 110)
        randomGender = random.randint(0, len(self.gender)-1)
        randomCharacter = random.randint(0, len(self.initials)-1)
        colorIndex = random.randint(0, len(self.colors)-1)
        dateStr = (datetime.datetime.now(
        ) - datetime.timedelta(randomAge * 365.24)).strftime("%m/%d/%Y")

        line = ""

        if delimiter == '|':
            line = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}\n".format(
                delimiter, self.lastNames[lNameIndex], self.firstNames[fNameIndex], self.initials[randomCharacter], self.gender[randomGender], self.colors[colorIndex], dateStr)
        elif delimiter == ',':
            line = "{1}{0}{2}{0}{3}{0}{4}{0}{5}\n".format(
                delimiter, self.lastNames[lNameIndex], self.firstNames[fNameIndex], self.gender[randomGender], self.colors[colorIndex], dateStr)
        elif delimiter == ' ':
            line = "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}\n".format(
                delimiter, self.lastNames[lNameIndex], self.firstNames[fNameIndex], self.initials[randomCharacter], self.gender[randomGender], dateStr, self.colors[colorIndex])

        return line
