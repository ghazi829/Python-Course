ali_math_marks = 56
ali_urdu_marks = 76
ali_comp_marks = 98
ali_phys_marks = 22

ali_total_marks = ali_math_marks + ali_urdu_marks + ali_comp_marks

ali_marks = [56,76,98,22]
print(ali_marks)
print(ali_marks[0])
print("======================================")
for x in range(0,4):
    print(ali_marks[x])

print("======================================")
for x in range(4):
    print(ali_marks[x])

print("======================================")
for x in ali_marks:
    print(x)
print("======================================")
tot = 0
for x in ali_marks:
    tot += x
print("Total Marks: ",tot)
print("======================================")
max = 0
for x in ali_marks:
    if x>max:
        max = x
print("Max Marks: ",max)
print("======================================")
std_names = ["Khalid","Farman","Usman","Zubair","Imran","Asad"]
for x in std_names:
    print(x)
