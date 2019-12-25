n = int(input())
if n <= 100 and n >= 1:
    if n == 2:
        print("NO")
    elif n % 2 == 0:
        print("YES")
    else:
        print("NO")
