import student_class
import address_class
import courses_enum

from student_class import *

student_dict = {}
def add_student(name, age, course, zip, city, username):

    course = course.title()
    address = address_class.Address(zip, city)

    if username not in student_dict:
        if course in courses_enum.Courses:
            course = course.upper().replace(" ", "")
            student_info = student_class.Student(name, age, courses_enum.Courses[course], address)
            student_dict[username] = student_info.student_info()
            return student_dict[username]

    return None

def display_student_record(username):
    if username in student_dict:
        return student_dict[username]
    return None

def display_student_courses(username):

    if username in student_dict:
        course_string = ""

        for index, courses in enumerate(student_dict[username]["course"]):
            if index > 0:
                course_string += ", "
            course_string += courses

        return course_string

    return None

def add_new_course(username, course):

    course = course.upper().replace(" ", "")
    course = courses_enum.Courses[course].value

    if username in student_dict and course not in student_dict[username]["course"]:
            student_dict[username]["course"].add(course)
            return student_dict[username]

    return None

def update_student_course(username, course_to_be_updated, new_course):

    course = course_to_be_updated.upper().replace(" ", "")
    course = courses_enum.Courses[course].value
    new_course = new_course.upper().replace(" ", "")
    if new_course != "":
        new_course = courses_enum.Courses[new_course].value

    if username in student_dict:
        if course in student_dict[username]["course"]:
            student_dict[username]["course"].remove(course)
            if new_course in student_dict[username]["course"]:
                return None
            if new_course != "":
                student_dict[username]["course"].add(new_course)
            return student_dict[username]

        return None

    return None

def display_student_zip(username):
    if username in student_dict:
        return student_dict[username]["address"]["zip_code"]
    return None

def display_student_city (username):
    if username in student_dict:
        return student_dict[username]["address"]["city"]
    return None

def number_of_students():
    return len(student_dict)

def update_student_record(username, field_to_update, new_value):
    field_to_update = field_to_update.lower()
    if username in student_dict:
        if field_to_update in student_dict[username]:
            student_dict[username][field_to_update] = new_value

        if field_to_update == "city" or field_to_update == "zip_code":
            student_dict[username]["address"][field_to_update] = new_value

        return student_dict[username]
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
