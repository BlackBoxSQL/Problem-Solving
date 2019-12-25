n = int(input())
i = 1
for i in range(n+1):
    square = i*i
    if square % 2 == 0 and square != 0:
        print("{}^2 = {}".format(i, square))
