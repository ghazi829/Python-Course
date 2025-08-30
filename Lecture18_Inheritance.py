
class Parent:
    def test():
        print("This is a test method from Parent class.")

class Child(Parent):
    def work():
        print("This is a work method from Child class.")

# obj1 = Parent
# obj1.test()

obj1 = Child
obj1.test()  # Calling Parent class method
obj1.work()  # Calling Child class method   
