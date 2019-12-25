x = input().split()  # for taking space separated vlues
i, f = x

i = int(x[0])  # converting them in int
f = int(x[1])  # converting them in int

if i < f:
    t = f - i
else:
    t = (24 - i) + f
print('O JOGO DUROU {} HORA(S)'.format(t))
