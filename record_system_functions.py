import student_class
from student_class import *

dict = {}
def add_student(name, age, course, zip, city, username):

    course = course.title()
    address = Address(zip, city)

    if username not in dict:
        if course in Courses:
            course = course.upper().replace(" ", "")
            student_info = student_class.Student(name, age, Courses[course], address)
            dict[username] = student_info.student_info()
            return dict[username]

    return None

def display_student_record(username):
    if username in dict:
        return dict[username]
    return None

def display_student_courses(username):

    if username in dict:
        course_string = ""

        for index, courses in enumerate(dict[username]["course"]):
            if index > 0:
                course_string += ", "
            course_string += courses

        return course_string

    return None

def add_new_course(username, course):

    course = course.upper().replace(" ", "")
    course = Courses[course].value

    if username in dict and course not in dict[username]["course"]:
            dict[username]["course"].add(course)
            return dict[username]

    return None

def update_student_course(username, course_to_be_updated, new_course):

    course = course_to_be_updated.upper().replace(" ", "")
    course = Courses[course].value
    new_course = new_course.upper().replace(" ", "")
    new_course = Courses[new_course].value

    if username in dict:
        if course in dict[username]["course"]:
            dict[username]["course"].remove(course)
            if new_course in dict[username]["course"]:
                return None
            elif new_course != "":
                dict[username]["course"].add(new_course)
            return dict[username]

        return None

    return None

def display_student_zip(username):
    if username in dict:
        return dict[username]["address"]["zip_code"]
    return None

def display_student_city (username):
    if username in dict:
        return dict[username]["address"]["city"]
    return None

def number_of_students():
    return len(dict)

def update_student_record(username, field_to_update, new_value):
    field_to_update = field_to_update.lower()
    if username in dict:
        if field_to_update in dict[username]:
            dict[username][field_to_update] = new_value

        if field_to_update == "city" or field_to_update == "zip_code":
            dict[username]["address"][field_to_update] = new_value

        return dict[username]
    return None
#
# def is_valid_input(user_number):
#     if user_number.isdigit():
#         return int(user_number)
#     else:
#         return None

def is_valid_input(user_number):
    try:
        return int(user_number)
    except ValueError:
        return None
