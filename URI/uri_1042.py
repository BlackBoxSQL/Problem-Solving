if __name__ == '__main__':
    numbers = []
    for i in range(0, 3):
        data = int(input())
        numbers.append(data)

print("\n".join(map(str,sorted(numbers))))
print("\n")
print("\n".join(map(str,numbers)))
