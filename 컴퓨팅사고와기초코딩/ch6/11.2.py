def compute_root(a, b, c):
    if (a != 0.0):
        r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
        print('해는', r1, '또는', r2)
    else:
        print('2차방정식이 아님')


compute_root(1, 2, -8)
compute_root(2, -6, -8)
compute_root(0, 2, 4)
