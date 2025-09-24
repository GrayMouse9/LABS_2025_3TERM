from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np # Импортируем установленный пакет

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

    # Вызываем метод из внешнего пакета numpy
    print("\nПример использования внешнего пакета:")
    array = np.array([1, 2, 3, 4, 5])
    print("Массив numpy:", array)
    print("Среднее значение в массиве:", np.mean(array))


if __name__ == "__main__":
    main()
