from tkinter import *
from tkinter import Button
import re

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


fr1 = Fraction(2, 3)
fr2 = Fraction(1, 6)
fr3 = Fraction(4, 12)
fr4 = Fraction(7, 4)

# print(f'Проверка вывода: {fr1}')
# print(f'{fr3} -> {fr3.simplify()}')
# print("+")
# print(f'{fr1} + {fr2} = {fr1.__add__(fr2)}')
# print(f'{fr1} + 1 = {fr1.__add__(1)}')
# print("-")
# print(f'{fr1} - {fr2} = {fr1.__sub__(fr2)}')
# print(f'{fr4} - 1 = {fr4.__sub__(1)}')
# print('*')
# print(f'{fr1} * {fr2} = {fr1.__mul__(fr2)}')
# print(f'{fr1} * 2 = {fr1.__mul__(2)}')
# print('/')
# print(f'{fr1} / {fr2} = {fr1.__truediv__(fr2)}')
# print(f'{fr3} / 4 = {fr3.__truediv__(4)} пу-пу-пу')



root = Tk()
root.title("Fractions")
root.geometry("400x300+80+200")


def input(s):
    entry.insert(END, s)


def clear():
    entry.delete(0, END)


def evaluate():
    s = entry.get()
    if "+" in s or "-" in s or "*" in s or "/" in s:
        if s.count("|") == 2:
            operator = re.search(r"[+\-*/]", s).group()
            almost_fraction1 = s.split(operator)[0]
            almost_fraction2 = s.split(operator)[1]
            fr1 = Fraction(int(almost_fraction1.split('|')[0]), int(almost_fraction1.split('|')[1]))
            fr2 = Fraction(int(almost_fraction2.split('|')[0]), int(almost_fraction2.split('|')[1]))
            # print(fr1)
            # print(fr2)
            if "+" in s:
                res = fr1.__add__(fr2)
                res_lab["text"] = res
            elif "-" in s:
                res = fr1.__sub__(fr2)
                res_lab["text"] = res
            elif "*" in s:
                res = fr1.__mul__(fr2)
                res_lab["text"] = res
            elif "/" in s:
                res = fr1.__truediv__(fr2)
                res_lab["text"] = res
        elif s.count("|") == 1:
            operator = re.search(r"[+\-*/]", s).group()
            almost_fraction1 = s.split(operator)[0]
            int_num = int(s.split(operator)[1])
            fr1 = Fraction(int(almost_fraction1.split('|')[0]), int(almost_fraction1.split('|')[1]))
            if "+" in s:
                res = fr1.__add__(int_num)
                res_lab["text"] = res
            elif "-" in s:
                res = fr1.__sub__(int_num)
                res_lab["text"] = res
            elif "*" in s:
                res = fr1.__mul__(int_num)
                res_lab["text"] = res
            elif "/" in s:
                res = fr1.__truediv__(int_num)
                res_lab["text"] = res
        else:
            res_lab['text'] = "Input a FRACTION"
    else:
        res_lab['text'] = "no operation"


lab = Label(root, text ="To input a fraction use |")
lab.place(x=70, y=50)

entry = Entry(root, width=20, font=('', 20))
entry.place(x=70, y=70)

plus_btn = Button(text="+", command=lambda: input('+'))
plus_btn.place(x=80, y=120, height=40, width=40)

minus_btn = Button(text="-", command=lambda: input('-'))
minus_btn.place(x=130, y=120, height=40, width=40)

multiply_btn = Button(text="*", command=lambda: input('*'))
multiply_btn.place(x=180, y=120, height=40, width=40)

division_btn = Button(text="/", command=lambda: input('/'))
division_btn.place(x=230, y=120, height=40, width=40)

equal_btn = Button(text="=", command = evaluate)
equal_btn.place(x=280, y=120, height=40, width=40)

res_lab = Label(root, text="res", font=('', 20), justify="center")
res_lab.place(x=70, y=200)


root.mainloop()
