from functools import reduce
from math import sqrt
# opt.6: 7YES, 10YES, 1YES, 11~YES, 12
# opt.5: 6, 7YES, 2, 11, 12


# 1
def quadratic():
    """
        Функция для вычисления корней квадратного уравнения
    """
    inp = input('Введите корни квадратного уравнения через пробел: ')
    lst = list(map(int, inp.split()))
    A, B, C = lst
    discriminant = B ** 2 - 4 * A * C
    if discriminant > 0:
        x1 = (-B + sqrt(discriminant)) / (2 * A)
        x2 = (-B - sqrt(discriminant)) / (2 * A)
        return (f'Первый корень равен: {x1}' + '/n'
                f'Второй корень равен: {x2}')
    elif discriminant == 0:
        x = -B / (2 * A)
        return f'Корень равен: {x}'
    else:
        return 'Корней нет'


# 7
def mult_even_and_summ_odd():
    numb = input('Введите 5 чисел через пробел: ')
    numbers = list(map(int, numb.split()))
    if len(numbers) != 5:
        raise Exception('Чисел должно быть пять!')
    even = [i for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]
    return (f'Произведение четных чисел: {reduce(lambda x,y: x*y, even)}' + '\n'
            f'Сумма нечетных чисел равна: {sum(odd)}')


# 10
def rules():
    numb = input('Введите 5 чисел через пробел: ')
    numbers = list(map(int, numb.split()))
    if len(numbers) != 5:
        raise Exception('Чисел должно быть пять!')
    even = [str(i) for i in numbers if i % 2 == 0]
    odd = [i for i in numbers if i % 2 != 0]
    return (f'По правилу сложения строк: {"".join(even)}' + '\n'
            f'По правилу сложения чисел: {sum(odd)}')


# 11
def power_voltage():
    U1 = 400
    S1 = complex(1000, 500)
    R = 0.5
    X = 1.0
    I = S1.real / U1
    Z = complex(R, X)
    DeltaU = I * Z
    U2 = U1 - DeltaU
    S2 = I * U2.conjugate()
    return (f'Ток в начале линии: {I} А' + '\n'
            f'Падение напряжения на линии: {DeltaU} В' + '\n'
            f'Напряжение на конце линии: {U2} В' + '\n'
            f'Мощность в конце линии: {S2} ВА')

#12
def trans_replacement():
    pass
