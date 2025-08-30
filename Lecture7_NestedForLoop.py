# Outer Loop is for Rows
for x in range(1,6):
    # Inner Loop is for Columns
    for y in range(1,6):
        print(y,end=" ")
    print("")
print("====================================================")
for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=" ")
    print("")
print("====================================================")
for x in range(1,6):
    for y in range(1,x+1):
        print(x,end=" ")
    print("")
print("====================================================")
for x in range(1,6):
    for y in range(1,x+1):
        print("H",end=" ")
    print("")
print("====================================================")
for x in range(1,6):
    for y in range(1,x+1):
        print("H",end=" ")
    print("")
print("====================================================")
# Outer Loop is for ROWs
for x in range(1,10):
    # 1st Inner Loop is for Spaces
    for y in range(10,x,-1):
        print(" ",end="")
    # 2nd Inner Loop is for Numbers
    for z in range(1,x+1):
        print("+",end=" ")
    print("")
print("===================================================")
for x in range(1,10):
    for y in range(10,x,-1):
        print(" ",end="")
    for z in range(1,x+1):
        print(x,end=" ")
    print()
print("===================================================")
