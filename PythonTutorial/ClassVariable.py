
class Student:

    class_year = 2025
    num_student = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Squiward", 55)
student4 = Student("Sandy", 27)

# print(student1.name)
# print(student1.age)
# print(Student.class_year)

# print(Student.num_student)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)
