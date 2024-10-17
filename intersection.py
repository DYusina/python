import random
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
        return self.a * self.b

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

        if intersection_width == 0 or intersection_height == 0:
            return 0

        return intersection_width * intersection_height


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def length(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

    @staticmethod
    def in_circle(x, y, x0, y0, radius):
        if sqrt((x - x0) ** 2 + (y - y0) ** 2) <= radius:
            return True
        else:
            return False

    # суть метода в том, что участок пересечения надо заключить в прямоугольник,
    # потом случайно ставить туда точки, посчитать пропорцию точек повавших в
    # пересечение к количеству всех точек и домножить на площадь прямоугольника
    # проблема метода в том что каждфй раз он может давать разный ответ из-за случайного
    # расположения точек
    @staticmethod
    def monte_carlo(x1, y1, rad1, x2, y2, rad2):
        right_border_x = min(x1 + rad1, x2 + rad2)
        left_border_x = max(x1 - rad1, x2 - rad2)

        center_dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        # расстояние от радиуса1 до пересечения линии центров с перпендикуляром на котором
        # находятся пересечения окружностей
        center_to_perpend_intersect = (rad2 ** 2 - rad1 ** 2 - center_dist ** 2) / (2 * center_dist)

        if center_to_perpend_intersect ** 2 > rad1 ** 2:
            return 0

        h = sqrt(rad1 ** 2 - center_to_perpend_intersect ** 2)

        # точка пересечения линии центров с перпендикуляром на котором пересечения окр-тей
        intersect_point_proj_x = x1 + center_to_perpend_intersect * (x2 - x1) / center_dist
        intersect_point_proj_y = y1 + center_to_perpend_intersect * (y2 - y1) / center_dist

        # координаты точек пересечения
        intersection1_x = intersect_point_proj_x + h * (y2 - y1) / center_dist
        intersection1_y = intersect_point_proj_y - h * (x2 - x1) / center_dist

        intersection2_x = intersect_point_proj_x - h * (y2 - y1) / center_dist
        intersection2_y = intersect_point_proj_y + h * (x2 - x1) / center_dist

        # Определяем прямоугольник пересечения
        min_y = min(intersection1_y, intersection2_y)
        max_y = max(intersection1_y, intersection2_y)

        intersection_rect_area = (right_border_x - left_border_x) * (max_y - min_y)

        inside = 0
        total_points = 10000
        for _ in range(total_points):
            point_x = random.uniform(left_border_x, right_border_x)
            point_y = random.uniform(min_y, max_y)

            if Circle.in_circle(point_x, point_y, x1, y1, rad1) and Circle.in_circle(point_x, point_y, x2, y2, rad2):
                inside += 1

        intersection_area = (inside / total_points) * intersection_rect_area
        return intersection_area

    def intersection(self, other):
        #  расстояние между центрами кругов
        d = sqrt((other.x - self.x) ** 2 + (other.y - self.y) ** 2)

        # круги не пересекаются
        if d >= self.radius + other.radius:
            return 0
        # один внутри другого
        elif d <= abs(self.radius - other.radius):
            return pi * min(self.radius, other.radius)**2
        else:
            return Circle.monte_carlo(self.x, self.y, self.radius, other.x, other.y, other.radius)


def main():
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


if __name__ == "__main__":
    main()
