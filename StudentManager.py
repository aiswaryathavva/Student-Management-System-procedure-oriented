from file_handler import load_students
from utils import get_valid_age, get_valid_marks,get_non_empty_input
class StudentManager:
    def __init__(self):
        self.students=load_students()
    def add_student(self, student):
        if self.find_student_by_id(student.id) is not None:
            print("A student already exists with this ID. Please enter a valid ID.")
        else:
            self.students.append(student)
            print("Student added successfully.")
    def find_student_by_id(self,student_id):
        for student in self.students:
            if student.id==student_id:
                return student
        return None
    def view_students(self):
        if not self.students:
            print("No students found.")
        else:
            print("-"*25)
            for student in self.students:
                student.display()
                print()
            print("-"*25)
    def search_student(self,student_id): 
        found_stu=self.find_student_by_id(student_id)
        if found_stu is not None:
            print("Student Found!!!")
            found_stu.display()
        else:
            print("Student not Found!!!")
    def update_student(self,student_id):
        student=self.find_student_by_id(student_id)
        if student is not None:
            student.display()
            new_name = get_non_empty_input("Enter student new name: ", "Name")
            new_age = get_valid_age("Enter your new age: ")
            new_course = get_non_empty_input("Enter student new course: ", "Course")
            new_marks = get_valid_marks("Enter your new marks: ")
            student.name=new_name
            student.age=new_age
            student.course=new_course
            student.marks=new_marks
            
            student.display()
        else:
            print("Student not found.")
    def delete_student(self,student_id):
        student=self.find_student_by_id(student_id)
        if student is not None:
            self.students.remove(student)
            print("The student is deleted successfully")
        else:
            print("Student not found.")
