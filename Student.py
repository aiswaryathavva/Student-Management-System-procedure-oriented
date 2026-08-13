class Student:
    def __init__(self, id, name, age, course, marks):
        self.id = id
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def display(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")
        print(f"Marks: {self.marks}")