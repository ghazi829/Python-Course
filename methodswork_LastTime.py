def add(x,y):
    add = x + y
    print("SUM of val1 & val2: ", add)
def sub(x,y):
    sub = x - y
    print("SUB of val1 & val2: ", sub)
def mul(x,y):
    mul = x * y
    print("MUL of val1 & val2: ", mul)
def div(x,y):
    div = x / y
    print("DIV of val1 & val2: ", div)


val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
choice = input("Enter your choice (+,-,*,/)")

if choice == '+':
    add(val1,val2)
elif choice == '-':
    sub(val1,val2)
elif choice == '*':
    mul(val1,val2)
elif choice == '/':
    div(val1,val2)
else:
    print("Invalid choice entered...")
