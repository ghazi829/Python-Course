
class Parent:

    def __init__(self,pname,pfamily):
        self.parentName = pname
        self.parentFamily = pfamily


class Child(Parent):

    def __init__(self, cname, cage, pname, pfamily):
        super().__init__(pname, pfamily)  # Call the constructor of Parent
        self.childName = cname
        self.childAge = cage

    def test(self):
        print("This is a test method from Child class.")


# obj1 = Parent
# obj1.test()

obj1 = Child("Zubair", 24,"Khalid Khan","Gujjar")

print("Child Name:", obj1.childName)
print("Child Age:", obj1.childAge)
