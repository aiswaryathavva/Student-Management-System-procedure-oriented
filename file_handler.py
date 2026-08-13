from Student import Student
def load_students():
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                line = line.strip()
                id, name, age, course, marks = line.split(",")
                age = int(age)
                marks = int(marks)
                student = Student(id, name, age, course, marks)
                students.append(student)

        return students

    except FileNotFoundError:
        print("students.txt not found. Starting with an empty student list.")
        return []
def save_students(students):
    with open('students.txt','w') as file:
        for student in students:
            line = ",".join([
str(student.id),
str(student.name),
str(student.age),
str(student.course),
str(student.marks)
])
            file.write(line + "\n")
        
    print("Students saved successfully")