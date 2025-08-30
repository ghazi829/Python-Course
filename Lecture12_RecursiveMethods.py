
# FIND SUM using Iteration
def findSUM():
    total = 0
    for x in range(1, 11):
        total = total + x
    print("SUM: ", total)

# FIND SUM using Recursion
def findSUMrec(num):
    if num == 0:
        return num
    else:
        return num + findSUMrec(num - 1)

# 10 + 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 55

def findFACT():
    fact = 1
    for x in range(1, 6):
        fact = fact * x

    print("FACT: ", fact)

def findFACTrec(num):
    if num == 1:
        return num
    else:
        return num * findFACTrec(num - 1)

# 5 * 4 * 3 * 2 * 1
# Main Method Section
findSUM()
print(findSUMrec(10))
findFACT()
findFACTrec(5)