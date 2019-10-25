if __name__ == "__main__":
    times = int(input())
    a = 0
    while a < times:
        diamond = str(input())
        partone = diamond.count('<')
        parttwo = diamond.count('>')
        if partone > parttwo:
            print(parttwo)
        if partone < parttwo:
            print(parttwo)
        if partone == parttwo:
            print(partone)
        a += 1
