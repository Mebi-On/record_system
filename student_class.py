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

