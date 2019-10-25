if __name__ == "__main__":
    j = 0
    for x in range(0, 5):
        a = int(input())
        if a % 2 == 0:
            j += 1
    print("%d valores pares" % (j))
