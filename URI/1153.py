# if __name__ == "__main__":
#     def fact(n):
#         f = 1
#         for i in range(1, n+1):
#             f = f*i
#         return f
#     a, b = map(int, input().split())  # taking input with space
#     result = fact(a) + fact(b)
#     print(result)


# avobe answer was not accepted because eof was was not implemeted this way
def Fact(n):
    if n == 0 or n == 0:
        return 1
    return n*Fact(n-1)


while True:
    try:
        a = int(input())
        S = Fact(a)
        print(S)
    except EOFError:
        break
