# Object Oriented Programming - OOP

class Student:

    def __init__(self,stdName,stdAge,stdClass):
        self.StudentName = stdName
        self.StudentAge = stdAge
        self.StudentClass = stdClass

# Setters Methods
    def setName(self,stdName):
        self.StudentName = stdName

    def setAge(self,stdAge):
        self.StudentAge = stdAge

    def setClass(self,stdClass):
        self.StudentClass = stdClass

# Getters Methods
    def getName(self):
        return self.StudentName

    def getAge(self):
        return self.StudentAge

    def getClass(self):
        return self.StudentClass

# sname = input("Enter your Name: ")
# sage = int(input("Enter your Age: "))
# sclass = input("Enter your Class: ")
#
# obj1 = Student(sname,sage,sclass)
obj1 = Student("Zubair Ali",23,"10th - A")

print("Student Name:",obj1.StudentName)
print("Student Age:",obj1.StudentAge)
print("Student Class:",obj1.StudentClass)
print("==================================================================")
obj1.setName("Zunair Ali")
obj1.setAge(25)
obj1.setClass("10th - B")

print("Student Name:",obj1.StudentName)
print("Student Age:",obj1.StudentAge)
print("Student Class:",obj1.StudentClass)