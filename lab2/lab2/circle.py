import math
import numpy as np
from .geometric_figure import GeometricFigure
from .figure_color import FigureColor


class Circle(GeometricFigure):
    """Класс для представления круга."""
    name = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.figure_color = FigureColor(color)

    def calculate_area(self):
        """Вычисляет площадь круга с использованием numpy для точности."""
        return np.pi * (self.radius ** 2)

    def calculate_circumference(self):
        """Вычисляет длину окружности с использованием numpy."""
        return 2 * np.pi * self.radius

    def get_numpy_array(self):
        """Возвращает параметры круга как numpy array."""
        return np.array([self.radius, self.calculate_area(), self.calculate_circumference()])

    def __repr__(self):
        return "Фигура: {}. Радиус: {}. Цвет: {}. Площадь: {:.2f}. Длина окружности: {:.2f}.".format(
            self.get_name(),
            self.radius,
            self.figure_color.color,
            self.calculate_area(),
            self.calculate_circumference()
        )

    @classmethod
    def get_name(cls):
        return cls.name
