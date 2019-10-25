if __name__ == "__main__":
    p1 = int(input())
    c1 = int(input())
    p2 = int(input())
    c2 = int(input())

    if p1*c1 == p2*c2:
        print("0\n")
    if p1*c1 < p2*c2:
        print("-1\n")
    else:
        print("1\n")
