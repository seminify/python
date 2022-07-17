def get_factorial(start, end):
    fact = 1
    for i in range(start, end + 1):
        fact *= i
    return fact


n = 4
f = get_factorial(1, n)
print(n, '! =', f)
n = 5
f = get_factorial(1, n)
print(n, '! =', f)
