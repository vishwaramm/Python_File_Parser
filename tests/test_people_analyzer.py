import unittest
from pathlib import Path
from . import file_generator as fg
from components import person
from components import people_analyzer


class TestPeopleAnalyzer(unittest.TestCase):

    def test_sortByGender(self):
        people = _getPeople()
        analyzer = people_analyzer.PeopleAnalyzer()
        sortedList = analyzer.sortByGender(people)

        self.assertIsNotNone(sortedList)
        self.assertEqual(len(sortedList), len(people))
        self.assertTrue(sortedList[0].firstName == "Melissa")
        self.assertTrue(sortedList[1].firstName == "Mary")
        self.assertTrue(sortedList[2].firstName == "David")
        self.assertTrue(sortedList[3].firstName == "Frank")

    def test_sortByDateOfBirth(self):
        people = _getPeople()
        analyzer = people_analyzer.PeopleAnalyzer()
        sortedList = analyzer.sortByDateOfBirth(people)

        self.assertIsNotNone(sortedList)
        self.assertEqual(len(sortedList), len(people))
        self.assertTrue(sortedList[0].firstName == "David")
        self.assertTrue(sortedList[1].firstName == "Frank")
        self.assertTrue(sortedList[2].firstName == "Mary")
        self.assertTrue(sortedList[3].firstName == "Melissa")

    def test_sortByLastNameDescending(self):
        people = _getPeople()
        analyzer = people_analyzer.PeopleAnalyzer()
        sortedList = analyzer.sortByLastNameDescending(people)

        self.assertIsNotNone(sortedList)
        self.assertEqual(len(sortedList), len(people))
        self.assertTrue(sortedList[0].firstName == "Frank")
        self.assertTrue(sortedList[1].firstName == "Mary")
        self.assertTrue(sortedList[2].firstName == "Melissa")
        self.assertTrue(sortedList[3].firstName == "David")


def _getPeople():
    people = []

    p1 = person.Person("Manson", "Mary", "A", "Female", "Green", "2/4/1976")
    people.append(p1)

    p2 = person.Person("Lewis", "Melissa", "H", "Female", "Red", "2/2/1988")
    people.append(p2)

    p3 = person.Person("Danielson", "David", "V", "Male", "Blue", "6/5/1948")
    people.append(p3)

    p4 = person.Person("Trigg", "Frank", "", "Male", "Orange", "4/3/1967")
    people.append(p4)

    return people
