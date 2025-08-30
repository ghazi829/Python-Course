class Parent:

    def Calc(self):
        print("Parent Class Calc method")

class Child(Parent):

    def Test(self):
        print("Child Class Test method")

class GrandChild(Child):

    def Work(self):
        print("GrandChild Class Work method")

obj1 = GrandChild()
obj1.Work()
obj1.Test()
obj1.Calc()
