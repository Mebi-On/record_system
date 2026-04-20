from record_system_functions import *

dict = {}
dict.clear()
# CASE 5 & 8 UNDONE

def student_record_menu():
    continue_main_loop = True

    while continue_main_loop:
        print("""
    1. Add a Student
    2. Display Student Record
    3. Display Student Courses
    4. Add New Course to Student
    5. Update Student Course
    6. Display Student Zip Code
    7. Display Student City
    8. Update Student Record
    9. Show Number of Students
    10. Exit
    """, end="")

        main_menu_choice = input("Enter your choice: ")
        main_menu_choice = is_valid_input(main_menu_choice)

        if main_menu_choice is None:
            print("Error: Enter a valid number")

        else:
            match main_menu_choice:
                case 1:
                    prompt_user_to_add_student = True

                    while prompt_user_to_add_student:
                        name = input("Enter Student Name: ").strip()
                        age = input("Enter Student Age: ")
                        course = input("Enter Course (e.g., Math, English, Science): ").strip()
                        zip_code = input("Enter Zip Code: ")
                        city = input("Enter City: ").strip()
                        username = input("Enter Username: ").strip()

                        age_valid = is_valid_input(age)

                        if not name:
                            print("Error: Student name cannot be empty")
                        elif age_valid is None:
                            print("Error: Enter a valid age number")
                        elif not course:
                            print("Error: Course cannot be empty")
                        elif not zip_code:
                            print("Error: Zip code cannot be empty")
                        elif not city:
                            print("Error: City cannot be empty")
                        elif not username:
                            print("Error: Username cannot be empty")
                        else:
                            result = add_student(name, age_valid, course, zip_code, city, username)

                            if result is None:
                                print(f"Error: Username '{username}' already exists or course not found")
                            else:
                                print(f"Student '{username}' added successfully!")
                                prompt_user_to_add_student = False

                case 2:
                    prompt_user_to_display = True

                    while prompt_user_to_display:
                        username = input("Enter Username: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        else:
                            result = display_student_record(username)

                            if result is None:
                                print(f"Error: Student '{username}' not found")
                            else:
                                print(f"\nStudent Record for {username}:")
                                print(result)
                                prompt_user_to_display = False

                case 3:
                    prompt_user_to_show_courses = True

                    while prompt_user_to_show_courses:
                        username = input("Enter Username: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        else:
                            result = display_student_courses(username)

                            if result is None:
                                print(f"Error: Student '{username}' not found")
                            else:
                                print(f"Courses for {username}: {result}")
                                prompt_user_to_show_courses = False

                case 4:
                    prompt_user_to_add_course = True

                    while prompt_user_to_add_course:
                        username = input("Enter Username: ").strip()
                        course = input("Enter Course to add (e.g., Math, English, Science): ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        elif not course:
                            print("Error: Course cannot be empty")
                        else:
                            result = add_new_course(username, course)

                            if result is None:
                                print(f"Error: Student '{username}' not found or course already exists")
                            else:
                                print(f"Course '{course}' added successfully to {username}!")
                                print(f"Updated courses: {result['course']}")
                                prompt_user_to_add_course = False

                case 5:
                    prompt_user_to_update_course = True

                    while prompt_user_to_update_course:
                        username = input("Enter Username: ").strip()
                        old_course = input("Enter course to replace: ").strip()
                        new_course = input("Enter new course: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        elif not old_course:
                            print("Error: Old course cannot be empty")
                        elif not new_course:
                            print("Error: New course cannot be empty")
                        else:
                            result = update_student_course(username, old_course, new_course)

                            if result is None:
                                print(f"Error: Could not update course. Student not found or course not enrolled")
                            else:
                                print(f"Course updated successfully for {username}!")
                                print(f"Updated courses: {result['course']}")
                                prompt_user_to_update_course = False

                case 6:
                    prompt_user_to_get_zip = True

                    while prompt_user_to_get_zip:
                        username = input("Enter Username: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        else:
                            result = display_student_zip(username)

                            if result is None:
                                print(f"Error: Student '{username}' not found")
                            else:
                                print(f"Zip Code for {username}: {result}")
                                prompt_user_to_get_zip = False

                case 7:
                    prompt_user_to_get_city = True

                    while prompt_user_to_get_city:
                        username = input("Enter Username: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        else:
                            result = display_student_city(username)

                            if result is None:
                                print(f"Error: Student '{username}' not found")
                            else:
                                print(f"City for {username}: {result}")
                                prompt_user_to_get_city = False

                case 8:
                    prompt_user_to_update_record = True

                    while prompt_user_to_update_record:
                        username = input("Enter Username: ").strip()
                        field_to_update = input("Enter Field To Update: ").strip()
                        new_value = input("Enter New Value: ").strip()

                        if not username:
                            print("Error: Username cannot be empty")
                        elif not field_to_update:
                            print("Error: Field cannot be empty")
                        elif not new_value:
                            print("Error: New value cannot be empty")
                        else:
                            if field_to_update == "age":
                                new_value = is_valid_input(new_value)
                                if new_value is None:
                                    print("Error: Age must be a valid number")

                            result = update_student_record(username, field_to_update, new_value)

                            if result is None:
                                print(f"Error: Could not update record. Student not found or record already exists")
                            else:
                                print(f"{username} {field_to_update} successfully updated to {new_value}")
                                prompt_user_to_update_record = False

                case 9:
                    result = number_of_students()

                    if result == 0:
                        print("No students in the system yet")
                    print(f"There is {result} student in the system")


                case 10:
                    continue_main_loop = False
                    print("Exiting Student Record System. Goodbye!")

                case _:
                    print("Error: Enter a valid number between 1 and 10")


student_record_menu()