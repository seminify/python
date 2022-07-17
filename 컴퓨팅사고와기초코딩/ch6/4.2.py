def get_sum(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum


for n in range(10, 100, 20):
    hap = get_sum(1, n)
    print('1+2+..+', n, '=', hap)
