from math import factorial
if __name__ == '__main__':
    n = int(input())
    r = int(input())

    s=factorial(n)/(factorial(r)*factorial(n-r))
    print(s)
