students=[]
def display_menu():
    print("========== Student Management ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Students")
    print("7.Exit")
def add_student(student):
    students.append(student)
    print("Student added successfully.")
def view_students(students):
    if not students:
        print("No students found.")
    else:
        print("-"*25)
        for stu in students:
            print_student(stu)
            print()
            print("-"*25)
def search_student(student):    
    if student is not None:
            print("Student Found!!!")
            print_student(student)
    else:
        print("Student not Found!!!")
def update_student(student):
    if student is not None:
        print_student(student)
        student["name"]=input("Enter student new name:")
        student["age"]=int(input("Enter student new age:"))
        student["course"]=input("Enter student new course:")
        student["marks"]=int(input("Enter Student new marks:"))
        print("Student updated successfully.")
        print_student(student)
    else:
        print("Student not found.")
def delete_student(student):
    if student is not None:
        students.remove(student)
        print("The student is deleted successfully")
    else:
        print("Student not found.")
def save_student(students):
    with open('students.txt','w') as file:
        for student in students:
            line = ",".join(str(value) for value in student.values())
            file.write(line + "\n")
            # file.write(str(student)+"\n")
    print("Students saved successfully")
def get_user_choice():
    choice = int(input("Enter your choice: "))
    return choice
def get_student():
    student_details=dict()
    student_details["id"]=input("Enter Student id:")
    student_details["name"]=input("Enter student name:")
    student_details["age"]=int(input("Enter student age:"))
    student_details["course"]=input("Enter student course:")
    student_details["marks"]=int(input("Enter Student marks:"))
    return student_details
def get_student_id():
    search_id=input("Enter student id: ")
    return search_id

def print_student(student):
    print(f"ID     : {student['id']}")
    print(f"Name   : {student['name']}")
    print(f"Age    : {student['age']}")
    print(f"Course : {student['course']}")
    print(f"Marks  : {student['marks']}")
def find_student_by_id(students,student_id):
    for stu in students:
        if stu['id']==student_id:
            return stu
    
    return None
while(True):
    display_menu()
    choice=get_user_choice()
    if  choice == 1:
        student=get_student()
        add_student(student)    
    elif choice == 2:
        view_students(students)
    elif choice == 3:
        student_id=get_student_id()
        student=find_student_by_id(students,student_id)
        search_student(student)
    elif choice == 4:
        student_id=get_student_id()
        student=find_student_by_id(students,student_id)
        update_student(student)
    elif choice == 5:
        student_id=get_student_id()
        student=find_student_by_id(students,student_id)       
        delete_student(student)
    elif choice == 6:
        save_student(students)
        print("The student data is saved in system")
    elif choice ==7:
        print("Thank you for using Student Management System.")
        break