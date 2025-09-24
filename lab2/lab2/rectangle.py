from lab2.geometric_figure import GeometricFigure
from lab2.figure_color import FigureColor

class Rectangle(GeometricFigure):
    """
    Класс для представления прямоугольника.
    """
    name = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.figure_color = FigureColor(color)

    def calculate_area(self):
        """
        Вычисляет площадь прямоугольника.
        """
        return self.width * self.height

    def __repr__(self):
        return "Фигура: {}. Ширина: {}. Высота: {}. Цвет: {}. Площадь: {}.".format(
            self.get_name(),
            self.width,
            self.height,
            self.figure_color.color,
            self.calculate_area()
        )

    @classmethod
    def get_name(cls):
        return cls.name
