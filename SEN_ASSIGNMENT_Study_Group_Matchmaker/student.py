
class Student:
    def __init__(self, name, course, level, availability, exam_weeks):
        self.name = name
        self.course = course
        self.level = level
        self.availability = availability
        self.exam_weeks = exam_weeks

    def __str__(self):
        return f"{self.name},{self.course},{self.level},{self.availability},{self.exam_weeks}"
