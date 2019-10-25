if __name__ == "__main__":
    mylist = [1, 2, 3]
    newlist = mylist.copy()
    newlist.append(4)
    print(mylist)
    print(newlist)

    # other way
    mylist2 = [1, 2, 3]
    newlist2 = mylist2[:]
    newlist2.append(4)
    print(mylist2)
    print(newlist2)

    # otherway
    mylist3 = [1, 2, 3]
    newlist3 = list(mylist3)
    newlist3.append(4)
    print(mylist3)
    print(newlist3)
