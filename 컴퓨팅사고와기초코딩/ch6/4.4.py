def get_factorial(start, end):
    fact = 1
    for i in range(start, end + 1):
        fact *= i
    return fact


for n in range(1, 10, 1):
    f = get_factorial(1, n)
    print(n, '! =', f)
