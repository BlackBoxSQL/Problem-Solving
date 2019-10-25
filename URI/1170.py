if __name__ == "__main__":
    for i in range(int(input())):
        food = float(input())
        dias = 0
        while food > 1:
            food -= 0.5*food
            dias += 1
        print("{} dias".format(dias))
