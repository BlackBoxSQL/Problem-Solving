if __name__ == "__main__":
    a = 1
    toss = []
    test = int(input())
    while a <= test:
        value = int(input())
        toss.append(value)
        a += 1
    countzero = toss.count(0)
    countone = toss.count(1)
    print("Mary won {} times and John won {} times".format(countzero, countone))
