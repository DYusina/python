from tkinter import *
from tkinter import messagebox
import hashlib
import random
import string

root = Tk()
root.title("Password")
root.geometry("400x200")


def verify():
    salt = ''.join(random.choices(string.ascii_letters, k=3))
    if hashlib.sha256((first_try_entry.get() + salt).encode()).hexdigest() == hashlib.sha256(
            (second_try_entry.get() + salt).encode()).hexdigest():
        messagebox.showinfo("Correct password", "Correct")
    else:
        messagebox.showinfo("Wrong password", "Try again")
        first_try_entry.delete(0, END)
        second_try_entry.delete(0, END)


first_try_lab = Label(root, text="Password:", font=('', 20))
first_try_lab.pack()

first_try_entry = Entry(root, show="*", font=('', 20))
first_try_entry.pack()

second_try_lab = Label(root, text="Enter the same password:", font=('', 20))
second_try_lab.pack()

second_try_entry = Entry(root, show="*", font=('', 20))
second_try_entry.pack()

verification_btn = Button(text="verify", command=verify)
verification_btn.pack()

root.mainloop()
