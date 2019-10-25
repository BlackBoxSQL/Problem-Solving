while True:
    try:
        v, t = map(int, input().split())
        result = v*(2*t)
        print(result)
    except EOFError:
        break
