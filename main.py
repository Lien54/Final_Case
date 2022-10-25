import tkinter as tk
from tkinter import BOTTOM, TOP, PhotoImage, messagebox as mb


window = tk.Tk()
window.title("Login Page")

win_width = 500
win_height = 400
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("{}x{}+{}+{}".format(
    win_width,
    win_height,
    width//2 - (win_width//2),
    height//2 - (win_height//2))
)
window.resizable(height = None, width = None)
window.configure(bg='#669BBC')

def login():
    email = "python542@gmail.com"
    password = "2045"
    if entry_textemail.get()==email and entry_password.get()==password:
        mb.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        mb.showerror(title="Error", message="Your email or password is incorrect.")


page_1 = tk.Frame(bg='#669BBC')
page_2 = tk.Frame(bg='#669BBC')

for frame in (page_1, page_2):
    frame.grid(row=0, column=0, sticky='nsew')

def show_frame(frame):
    frame.tkraise()

show_frame(page_1)

    #!==== Creating page login ====!#
lbl_login = tk.Label(
    page_1, text="Login",
    bg='#669BBC', fg="white",
    font=("Courier", 28, "bold")
)
lbl_login.grid(row = 0, column = 0, columnspan = 3, sticky = "news", pady = 20)

lbl_textemail = tk.Label(
    page_1, text="Email",
    bg='#669BBC', fg="#FFFFFF",
    font=("Courier", 14)
)
lbl_textemail.grid(row = 1, column = 0)
entry_textemail = tk.Entry(page_1, font=("Courier", 16))
entry_textemail.grid(row = 1, column = 1, pady = 20)

lbl_password = tk.Label(
    page_1, text="Password",
    bg='#669BBC', fg="#FFFFFF",
    font=("Courier", 14)
)
lbl_password.grid(row = 2, column = 0)
entry_password = tk.Entry(page_1, show="*", font=("Courier", 16))
entry_password.grid(row = 2, column = 1, pady = 20)

def enter(event):
    print("Enter")

btn_login = tk.Button(
    page_1, text = "Login",
    bg = "#F3A712", fg = "Black",
    font=("Courier", 16, "bold"), command=lambda: show_frame(page_2))
btn_login.grid(row = 3, column = 0, columnspan = 2, pady = 30)

window.bind('<Return>', enter)

    #!==== Creating page Quiz ====!#

page_2.config(background="#669BBC")

lbl_title = tk.Label(
    page_2, text = "QUIZ",
    bg='#669BBC', fg="#FFFFFF",
    font = ("Courier", 26, 'bold')
)
lbl_title.pack()

window.mainloop()