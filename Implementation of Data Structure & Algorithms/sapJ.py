if __name__ == "__main__":
    test = int(input())
    value = 0
    for i in range(0, test):
        insertvalue = int(input())
        if insertvalue == 1:
            value += 1
    print(value)
