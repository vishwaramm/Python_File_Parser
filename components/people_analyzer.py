from . import file_parser as fp
import operator
import datetime


class PeopleAnalyzer:
    def sortByGender(self, people):
        def sortGender(person):
            return person.getGenderString()

        sortedPeople = people.copy()

        sortedPeople.sort(key=operator.attrgetter("lastName"))
        sortedPeople = sorted(sortedPeople, key=sortGender)

        return sortedPeople

    def sortByDateOfBirth(self, people):
        def sortDateTime(person):
            items = person.dateOfBirth.split('/')

            if len(items) == 1:
                items = person.dateOfBirth.split('-')

            if len(items) < 3:
                raise Exception(
                    "Cannot parse date {0}".format(person.dateOdBirth))

            return datetime.datetime(int(items[2]), int(items[0]), int(items[1]))

        sortedPeople = people.copy()

        sortedPeople.sort(key=operator.attrgetter("lastName"))
        sortedPeople = sorted(sortedPeople, key=sortDateTime)
        return sortedPeople

    def sortByLastNameDescending(self, people):
        sortedPeople = people.copy()

        sortedPeople.sort(key=operator.attrgetter("lastName"), reverse=True)
        return sortedPeople
