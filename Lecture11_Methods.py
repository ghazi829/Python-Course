
# Method Definition
def test():
    print("It's a Test method")

def calc():
    a = 10
    b = 20
    c = a + b
    print("SUM of A & B: ",c)

def obtain(math,english,urdu,comp,phys):
    tot = math + english + urdu + comp + phys
    print("Obtain marks: ",tot)

def salary(wages,leaves):
    tsalary = wages*30
    tcut = leaves * wages

    netsalary = tsalary - tcut

    # print("Net Salary is: ",netsalary)
    return netsalary

# Main Function
print("WElcome to Main Function")

# Method Calling
test()
calc()
obtain(45,56,67,78,89)
totalsalary = salary(800,3)
print("Net Salary before bonus: is: ",totalsalary)
if totalsalary<=15000:
    totalsalary += 2000

print("Net Salary after bonus: is: ",totalsalary)