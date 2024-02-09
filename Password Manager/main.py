from tkinter import *
from tkinter import messagebox


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Invalid Input", message="Do not leave any fields empty!"
        )
    else:
        is_correct = messagebox.askokcancel(
            title=f"{website.title()} Credentials",
            message=f"Username: {email}\nPassword: {password}\nClick 'ok' if this information in correct.",
        )

        if is_correct:
            with open("./Password Manager/.credentials.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="./Password Manager/logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=0, row=0, columnspan=3)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.focus()
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=19)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
