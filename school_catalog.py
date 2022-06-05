class School:
    def __init__(self, name, level, numberOfStudents) -> None:
        self._name = name
        self._level = level
        self._numberOfStudents = numberOfStudents

    def get_name(self):
        return self._name

    def get_level(self):
        return self._level

    def get_numberOfStudents(self):
        return self._numberOfStudents

    def set_numberOfStudents(self, value):
        self._numberOfStudents = value

    def __repr__(self) -> str:
        return f'School Name: {self.get_name().upper()} {self.get_level().upper()} SCHOOL \nNumber of students: {self.get_numberOfStudents()}'


class PrimarySchool(School):

    def __init__(self, name, numberOfStudents, pickup_policy) -> None:
        super().__init__(name, 'primary', numberOfStudents)
        self._pickup_policy = pickup_policy

    def get_pickup_policy(self):
        return self._pickup_policy

    def __repr__(self) -> str:
        parent_repr = super().__repr__()
        return parent_repr + f'\nThe pickup policy is: {self.get_pickup_policy()}'


class MiddleSchool(School):
    pass


class HighSchool(School):

    def __init__(self, name, numberOfStudents, sports_teams) -> None:
        super().__init__(name, 'high', numberOfStudents)
        self._sports_teams = sports_teams

    def get_sports_teams(self):
        return self._sports_teams

    def __repr__(self) -> str:
        parent_repr = super().__repr__()
        return parent_repr + f'\nThe sports teams are: {self.get_sports_teams()}'


garfield = School('Garfield', 'High', '1150')
print(garfield)

testSchool = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(testSchool.get_pickup_policy())
print(testSchool)

c = HighSchool("Codecademy High", 500, ["Tennis", "Basketball"])
print(c.get_sports_teams())
print(c)
