n = int(input())
c = 1
while n > 0:
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    moves = abs(x1 - x2) + abs(y1 - y2)
    print("Case ", c,": ", moves, sep='',end='\n')
    n -= 1
    c += 1

# Runtime error