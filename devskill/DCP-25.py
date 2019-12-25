test = int(input())
for i in range(test):
    text = input()
    rev = text[::-1]
    if rev == text:
        print("Yes")
    else:
        print("No")
