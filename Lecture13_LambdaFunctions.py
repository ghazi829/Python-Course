
def test():
    print("It's a Test method")

def sum(x,y):
    tot = x + y
    print("Total is: ",tot)

def salary(days,wages):
    return days * wages

def findpass(marks):
    pmarks = []
    for x in marks:
        if x>=40:
            pmarks.append(x)
    return pmarks
# Main Method
print("Welcome to Main method")
test()
simple = lambda : print("It's Simple Lambda Function")
simple()

sum(10,2)
doit = lambda a,b: print("SUM of a & b: ",a+b)
doit(10,5)

print("Total salary is: ",salary(25,500))
area = lambda l,w: l*w
print("Total Area is: ",area(5,3))

khalid_marks = [45, 23, 78, 39, 66]
print("Khalid marks: ",khalid_marks)
print("Khalid PASS Marks", findpass(khalid_marks))



failedmarks = list(filter(lambda x:x<40,khalid_marks))
print(failedmarks)

newmarks = list(map(lambda x:x+5,khalid_marks))
print(newmarks)

onlyfailedpapers = list(map(lambda x:x+5 if x<=40 else x+0,khalid_marks))
print(onlyfailedpapers)

