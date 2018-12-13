
class Person:
    # allocate space for only these attributes so we don't need to create a __dict__ property in the class and we save space when parsing large files
    __slots__ = ["lastName", "firstName", "middleInitial",
                 "gender", "favoriteColor", "dateOfBirth"]

    def __init__(self, lastName, firstName, middleInitial, gender, favoriteColor, dateOfBirth):
        self.lastName = lastName
        self.firstName = firstName
        self.middleInitial = middleInitial
        self.gender = gender
        self.favoriteColor = favoriteColor
        self.dateOfBirth = dateOfBirth

    def getGenderString(self):
        if self.gender == "M" or self.gender == "Male":
            return "Male"
        elif self.gender == "F" or self.gender == "Female":
            return "Female"
