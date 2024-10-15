from tkinter import *
from tkinter import messagebox
import hashlib
import random
import string


def custom_hash(password):
    prime = 31
    hash_value = 0
    for char in password:
        hash_value = hash_value * prime + ord(char)
    return hash_value


def verify():
    salt = ''.join(random.choices(string.ascii_letters, k=3))
    password1 = first_try_entry.get()
    password2 = second_try_entry.get()

    sha_hash1 = hashlib.sha256((password1 + salt).encode()).hexdigest()
    sha_hash2 = hashlib.sha256((password2 + salt).encode()).hexdigest()

    custom_hash1 = custom_hash(password1)
    custom_hash2 = custom_hash(password2)

    if sha_hash1 == sha_hash2 and custom_hash1 == custom_hash2:
        messagebox.showinfo("Correct password", "Correct")
    else:
        messagebox.showinfo("Wrong password", "Try again")
        first_try_entry.delete(0, END)
        second_try_entry.delete(0, END)


def main():
    global first_try_entry, second_try_entry

    root = Tk()
    root.title("Password")
    root.geometry("400x200")

    first_try_lab = Label(root, text="Password:", font=('', 20))
    first_try_lab.pack()

    first_try_entry = Entry(root, show="*", font=('', 20))
    first_try_entry.pack()

    second_try_lab = Label(root, text="Enter the same password:", font=('', 20))
    second_try_lab.pack()

    second_try_entry = Entry(root, show="*", font=('', 20))
    second_try_entry.pack()

    verification_btn = Button(text="Verify", command=verify)
    verification_btn.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
