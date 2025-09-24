import unittest
import math
from lab2.rectangle import Rectangle
from lab2.circle import Circle
from lab2.square import Square

class TestShapeAreas(unittest.TestCase):

    def test_rectangle_area(self):
        """Тестирование вычисления площади прямоугольника."""
        rect = Rectangle(5, 10, "синий")
        self.assertEqual(rect.calculate_area(), 50)

    def test_circle_area(self):
        """Тестирование вычисления площади круга."""
        circ = Circle(7, "зеленый")
        # Используем assertAlmostEqual для сравнения чисел с плавающей запятой
        self.assertAlmostEqual(circ.calculate_area(), math.pi * (7 ** 2))

    def test_square_area(self):
        """Тестирование вычисления площади квадрата."""
        sq = Square(6, "красный")
        self.assertEqual(sq.calculate_area(), 36)

    def test_square_inheritance(self):
        """Тестирование того, что у квадрата ширина и высота равны."""
        sq = Square(8, "желтый")
        self.assertEqual(sq.width, 8)
        self.assertEqual(sq.height, 8)

# Это позволяет запускать тесты напрямую из этого файла
if __name__ == '__main__':
    unittest.main()
