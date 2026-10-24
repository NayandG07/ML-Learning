class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")

s1 = Student("John", 101)
s1.display()