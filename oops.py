class Employee:
    def __int__(self, name, salary):
        self.name = name
        self.salary = salary

    def getSalary(self):
        return self.salary


rohan = Employee("pranita", 78888)
print(rohan.salary)
print(rohan.name)
