
from student import Student
from storage import Storage
from matcher import Matcher

def menu():
    print("\nSTUDY GROUP MATCHMAKER")
    print("1. Register Student")
    print("2. Match Study Groups")
    print("3. View All Students")
    print("4. Exit")

def main():
    storage = Storage()
    matcher = Matcher(storage)

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            course = input("Course: ")
            level = input("Skill Level (Beginner/Intermediate/Confident): ")
            availability = input("Availability (Morning/Afternoon/Evening): ")
            exam_weeks = int(input("Weeks to Exam: "))

            student = Student(name, course, level, availability, exam_weeks)
            storage.add_student(student)

        elif choice == "2":
            matcher.match_groups()

        elif choice == "3":
            storage.view_students()

        elif choice == "4":
            print("Good luck with your studies!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
