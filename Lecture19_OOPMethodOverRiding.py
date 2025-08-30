class Parent:
    def Test(self):
        print("It's a Parent Class Test Method")

    def Calc(self):
        print("It's a Calculator Method")

class Child(Parent):
    def Test(self):
        print("It's a Child Class Test Method")

    def Salary(self):
        print("It's a Salary Method")


# obj1 = Parent()
# obj1.Test()

obj1 = Child()

obj1.Test()
obj1.Calc()
obj1.Salary()