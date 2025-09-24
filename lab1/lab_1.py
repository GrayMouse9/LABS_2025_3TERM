import sys
import math

def get_coef(index, prompt):
    while True:
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except IndexError:
            # Вводим с клавиатуры
            coef_str = input(prompt)
        try:
            coef = float(coef_str)
            return coef
        except ValueError:
             print("Ошибка: нужно ввести число.")



def get_biquadratic_roots(a, b, c):
    result = []

    # Решаем квадратное уравнение относительно y = x^2
    D = b*b - 4*a*c
    if D < 0:
        return result  # нет действительных решений

    if D == 0.0:
        y = -b / (2.0*a)
        if y >= 0:
            result.append(math.sqrt(y))
            result.append(-math.sqrt(y))
    else:
        sqD = math.sqrt(D)
        y1 = (-b + sqD) / (2.0*a)
        y2 = (-b - sqD) / (2.0*a)
        for y in (y1, y2):
            if y >= 0:
                result.append(math.sqrt(y))
                result.append(-math.sqrt(y))

    # убираем дубликаты (например, если корень равен 0)
    result = sorted(set(result))
    return result


def main():

    a = get_coef(1, 'Введите коэффициент A: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')

    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0.")
        return

    roots = get_biquadratic_roots(a, b, c)

    if not roots:
        print('Действительных корней нет')
    elif len(roots) == 1:
        print('Один действительный корень: {}'.format(roots[0]))
    else:
        print('Действительные корни:', ', '.join(map(str, roots)))


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

