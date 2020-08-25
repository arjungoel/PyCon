class Employee(object):
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    @property
    def name(self):
        return self._name

    @property
    def designation(self):
        return self._designation

    @name.setter
    def name(self, value):
        self._name = value.capitalize()

    @designation.setter
    def designation(self, value):
        self._designation = value.capitalize()


emp = Employee('matt', 'engineer')
print(emp.name + ' ' + 'is having the position of' + ' ' + emp.designation)
