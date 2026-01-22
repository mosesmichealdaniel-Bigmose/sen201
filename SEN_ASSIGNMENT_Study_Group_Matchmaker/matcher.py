
class Matcher:
    def __init__(self, storage):
        self.storage = storage

    def match_groups(self):
        students = self.storage.get_students()
        matched = False

        print("\nMATCHED STUDY GROUPS")
        for i in range(len(students)):
            for j in range(i + 1, len(students)):
                s1 = students[i]
                s2 = students[j]

                if (
                    s1.course == s2.course and
                    s1.level == s2.level and
                    s1.availability == s2.availability and
                    abs(s1.exam_weeks - s2.exam_weeks) <= 1
                ):
                    print(f"- {s1.name} and {s2.name} | Course: {s1.course}")
                    matched = True

        if not matched:
            print("No compatible study groups found yet")
