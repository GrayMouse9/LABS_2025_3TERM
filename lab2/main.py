from lab2.rectangle import Rectangle
from lab2.circle import Circle
from lab2.square import Square
import numpy as np

def main():
    # Установим N (например, номер по списку)
    N = 10

    # Создаем объекты
    rect = Rectangle(N, N, "синего")
    circ = Circle(N, "зеленого")
    sq = Square(N, "красного")

    # Выводим информацию об объектах
    print(rect)
    print(circ)
    print(sq)

    # Демонстрация использования numpy для вычислений с фигурами
    print("\n" + "="*50)
    print("Использование NumPy для анализа фигур:")
    print("="*50)

    # Создаем массив площадей фигур с помощью numpy
    areas = np.array([
        rect.calculate_area(),
        circ.calculate_area(),
        sq.calculate_area()
    ])

    # Создаем массив названий фигур
    names = np.array([rect.get_name(), circ.get_name(), sq.get_name()])

    # print(f"Площади фигур: {areas}")
    print(f"Средняя площадь: {np.mean(areas):.2f}")
    print(f"Максимальная площадь: {np.max(areas):.2f}")
    print(f"Минимальная площадь: {np.min(areas):.2f}")

    # Находим фигуру с максимальной площадью
    max_area_index = np.argmax(areas)
    print(f"Фигура с наибольшей площадью: {names[max_area_index]} ({areas[max_area_index]:.2f})")

    # Сумма всех площадей
    print(f"Сумма всех площадей: {np.sum(areas):.2f}")


if __name__ == "__main__":
    main()
