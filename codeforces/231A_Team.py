test = int(input())
problemlist = []
result = 0
for cases in range(test):
    for threetime in range(3):
        problems = int(input())
        problemlist.append(problems)

totalones = problemlist.count(1)
finalresult = totalones / 3
print(int(finalresult))
