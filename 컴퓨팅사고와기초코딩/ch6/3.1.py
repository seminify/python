def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area


c_area = calculate_area(10.0)
print('반지름 10인 원의 면적은', c_area)
c_area = calculate_area(5.0)
print('반지름 5인 원의 면적은', c_area)
