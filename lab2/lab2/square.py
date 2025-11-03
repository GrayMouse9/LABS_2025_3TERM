import numpy as np
from .rectangle import Rectangle


class Square(Rectangle):
    """Класс для представления квадрата, наследуется от Прямоугольника."""

    name = "Квадрат"

    def __init__(self, side, color):
        """Вызываем конструктор родительского класса (Rectangle)."""
        super().__init__(side, side, color)
        self.side = side

    def get_numpy_array(self):
        """Возвращает параметры квадрата как numpy array."""
        return np.array([self.side, self.calculate_area(), self.calculate_perimeter(), self.get_diagonal()])

    def __repr__(self):
        return "Фигура: {}. Сторона: {}. Цвет: {}. Площадь: {}. Периметр: {}. Диагональ: {:.2f}.".format(
            self.get_name(),
            self.side,
            self.figure_color.color,
            self.calculate_area(),
            self.calculate_perimeter(),
            self.get_diagonal()
        )

    @classmethod
    def get_name(cls):
        return cls.name
