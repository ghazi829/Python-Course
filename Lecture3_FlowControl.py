# Variable Initialization
firstValue = int(input("Enter first value: "))
secondValue = int(input("Enter second value: "))
choice = input("Enter your choice (+,-,*,/) ")

if choice == '+':
    addition = firstValue + secondValue
    print("SUM of first & second value:", addition)
elif choice == '-':
    subtraction = firstValue - secondValue
    print("SUB of first & second value:", subtraction)
elif choice == '*':
    multiplication = firstValue * secondValue
    print("MUL of first & second value:", multiplication)
elif choice == '/':
    division = firstValue / secondValue
    print("DIV of first & second value:", division)
else:
    print("Invalid choice entered...try again")

