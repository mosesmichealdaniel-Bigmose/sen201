
from student import Student

class Storage:
    def __init__(self):
        self.filename = "students.txt"

    def add_student(self, student):
        with open(self.filename, "a") as file:
            file.write(str(student) + "\n")
        print("Student registered successfully")

    def get_students(self):
        students = []
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, course, level, availability, exam_weeks = line.strip().split(",")
                    students.append(Student(name, course, level, availability, int(exam_weeks)))
        except FileNotFoundError:
            pass
        return students

    def view_students(self):
        students = self.get_students()
        if not students:
            print("No students registered yet")
            return
        print("\nREGISTERED STUDENTS")
        for s in students:
            print(s)
