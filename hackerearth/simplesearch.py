def linear_search(L, x):
    # n = len(L)
    # for i in range(n):
    for i in range(len(L)):
        if L[i] == x:
            print(i)


test = int(input())
L = []
for i in range(test):
    items = int(input())
    L.append(items)

x = int(input())
linear_search(L, x)
