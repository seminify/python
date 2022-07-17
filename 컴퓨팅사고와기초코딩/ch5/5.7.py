sum = 0
for i in range(1, 101):
    sum += i
    if i != 100:
        print(i, '+', end=' ')
    else:
        print(i, '=', sum)
