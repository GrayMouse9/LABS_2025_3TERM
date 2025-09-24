import sys
import math

class BiquadraticSolver:
    """
    Класс для решения биквадратных уравнений вида ax^4 + bx^2 + c = 0.
    """

    def __init__(self):
        """
        Конструктор класса. Инициализирует коэффициенты и список корней.
        """
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        self.roots_list = []

    def get_coef(self, index, prompt):
        """
        Читает коэффициент из командной строки или запрашивает ввод с клавиатуры,
        повторяя запрос до тех пор, пока не будет введено корректное число.

        Args:
            index (int): Номер параметра в командной строке.
            prompt (str): Приглашение для ввода коэффициента.

        Returns:
            float: Коэффициент уравнения.
        """
        # Сначала пытаемся прочитать из аргументов командной строки
        if index < len(sys.argv):
            try:
                coef = float(sys.argv[index])
                print(f'{prompt} {coef} (из командной строки)')
                return coef
            except ValueError:
                print(f"Некорректное значение '{sys.argv[index]}' в командной строке. Введите его с клавиатуры.")

        # Если не получилось, запрашиваем ввод с клавиатуры в цикле
        while True:
            try:
                print(prompt)
                coef_str = input()
                return float(coef_str)
            except ValueError:
                print("Ошибка: Введите корректное действительное число.")

    def get_coefs(self):
        """
        Чтение трёх коэффициентов A, B и C.
        """
        print("Решение биквадратного уравнения ax^4 + bx^2 + c = 0")
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        """
        Вычисление действительных корней биквадратного уравнения.
        """
        a, b, c = self.coef_A, self.coef_B, self.coef_C

        # Если A=0, уравнение становится квадратным: bx^2 + c = 0
        if a == 0:
            if b != 0:
                val = -c / b
                if val > 0:
                    root = math.sqrt(val)
                    self.roots_list = [-root, root]
                elif val == 0:
                    self.roots_list = [0.0]
            # Если b=0 и c=0, корней бесконечно много (любое число),
            # если b=0 и c!=0, корней нет. Для простоты оставляем список пустым.
            return

        # Решаем вспомогательное квадратное уравнение at^2 + bt + c = 0, где t = x^2
        D = b*b - 4*a*c

        t_roots = []
        if D == 0.0:
            t_roots.append(-b / (2.0*a))
        elif D > 0.0:
            sqD = math.sqrt(D)
            t_roots.append((-b + sqD) / (2.0*a))
            t_roots.append((-b - sqD) / (2.0*a))

        # Если D < 0, действительных корней для t нет, значит и для x их тоже нет.

        # Находим корни x из положительных корней t
        final_roots = set()
        for t in t_roots:
            if t > 0:
                x = math.sqrt(t)
                final_roots.add(x)
                final_roots.add(-x)
            elif t == 0:
                final_roots.add(0.0)

        # Сохраняем отсортированный список уникальных корней
        self.roots_list = sorted(list(final_roots))

    def print_roots(self):
        """
        Вывод вычисленных корней в консоль.
        """
        if not self.roots_list:
            print('Результат: Нет действительных корней.')
        else:
            num_roots = len(self.roots_list)
            roots_str = ', '.join(map(str, self.roots_list))
            if num_roots == 1:
                print(f'Результат: Найден один корень: {roots_str}')
            else:
                print(f'Результат: Найдено корней ({num_roots}): {roots_str}')

def main():
    """
    Основная функция.
    """
    # Создание объекта класса
    solver = BiquadraticSolver()
    # Последовательный вызов необходимых методов
    solver.get_coefs()
    solver.calculate_roots()
    solver.print_roots()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()
