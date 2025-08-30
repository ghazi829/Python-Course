# Defining a Class
class Bike:
    # Initializing a Constructor
    def  __init__(self,bColor,bGears,bModel,bPrice):
        self.bikeColor = bColor
        self.bikeGears = bGears
        self.bikeModel = bModel
        self.bikePrice = bPrice

# Creating an Object
obj1 = Bike("Red",5,"ABC101",15000)
print(obj1.bikeColor)
print(obj1.bikePrice)
print("--------------------------------------------------------")
# Creating an Object
obj2 = Bike("Black",6,"XYZ101",18000)
print(obj2.bikeColor)
print(obj2.bikeGears)
