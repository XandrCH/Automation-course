import math
side = float(input( 'Введите длинну стороны квадрата:'))
def square(side):
    return f'Площадь квадрата: {math.ceil(side*side)}'
print(square(side))