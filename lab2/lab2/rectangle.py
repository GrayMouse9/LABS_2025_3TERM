import numpy as np
from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


class Rectangle(GeometricFigure):
    """Класс для представления прямоугольника."""

    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.figure_color = FigureColor(color)

    def calculate_area(self) -> float:
        """Вычисляет площадь прямоугольника."""
        return self.width * self.height

    def calculate_perimeter(self):
        """Вычисляет периметр прямоугольника."""
        return 2 * (self.width + self.height)

    def get_numpy_array(self):
        """Возвращает параметры прямоугольника как numpy array."""
        return np.array([self.width, self.height, self.calculate_area(), self.calculate_perimeter()])

    def get_diagonal(self):
        """Вычисляет диагональ прямоугольника с использованием numpy."""
        return np.sqrt(self.width**2 + self.height**2)

    def __repr__(self):
        return "Фигура: {}. Ширина: {}. Высота: {}. Цвет: {}. Площадь: {}. Периметр: {}. Диагональ: {:.2f}.".format(
            self.get_name(),
            self.width,
            self.height,
            self.figure_color.color,
            self.calculate_area(),
            self.calculate_perimeter(),
            self.get_diagonal()
        )

    @classmethod
    def get_name(cls):
        return cls.name
