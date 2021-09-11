# polymorphism Example
class Principle:
    def role(self):
        print("Principle: I manage all activities of the college")
class Dean:
    def role(self):
        print("Dean: I am decision taking person")
class Hod:
    def role(self):
        print("Hod: I have responsibility of teachers and students")
class Faculty:
    def role(self):
        print("Faculty: I have to complete syllabus succesfully")
def func(obj):
    obj.role()
campus=[Principle(),Dean(),Hod(),Faculty()]
for obj in campus: 
    func(obj)


# Single level inheritance
class College:
    def college_name(self):
        print("YCCE") 
class Student(College):
    def student_info(self):
        print("Name:Aishwarya Nandanwar") 
        print("Branch:Electronics")
obj = Student()
obj.college_name()
obj.student_info()


# Multilevel Inheritance
class College:
    def college_name(self):
        print("YCCE")
class Student(College):
    def student_info(self):
        print("Name:Aishwarya Nandanwar")
        print("Branch:Electronics")
class Exam(Student):
    def subject(self):
        print("Subject 1:Engineering Graphics")
        print("Subject 2: Maths 1")
        print("Subject 3: C-language")
obj = Exam()
obj.college_name()
obj.student_info()
obj.subject()


# Multiple Inheritance
class SubjMarks:
    math = int(input("Enter paper marks of Maths"))
    EG = int(input("Enter paper marks of EG"))
    C = int(input("Enter paper marks of C "))
    English = int(input("Enter paper marks of english"))
class PractMarks:
  cpract = int(input("Enter practicals marks of C Language"))
class TotalMarks(SubjMarks,PractMarks):
    def total(self):
        if self.math>=40 and self.C>40 and self.English and self.cpract>=20:
            print("Pass")
        else:
            print("Fail")
obj = TotalMarks()
obj.total()

# Method overriding concept
class Father:
    def bike(self):
        print("KTM")
    def laptop(self):
        print("Laptop")
class Aman(Father):
    def laptop(self):
        print("As per my programming language this is not cool for me")
        print("Laptop So Expensive")
obj = Aman()
obj.bike()
obj.laptop()


# Creating a base class
class Base:
    def __init__(self):
        self._a=2
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling Protected Member of Base Class")
        print(self._a)
obj1 = Derived()
obj2 = Base()
print(obj2)


# Constructor Overriding
class Father:
    def __init__(self): 
        print("Father:= I am on time on breakfast table")
def Child(Father):
    def __init__(self):
        print("Child:=I will be late for breakfast")
obj = Child()