# Password Manager
import string
from tkinter import *
from random import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    caps_letters = list(string.ascii_uppercase)
    lower_letters = list(string.ascii_lowercase)
    numbers = [n for n in range(0, 10)]
    punctuations = list(string.punctuation)
    characters = []
    characters.extend(caps_letters)
    characters.extend(lower_letters)
    characters.extend(numbers)
    characters.extend(punctuations)
    password_list = []
    running_count = 0
    for _ in range(18):
        password_list.append(str(choice(characters)))
    password_str = "".join(password_list)
    text3_password.delete(0, END)
    text3_password.insert(END, string=password_str)
    print(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    with open("Passwords.txt", "a") as file:
        website_to_save = text1_Website.get()
        email_to_save = text2_Email.get()
        password_to_save = text3_password.get()
        file.write(f"{website_to_save} | {email_to_save} | {password_to_save}\n")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.geometry("500x500")
window.title("Pomodoro")
window.config(bg="white",
              padx=5,
              pady=50)

canvas = Canvas(width=200,
                height=190,
                bg="white",
                highlightthickness=0)

logo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(column=1, row=0)

label1_website = Label(text="Website:",
                       bg="white",
                       fg="black",
                       font=("Courier", 20))
label1_website.grid(column=0, row=1)

label2_Email = Label(text="Email/User:",
                     bg="white",
                     fg="black",
                     font=("Courier", 20),
                     )
label2_Email.grid(column=0, row=2)

label3_Password = Label(text="Password:",
                        bg="white",
                        fg="black",
                        font=("Courier", 20,))
label3_Password.grid(column=0, row=3)

text1_Website = Entry(width=30,
                      bg="white",
                      fg="black",
                      highlightthickness=0,
                      insertbackground="black",
                      )
text1_Website.grid(column=1, row=1)
text1_Website.focus_set()

text2_Email = Entry(width=30,
                    bg="white",
                    fg="black",
                    highlightthickness=0,
                    insertbackground="black",
                    )
text2_Email.grid(column=1, row=2)
text2_Email.focus_set()

text3_password = Entry(width=30,
                       bg="white",
                       fg="black",
                       highlightthickness=0,
                       insertbackground="black")
text3_password.grid(column=1, row=3)
text3_password.focus_set()

button1_generate = Button(width=20,
                          text="Generate Password",
                          bg="white",
                          fg="black",
                          highlightthickness=0,
                          highlightcolor="white",
                          highlightbackground="white",
                          command=generate)
button1_generate.grid(column=1, row=4)

button2_add = Button(width=20,
                     text="Add",
                     bg="white",
                     fg="black",
                     highlightthickness=0,
                     highlightcolor="white",
                     highlightbackground="white",
                     command=add)

button2_add.grid(column=1, row=5)

window.mainloop()