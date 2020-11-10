"""
Author: Dula Temesgen
program: Class composition assignment

Date: 11/10/2020
"""
from datetime import today


class Person:
    def __init__(self, person_id, last_name, first_name, phone_number, address):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address


class Student:
    def __init__(self, person, gpa, major, start_date):
        self.person = person
        self.gpa = gpa
        self.major = major
        self.start_date = start_date

    def change_major(self, value):
        self.major = value

    def change_gpa(self, value):
        self.gpa = value

    def display(self):
        print(f'First name: {self.person.first_name}, \nLast Name: {self.person.last_name}, \nPhone number: {self.person.phone_number} \nAddress: {self.person.address} \nGPA is: {self.gpa} \nMajor is: {self.major}')


person = Person(1, 'Dula', 'Temesgen', '515-000-2000', '2745 Easter springs RD,. Des Moines Iowa 50454')

student = Student(person, 4.0, 'comSci', datetime.today())

student.change_gpa(1.0)
student.change_major('Math')
student.display()
del person
del student
