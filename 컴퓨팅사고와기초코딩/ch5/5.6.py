i = 1
while i <= 9:
    print('[', i, '단 ]')
    for j in range(1, 10, 1):
        k = i * j
        print(i, '*', j, '=', k)
    print('\n')
    i += 1
