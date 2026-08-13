from StudentManager import StudentManager
from utils import get_valid_age, get_valid_marks,get_non_empty_input
from Student import Student
manager = StudentManager()
from file_handler import save_students
def display_menu():
    print("========== Student Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7.Save and Exit")


def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= 7:
                return choice
            print("Please enter a choice between 1 and 7.")
        except ValueError:
            print("Please enter a valid integer.")
def get_student(manager):
    while True:
        id = input("Enter Student id:")
        if manager.find_student_by_id(id) is None:
            break
        print("The id exists already. Please enter a new id.")
    name = get_non_empty_input("Enter student name: ", "Name")
    age = get_valid_age("Enter student age: ")
    course = get_non_empty_input("Enter student course: ", "Course")
    marks = get_valid_marks("Enter student marks: ")
    student=Student(id,name,age,course,marks)
    return student
def get_valid_age(message):
    while True:
        try:
            age = int(input(message))
            if age > 0:
                return age
            print("Enter a positive age.")
        except ValueError:
            print("Please enter a valid integer.")
def get_valid_marks(message):
    while True:
        try:
            marks = int(input(message))
            if 0 <= marks <= 100:
                return marks
            print("Please enter marks between 0 and 100.")
        except ValueError:
            print("Please enter a valid integer.")
def get_student_id():
    search_id=input("Enter student id: ")
    return search_id


while(True):
    display_menu()
    choice=get_user_choice()
    if  choice == 1:
        student=get_student(manager)
        manager.add_student(student)         
    elif choice == 2:
        manager.view_students()
    elif choice == 3:
        student_id=get_student_id()  
        manager.search_student(student_id)
    elif choice == 4:
        student_id=get_student_id()    
        manager.update_student(student_id)
    elif choice == 5:
        student_id=get_student_id()       
        manager.delete_student(student_id)
    elif choice == 6:
        save_students(manager.students)
        print("The student data is saved in system")
    elif choice ==7:
        save_students(manager.students)
        print("Students saved successfully.")
        print("Thank you for using Student Management System.")
        break