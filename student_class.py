from enum import Enum

class Courses(Enum):
    MATH = "Math"
    PHYSICS = "Physics"
    COMPUTERSCIENCE = "Computer Science"
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    STATISTICS = "Statistics"
    ENGLISH = "English"
    ECONOMICS = "Economics"
    HISTORY = "History"
    PHILOSOPHY = "Philosophy"
    SOCIOLOGY = "Sociology"
    POLITICALSCIENCE = "Political Science"
    GEOGRAPHY = "Geography"
    PSYCHOLOGY = "Psychology"
    ART = "Art"
    MUSIC = "Music"
    ENGINEERING = "Engineering"
    LAW = "Law"
    MEDICINE = "Medicine"
    BUSINESS = "Business"

class Student:
    def __init__(self, name, age, course, address):
        self.name = name
        self.age = age
        self.course = course
        self.address = address

    def student_info(self):
        return {
            "name": self.name,
            "age": self.age,
            "course": {self.course.value},
            "address": self.address.address_info()
        }


class Address:
    def __init__(self, zip_code, city):
        self.zip_code = zip_code
        self.city = city

    def address_info(self):
        return {
            "zip_code": self.zip_code,
            "city": self.city
        }