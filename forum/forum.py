from tkinter import *
from PIL import Image, ImageTk


class User():

    # ban - boolean
    def __init__(self, username, password, followers, ban):
        self.username = username
        self.password = password
        self.followers = followers
        self.ban = ban

    def __str__(self):
        return f'username:{self.username}\npassword:{self.password}\nfollowers:{self.followers}\nbanned:{self.ban}'


# user1 = User("bear_killer", "qwerty123", 1259, False)
# print(user1)

root = Tk()
root.title("forum")
root.geometry("500x500")


def clear_screen():
    for widget in root.winfo_children():
        widget.destroy()




def login_page():
    clear_screen()

    login_lab = Label(root, text="Login", font=('', 20))
    login_lab.place(x=225, y=100)

    username_entry = Entry(root, width=20, font=('', 20))
    # nickname_entry.insert(0, "nickname")
    # nickname_entry['fg'] = 'grey'
    # nickname_entry.place(x=120, y=150)
    # nickname_entry.insert(0, 'username')
    # nickname_entry.bind('<FocusIn>', on_entry_click)
    # nickname_entry.bind('<FocusOut>', on_focusout)
    # nickname_entry['fg'] = 'grey'
    username_entry.place(x=120, y=150)

    password_entry = Entry(root, width=20, font=('', 20))
    # password_entry.insert(0, 'password')
    # password_entry.bind('<FocusIn>', on_entry_click)
    # password_entry.bind('<FocusOut>', on_focusout)
    # password_entry['fg'] = 'grey'
    password_entry.place(x=120, y=190)

    login_btn = Button(root, text="Login", command=lambda:login(username_entry, password_entry))
    login_btn.place(x=220, y=250)

    signup_teleport_btn = Button(root, text="signup", command=signup_page)
    signup_teleport_btn.place(x=220, y=400)


def login(username_entry, password_entry):
    try:
        with open('users.txt', 'r') as f:
            found_user = None
            for line in f:
                # Check if the line contains the username
                if f"nickname:{username_entry.get()}" in line:
                    found_user = line.strip()  # Store the found user line
                    break  # Exit the loop once the user is found
            if found_user:
                print("User found:")
                print(found_user)
            else:
                print("User not found")
    except FileNotFoundError:
        print("The file 'users.txt' does not exist.")


def signup_page():
    clear_screen()

    signup_lab = Label(root, text="Sign up", font=('', 20))
    signup_lab.place(x=225, y=100)

    su_username_entry = Entry(root, width=20, font=('', 20))
    # nickname_entry.insert(0, 'username')
    # nickname_entry.bind('<FocusIn>', on_entry_click)
    # nickname_entry.bind('<FocusOut>', on_focusout)
    # nickname_entry['fg'] = 'grey'
    su_username_entry.place(x=120, y=150)

    su_password_entry = Entry(root, width=20, font=('', 20))
    # password_entry.insert(0, 'password')
    # password_entry.bind('<FocusIn>', on_entry_click)
    # password_entry.bind('<FocusOut>', on_focusout)
    # password_entry['fg'] = 'grey'
    su_password_entry.place(x=120, y=190)

    su_second_password_entry = Entry(root, width=20, font=('', 20))
    # password_entry.insert(0, 'new password')
    # password_entry.bind('<FocusIn>', on_entry_click)
    # password_entry.bind('<FocusOut>', on_focusout)
    # password_entry['fg'] = 'grey'
    su_second_password_entry.place(x=120, y=230)

    signup_btn = Button(root, text="signup", command=lambda: signup(su_username_entry, su_password_entry, su_second_password_entry))
    signup_btn.place(x=220, y=400)

    # def on_entry_click(event):
    #     """function that gets called whenever entry is clicked"""
    #     if nickname_entry.get() == 'username':
    #         nickname_entry.delete(0, "end")
    #         nickname_entry.insert(0, '')
    #         nickname_entry['fg'] = 'white'
    #     if password_entry.get() == 'password':
    #         password_entry.delete(0, "end")
    #         password_entry.insert(0, '')
    #         password_entry['fg'] = 'white'
    #
    # def on_focusout(event):
    #     if nickname_entry.get() == '':
    #         nickname_entry.insert(0, 'username')
    #         nickname_entry['fg'] = 'grey'
    #     if password_entry.get() == '':
    #         password_entry.insert(0, 'username')
    #         password_entry['fg'] = 'grey'


def signup(su_username_entry, su_password_entry, su_second_password_entry):
    if su_password_entry.get() == su_second_password_entry.get():
        user = User(su_username_entry.get(), su_password_entry.get(), 0, False)
        print(user)
        with open('users.txt', 'a') as f:
            f.write(str(user) + '\n\n')
    else:
        print("ERROR MF")


login_page()


root.mainloop()
