import unittest
from record_system_functions import *


class TestRecordSystemFunction(unittest.TestCase):
    dict = {}

    def setUp(self):
        student_dict.clear()

    def test_add_new_student_to_dictionary(self):
        actual = add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        expected = {
            "name" : "John Doe",
            "age" : 23,
            "course" : {"Math"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}}
        self.assertEqual(actual, expected)
        self.assertIn("johnDoe1", student_dict)

    def test_add_new_student_to_dictionary_with_already_existing_username(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = {add_student("John Mae", 23, "English", 112, "Lagos", "johnDoe1")}
        expected = {None}
        self.assertEqual(actual, expected)

    def test_add_new_student_to_dictionary_with_nonexistent_course(self):
        actual = {add_student("John Mae", 23, "French", 112, "Lagos", "johnDoe1")}
        expected = {None}
        self.assertEqual(actual, expected)

    def test_display_student_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = display_student_record("johnDoe1")
        expected = {
            "name" : "John Doe",
            "age" : 23,
            "course" : {"Math"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}}
        self.assertEqual(actual, expected)
        self.assertIn("johnDoe1", student_dict)

    def test_display_student_record_of_nonexistent_student(self):
        actual = display_student_record("johnDoe1")
        expected = None
        self.assertEqual(actual, expected)
        self.assertTrue(len(student_dict) == 0)

    def test_add_new_course_to_student_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = add_new_course("johnDoe1", "english")
        expected = {
            "name" : "John Doe",
            "age" : 23,
            "course" : {"Math", "English"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)

    def test_add_new_course_to_student_record_with_already_existing_course(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = add_new_course("johnDoe1", "math")
        expected = None
        self.assertEqual(actual, expected)

    def test_add_new_course_to_student_record_with_nonexistent_username(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = add_new_course("johnDoe2", "English")
        expected = None
        self.assertEqual(actual, expected)

    def test_update_course_on_student_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = update_student_course("johnDoe1", "math", "english")
        expected = {
            "name" : "John Doe",
            "age" : 23,
            "course" : {"English"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)

    def test_update_course_on_student_record_with_already_existing_course(self):
        add_student("John Doe", 23, "English", 112, "Lagos", "johnDoe1")
        add_new_course("johnDoe1", "Math")
        actual = update_student_course("johnDoe1", "Math", "English")
        expected = None
        self.assertEqual(actual, expected)

    def test_delete__coursse_with_update_course_functione(self):
        add_student("John Doe", 23, "English", 112, "Lagos", "johnDoe1")
        add_new_course("johnDoe1", "Math")
        actual = update_student_course("johnDoe1", "Math", "")
        expected = {
            "name" : "John Doe",
            "age" : 23,
            "course" : {"English"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)

    def test_update_course_on_student_record_with_nonexistent_username(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        add_new_course("johnDoe1", "Math")
        actual = update_student_course("johnDoe2", "Math", "Biology")
        expected = None
        self.assertEqual(actual, expected)


    def test_display_student_zip(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = display_student_zip("johnDoe1")
        expected = 112
        self.assertEqual(actual, expected)

    def test_diaplay_student_zip_with_nonexistent_username(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = display_student_zip("johnDoe2")
        expected = None
        self.assertEqual(actual, expected)

    def test_display_student_city(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = display_student_city("johnDoe1")
        expected = "Lagos"
        self.assertEqual(actual, expected)

    def test_diaplay_student_city_with_nonexistent_username(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = display_student_city("johnDoe2")
        expected = None
        self.assertEqual(actual, expected)

    def test_number_of_students(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        add_student("Bruce", 24, "Math", 112, "Lagos", "bruceWayns")
        add_student("Jack", 17, "Math", 112, "Lagos", "JackBlvck")
        actual = number_of_students()
        expected = 3
        self.assertEqual(actual, expected)

    def test_number_of_students_with_empty_records(self):
        actual = number_of_students()
        expected = 0
        self.assertEqual(actual, expected)

    def test_update_student_age_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = update_student_record("johnDoe1", "age", 24)
        expected = {
            "name" : "John Doe",
            "age" : 24,
            "course" : {"Math"},
            "address" : {'zip_code': 112, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)

    def test_update_student_name_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = update_student_record("johnDoe1", "name", "Jane Doe")
        expected = {
            "name": "Jane Doe",
            "age": 23,
            "course": {"Math"},
            "address": {'zip_code': 112, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)

    def test_update_student_city_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = update_student_record("johnDoe1", "city", "Abuja")
        expected = {
            "name": "John Doe",
            "age": 23,
            "course": {"Math"},
            "address": {'zip_code': 112, 'city': 'Abuja'}
        }
        self.assertEqual(actual, expected)

    def test_update_student_zip_record(self):
        add_student("John Doe", 23, "Math", 112, "Lagos", "johnDoe1")
        actual = update_student_record("johnDoe1", "zip_code", 10001)
        expected = {
            "name": "John Doe",
            "age": 23,
            "course": {"Math"},
            "address": {'zip_code': 10001, 'city': 'Lagos'}
        }
        self.assertEqual(actual, expected)
