sum = 0
for i in range(2, 101, 2):
    sum += i
    if i != 100:
        print(i, '+', end=' ')
    else:
        print(i, '=', sum)
