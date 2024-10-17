from math import *


def find_nok(x, y):
    return x * y // gcd(x, y)


class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}/{self.b}'

    def simplify(self):
        a = self.a
        b = self.b
        new_a = a // gcd(a, b)
        new_b = b // gcd(a, b)
        return Fraction(new_a, new_b)

    def __add__(self, x):
        if isinstance(x, int):
            new_x = Fraction(x, 1)
            return self.__add__(new_x).simplify()
        elif isinstance(x, Fraction):
            a = self.a
            b = self.b
            c = x.a
            d = x.b
            nok = find_nok(b, d)
            a *= nok // b
            c *= nok // d
            new_a = a + c
            return Fraction(new_a, nok).simplify()

    def __sub__(self, x):
        if isinstance(x, int):
            new_x = Fraction(x, 1)
            return self.__sub__(new_x).simplify()
        else:
            a = self.a
            b = self.b
            c = x.a
            d = x.b
            nok = find_nok(b, d)
            # print(sa)
            a *= nok // b
            c *= nok // d
            new_a = a - c
            # print(nok, self.a)
            return Fraction(new_a, nok).simplify()

    def __mul__(self, x):
        if isinstance(x, int):
            new_x = Fraction(x, 1)
            return self.__mul__(new_x)
        else:
            a = self.a
            b = self.b
            c = x.a
            d = x.b
            return Fraction(a*c, b*d).simplify()

    def __truediv__(self, x):
        if isinstance(x, int):
            new_x = Fraction(x, 1)
            return self.__mul__(new_x)
        else:
            a = self.a
            b = self.b
            c = x.a
            d = x.b
            print(a, d, b, c)
            return Fraction(a*d, b*c).simplify()

def main():
    fr1 = Fraction(2, 3)
    fr2 = Fraction(1, 6)
    fr3 = Fraction(4, 12)
    fr4 = Fraction(7, 4)

    print(f'Проверка вывода: {fr1}')
    print(f'{fr3} -> {fr3.simplify()}')
    print("+")
    print(f'{fr1} + {fr2} = {fr1.__add__(fr2)}')
    print(f'{fr1} + 1 = {fr1.__add__(1)}')
    print("-")
    print(f'{fr1} - {fr2} = {fr1.__sub__(fr2)}')
    print(f'{fr4} - 1 = {fr4.__sub__(1)}')
    print('*')
    print(f'{fr1} * {fr2} = {fr1.__mul__(fr2)}')
    print(f'{fr1} * 2 = {fr1.__mul__(2)}')
    print('/')
    print(f'{fr1} / {fr2} = {fr1.__truediv__(fr2)}')
    print(f'{fr3} / 4 = {fr3.__truediv__(4)} пу-пу-пу')


if __name__ == "__main__":
    main()

