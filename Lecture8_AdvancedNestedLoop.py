for x in range(1,11):
    for y in range(1,11):
        print("*",end=" ")
    print()
print("=================================================")
for x in range(1,11):
    for y in range(1,11):
        if x==1 or x==10 or y==1 or y==10:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print("=================================================")
for x in range(1,11):
    for y in range(1,11):
        if x==1 or x==5 or y==1:
            print("*",end=" ")
        else:
            if y==10 and x<=5:
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
print("=================================================")
for x in range(1,10):
    for y in range(10,x,-1):
        print(" ",end="")
    for z in range(1,x+1):
        if x==1 or x==2 or z==1 or z==x or x==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
print("=================================================")
for x in range(9,0,-1):
    for y in range(10,x,-1):
        print(" ",end="")
    for z in range(1,x+1):
        if x==1 or x==2 or z==1 or z==x:v 
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print("")
print("=================================================")
for x in range(1,11):
    for y in range(1,11):
        if y==1 or y==10:
            print("*",end=" ")
        else:
            if x+y==11:
                print("*", end=" ")
            else:
                print(" ",end=" ")
    print()
p
