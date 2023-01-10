from math import sqrt

message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> None:
    """Проверяет введенное число."""
    if your_number <= 0:
        message = 'число равно нулю'
        print(message)
        return your_number
    result = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень '
          f'из введенного вами числа. '
          f'Это будет: {result}')
    return None


print(message)
calc(25.5)
