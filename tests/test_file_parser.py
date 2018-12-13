import unittest
from pathlib import Path
from . import file_generator as fg
from components import file_parser as fp
#from .context import components


class TestFileParser(unittest.TestCase):

    def setUp(self):
        self.path = Path("input")
        self.csv50Filename = self.path / "csv_50.txt"
        self.pipe50Filename = self.path / "pipe_50.txt"
        self.space50Filename = self.path / "space_50.txt"

        generator = fg.FileGenerator()

        if self.csv50Filename.is_file() == False:
            generator.generate(self.csv50Filename, 50, ",")

        if self.pipe50Filename.is_file() == False:
            generator.generate(self.pipe50Filename, 50, "|")

        if self.space50Filename.is_file() == False:
            generator.generate(self.space50Filename, 50, " ")

    def test_Parse_Csv(self):
        parser = fp.FileParser()
        people = parser.parse(self.csv50Filename)

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 50)

    def test_Parse_Psv(self):
        parser = fp.FileParser()
        people = parser.parse(self.pipe50Filename)

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 50)

    def test_Parse_Ssv(self):
        parser = fp.FileParser()
        people = parser.parse(self.space50Filename)

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 50)

    def test_Parse_Bad_Input_Csv(self):
        parser = fp.FileParser()
        people = parser.parse(self.path / "comma_bad_input.txt")

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 2)

    def test_Parse_Bad_Input_Ssv(self):
        parser = fp.FileParser()
        people = parser.parse(self.path / "space_bad_input.txt")

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 2)

    def test_Parse_Bad_Input_Psv(self):
        parser = fp.FileParser()
        people = parser.parse(self.path / "pipe_bad_input.txt")

        self.assertIsNotNone(people)
        self.assertEqual(len(people), 3)

    def test_ParseLine_CommaDelimited_Success(self):
        parser = fp.FileParser()
        line = "Abercrombie, Neil, Male, Tan, 2/13/1943"
        parser.delimiter = ','
        person = parser.parseLine(
            line, parser.delimiterDictionary[parser.delimiter])

        self.assertIsNotNone(person)
        self.assertEqual(person.lastName, "Abercrombie")
        self.assertEqual(person.firstName, "Neil")
        self.assertEqual(person.gender, "Male")
        self.assertEqual(person.favoriteColor, "Tan")
        self.assertEqual(person.dateOfBirth, "2/13/1943")
        self.assertIsNone(person.middleInitial)

    def test_ParseLine_PipeDelimited_Success(self):
        parser = fp.FileParser()
        line = "Smith | Steve | D | M | Red | 3-3-1985"
        parser.delimiter = '|'
        person = parser.parseLine(
            line, parser.delimiterDictionary[parser.delimiter])

        self.assertIsNotNone(person)
        self.assertEqual(person.lastName, "Smith")
        self.assertEqual(person.firstName, "Steve")
        self.assertEqual(person.gender, "M")
        self.assertEqual(person.favoriteColor, "Red")
        self.assertEqual(person.dateOfBirth, "3-3-1985")
        self.assertEqual(person.middleInitial, "D")

    def test_ParseLine_SpaceDelimited_Success(self):
        parser = fp.FileParser()
        line = "Kournikova Anna F F 6-3-1975 Red"
        parser.delimiter = ' '
        person = parser.parseLine(
            line, parser.delimiterDictionary[parser.delimiter])

        self.assertIsNotNone(person)
        self.assertEqual(person.lastName, "Kournikova")
        self.assertEqual(person.firstName, "Anna")
        self.assertEqual(person.gender, "F")
        self.assertEqual(person.favoriteColor, "Red")
        self.assertEqual(person.dateOfBirth, "6-3-1975")
        self.assertEqual(person.middleInitial, "F")


if __name__ == '__main__':
    unittest.main()
