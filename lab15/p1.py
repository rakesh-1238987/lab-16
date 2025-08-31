class Student:
    def __init__(self, name):
        self.name = name
        self.subjects = []

    def enroll(self, *subjects):
        self.subjects.extend(subjects)

s1 = Student("Rakesh")
s1.enroll("Math", "Physics", "Chemistry")
print(s1.subjects)
