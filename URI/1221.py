testcase = int(input())
i = 0
while i < testcase:

    number = int(input())
    # prime number is always greater than 1
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number, "Not Prime")
                break
        else:
            print(number, "Prime")
    # if the entered number is less than or equal to 1
    # then it is not prime number
    else:
        print(number, "Not Prime")
    i += 1
