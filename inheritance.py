"""
Author: Dula Temesgen
program: inheritance.py

Multiple inheritance assignment
"""

from datetime import date


class Employee:
    def __init__(self, start_date, salary, last_name, first_name, address, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.address = address
        self.phone_number = phone_number
        self.start_date = start_date
        self.salary = salary

    def give_raise(self, new_salary):
        self.salary = new_salary

class Person:
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address

class Manager(Employee, Person):
    def __init__(self, department, start_date, salary, last_name, first_name, address, phone_number, direct_reports=[]):
        Employee.__init__(self, start_date, salary, last_name, first_name, address, phone_number)
        Person.__init__(self, last_name, first_name, address)
        self._department = department
        self._direct_reports = direct_reports

    def display_direct_reports(self):
        for x in self._direct_reports:
            print(x.display())

employee = Employee(date.today(), 40000, 'Hendrix', 'Skit', '170 Easeter rd', '515-500-9001')

manager = Manager('Compliance', date.today(), 40000, 'Temesgen', 'Dula', '425 Easter lake dr', '515-500-5000', [employee])
# Manager Display is being used
print(manager.display())  

manager.display_direct_reports()
manager.give_raise(42000)
# Manager display is being used
print(manager.display())  

del employee
del manager