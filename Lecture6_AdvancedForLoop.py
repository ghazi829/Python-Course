tot = 0
for x in range(1,11):
    # tot = tot + x
    tot += x
print(tot)
print("===================================================")
fact = 1
for x in range(1,6):
    fact = fact * x
print(fact)
print("===================================================")
print("1 1 2 3 5 8 13 21 34 55")
first = 1
second = 0
for x in range(1,11):
    third = first + second
    print(third,end=" ")
    first = second
    second = third