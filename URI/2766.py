if __name__ == "__main__":
    names = []
    for i in range(10):
        inputnames = str(input())
        if i == 2 or i == 6 or i == 8:
            names.append(inputnames)
    for name in names:
        print(name)
