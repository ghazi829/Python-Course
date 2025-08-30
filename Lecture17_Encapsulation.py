# Object Oriented Programming - OOP

class Student:

    def __init__(self, stdName, stdAge, stdClass):
        self.__StudentName = stdName
        self.__StudentAge = stdAge
        self.__StudentClass = stdClass

    # Setters Methods
    def setName(self, stdName):
        self.__StudentName = stdName

    def setAge(self, stdAge):
        self.__StudentAge = stdAge

    def setClass(self, stdClass):
        self.__StudentClass = stdClass

    # Getters Methods
    def getName(self):
        return self.__StudentName

    def getAge(self):
        return self.__StudentAge

    def getClass(self):
        return self.__StudentClass


# sname = input("Enter your Name: ")
# sage = int(input("Enter your Age: "))
# sclass = input("Enter your Class: ")
#
# obj1 = Student(sname,sage,sclass)
obj1 = Student("Zubair Ali", 23, "10th - A")

print("Student Name:", obj1.getName())
print("Student Age:", obj1.getAge())
print("Student Class:", obj1.getClass())
print("==================================================================")
obj1.setName("Zunair Ali")
obj1.setAge(25)
obj1.setClass("10th - B")

