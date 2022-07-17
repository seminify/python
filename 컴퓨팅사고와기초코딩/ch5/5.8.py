sum = 0
for i in range(1, 101, 2):
    sum += i
    if i != 99:
        print(i, '+', end=' ')
    else:
        print(i, '=', sum)
