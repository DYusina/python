from math import *


# прямоугольник описываем левой верхней точкой, его верхней и боковой сторонами
class Rectangle:
    def __init__(self, x, y, a, b):
        self.x = x
        self.y = y
        self.a = a
        self.b = b

    def perimeter(self):
        return 2 * (self.a + self.b)

    def area(self):
        return self.a*self.b

    def diagonal(self):
        return sqrt(self.a ** 2 + self.b ** 2)

    def intersection(self, other):
        # для каждого прямоугольника вычислим правую нижнюю точку
        x1 = self.x + self.a
        y1 = self.y - self.b
        x2 = other.x + other.a
        y2 = other.y - other.b

        intersection_width = max(0, min(x1, x2) - max(self.x, other.x))
        intersection_height = max(0, min(self.y, other.y) - max(y1, y2))
        # print(intersection_width)
        # print(intersection_height)

        if intersection_width == 0 or intersection_height == 0:
            return 0

        return intersection_width * intersection_height


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def length(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2

    def intersection(self, other):
        #  расстояние между центрами кругов
        d = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

        # круги не пересекаются
        if d >= self.radius + other.radius:
            return 0

        # один внутри другого
        if d <= abs(self.radius - other.radius):
            return pi * min(self.radius, other.radius) ** 2

        r1, r2 = self.radius, other.radius
        area = (r1 ** 2 * acos((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d * r1)) +
                r2 ** 2 * acos((d ** 2 + r2 ** 2 - r1 ** 2) / (2 * d * r2)) -
                0.5 * sqrt((-d + r1 + r2) * (d + r1 - r2) * (d - r1 + r2) * (d + r1 + r2)))

        return area


rect1 = Rectangle(1, 3, 4, 4)
rect2 = Rectangle(3, 1, 4, 4)
print(f'rect1 perimeter: {rect1.perimeter()}')
print(f'rect1 area: {rect1.area()}')
print(f'rect2 diagonal: {rect1.diagonal()}')
print(f'rect1 and rect2 intersection: {rect1.intersection(rect2)}')
print()

circle1 = Circle(0, 0, 5)  # Круг с центром в (0, 0) и радиусом 5
circle2 = Circle(3, 0, 5)  # Круг с центром в (3, 0) и радиусом 5

print(f'circle1 area: {circle1.area()}')
print(f'circle2 length: {circle2.length()}')
print(f'circle1 and circle2 intersection: {circle1.intersection(circle2)}')


