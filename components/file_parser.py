from . import person as p


class FileParser:
    delimiterDictionary = {}

    def __init__(self):
        self.delimiter = None
        self.delimiterDictionary[","] = {}
        self.delimiterDictionary["|"] = {}
        # space is added last because there are spaces in comma, and pipe txt files
        self.delimiterDictionary[" "] = {}

        self.delimiterDictionary[","]["FirstName"] = 1
        self.delimiterDictionary[","]["LastName"] = 0
        self.delimiterDictionary[","]["MiddleInitial"] = -1
        self.delimiterDictionary[","]["Gender"] = 2
        self.delimiterDictionary[","]["FavoriteColor"] = 3
        self.delimiterDictionary[","]["DateOfBirth"] = 4

        self.delimiterDictionary["|"]["FirstName"] = 1
        self.delimiterDictionary["|"]["LastName"] = 0
        self.delimiterDictionary["|"]["MiddleInitial"] = 2
        self.delimiterDictionary["|"]["Gender"] = 3
        self.delimiterDictionary["|"]["FavoriteColor"] = 4
        self.delimiterDictionary["|"]["DateOfBirth"] = 5

        self.delimiterDictionary[" "]["FirstName"] = 1
        self.delimiterDictionary[" "]["LastName"] = 0
        self.delimiterDictionary[" "]["MiddleInitial"] = 2
        self.delimiterDictionary[" "]["Gender"] = 3
        self.delimiterDictionary[" "]["FavoriteColor"] = 5
        self.delimiterDictionary[" "]["DateOfBirth"] = 4

    def parse(self, filename):

        people = []
        appender = people.append
        # read file
        with open(filename, "r") as file:
            # get first line and auto-detect delimiter
            line = file.readline()
            # find what delimiter is in use
            for k in self.delimiterDictionary:
                if k in line:
                    self.delimiter = k
                    break

            # if none of our delimiters are found in the line then throw an exception
            if self.delimiter is None:
                raise Exception("No recognized delimiter found.")

            # get delimiter dictionary to get the index of each column
            parser = self.delimiterDictionary[self.delimiter]

            # for each line in file, parse line and create class and store in collection
            while line:
                # parse data in current line
                person = self.parseLine(line, parser)

                # add person to collection if not null
                if person is not None:
                    appender(person)

                line = file.readline()

        return people

    def parseLine(self, line, parser):
        def _getColumn(data, dictionary, key):
            index = dictionary[key]

            if index > -1:
                return data[index].strip()
            return None

        try:
            # split line by delimiter into array of strings
            data = line.split(self.delimiter)

            # create and populate person class with data from line

            person = p.Person(_getColumn(data, parser, "LastName"),
                              _getColumn(data, parser, "FirstName"),
                              _getColumn(data, parser, "MiddleInitial"),
                              _getColumn(data, parser, "Gender"),
                              _getColumn(data, parser, "FavoriteColor"),
                              _getColumn(data, parser, "DateOfBirth"))

            # return created person
            return person
        except Exception as e:
            # print error message and return null
            print(e)
            return None
