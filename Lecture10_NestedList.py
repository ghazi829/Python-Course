#ali_marks = [45,56,56,23]

std_names = ["Farman","Khalid","Kashif"]
std_marks = [[34,45,56],[56,78,90],[67,23,89]]
#std_total = [135,224,179]
print(std_names)
print(std_marks)

for x in std_marks:
    print(x)
print("===================================================")
std_total = []
for x in range(3):
    tot = sum(std_marks[x])
    per = tot/300 * 100
    print(std_names[x]," - ",std_marks[x],"-",tot,"-",per)
    std_total.append(tot)

print(std_total)