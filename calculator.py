from tkinter import *
from tkinter import Button
import re


root = Tk()
root.title("Calculator")
root.geometry("370x500+80+200")


def input(s):
    entry.insert(END, s)


def delete():
    if entry.get():
        entry.delete(len(entry.get())-1, END)


def evaluate():
    s = entry.get()
    if ("+" in s) or ("-" in s) or ("*" in s) or ("/" in s) or ("//" in s) or ("%" in s):
        num1 = float(re.split(r'\+|\-|\*|//|/|%', s)[0])
        num2 = float(re.split(r'\+|\-|\*|//|/|%', s)[1])

        if "//" in s:
            if num2 == 0:
                res_lab['text']='ERROR'
            else:
                res = num1//num2
                if res%1 == 0:
                    res_lab['text'] = int(res)
                else:
                    res_lab['text'] = res
        elif "%" in s:
            if num2 == 0:
                res_lab['text']='ERROR'
            else:
                res = num1%num2
                if res%1 == 0:
                    res_lab['text']=int(res)
                else:
                    res_lab['text'] = res
        elif "+" in s:
            res = num1+num2
            if res % 1 == 0:
                res_lab['text'] = int(res)
            else:
                res_lab['text'] = res
        elif "-" in s:
            res = num1 - num2
            if res % 1 == 0:
                res_lab['text'] = int(res)
            else:
                res_lab['text'] = res
        elif "*" in s:
            res = num1 * num2
            if res % 1 == 0:
                res_lab['text'] = int(res)
            else:
                res_lab['text'] = res
        elif "/" in s:
            if num2 == 0:
                res_lab['text']='ERROR'
            else:
                res = num1/num2
                if res%1 == 0:
                    res_lab['text'] = int(res)
                else:
                    res_lab['text'] = res


    else:
        res_lab['text'] = 'not enough input'


def clear():
    entry.delete(0, END)


entry = Entry(root, width=20, font=('', 20))
entry.place(x=51, y=50)

btn1 = Button(text="1", command=lambda: input('1'))
btn1.place(x=60, y=100, height=60, width=60)

btn2 = Button(text="2", command=lambda: input('2'))
btn2.place(x=125, y=100, height=60, width=60)

btn3 = Button(text="3", command=lambda: input('3'))
btn3.place(x=190, y=100, height=60, width=60)

plus_btn = Button(text="+", command=lambda: input('+'))
plus_btn.place(x= 255, y=100, height=60, width=60)

btn4 = Button(text="4", command=lambda: input('4'))
btn4.place(x=60, y=165, height=60, width=60)

btn5 = Button(text="5", command=lambda: input('5'))
btn5.place(x=125, y=165, height=60, width=60)

btn6 = Button(text="6", command=lambda: input('6'))
btn6.place(x=190, y=165, height=60, width=60)

minus_btn = Button(text="-", command=lambda: input('-'))
minus_btn.place(x=255, y=165, height=60, width=60)

btn7 = Button(text="7", command=lambda: input('7'))
btn7.place(x=60, y=230, height=60, width=60)

btn8 = Button(text="8", command=lambda: input('8'))
btn8.place(x=125, y=230, height=60, width=60)

btn9 = Button(text="9", command=lambda: input('9'))
btn9.place(x=190, y=230, height=60, width=60)

multiply_btn = Button(text="*", command=lambda: input('*'))
multiply_btn.place(x=255, y=230, height=60, width=60)

div_btn = Button(text="div", command=lambda: input('//'))
div_btn.place(x=60, y=295, height=60, width=60)

btn0 = Button(text="0", command=lambda: input('0'))
btn0.place(x=125, y=295, height=60, width=60)

mod_btn = Button(text="mod", command=lambda: input('%'))
mod_btn.place(x=190, y=295, height=60, width=60)

divide_btn = Button(text="/", command=lambda: input('/'))
divide_btn.place(x=255, y=295, height=60, width=60)

delete_btn = Button(text="<-", command=delete)
delete_btn.place(x=60, y=360, height=60, width=60)

res_btn = Button(text="=", command=evaluate)
res_btn.place(x=125, y=360, height=60, width=60)

clear_btn = Button(text="C", command=clear)
clear_btn.place(x=190, y=360, height=60, width=60)

point_btn = Button(text=".", command=lambda: input('.'))
point_btn.place(x=255, y=360, height=60, width=60)

res_lab = Label(root, text="res", font=('', 20), justify="center")
res_lab.place(x=60, y=430)

root.mainloop()
