from pyperclip import *
from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def search():
    website = website_input.get()
    try:
        with open("./Password Manager/.credentials.json", "r") as file:
            credential_dict = json.load(file)

        messagebox.showinfo(
            title=f"Searching for {website}",
            message=f"Username/Email: {credential_dict[website]['username']}\nPassword: {credential_dict[website]['password']}",
        )
    except:
        messagebox.showinfo(
            title=f"Searching for {website}", message=f"{website} doesn't exist"
        )


def generate_password():
    password_input.delete(first=0, last=END)

    l_sequence = [choice(letters) for i in range(randint(0, 6))]
    n_sequence = [choice(numbers) for i in range(randint(0, 4))]
    s_sequence = [choice(symbols) for i in range(randint(0, 2))]

    password = l_sequence + n_sequence + s_sequence

    shuffle(password)
    password_input.insert(0, "".join(password))
    copy("".join(password))


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    credentials = {website: {"email": email, "password": password}}

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
            try:
                with open("./Password Manager/.credentials.json", "r") as file:
                    data = json.load(file)
                    data.update(credentials)

                with open("./Password Manager/.credentials.json", "w") as file:
                    json.dump(data,file, indent=2)
            except:
                with open("./Password Manager/.credentials.json", "w") as file:
                    json.dump(credentials,file, indent=2)

            website_input.delete(first=0, last=END)
            email_input.delete(first=0, last=END)
            password_input.delete(first=0, last=END)
            messagebox.showinfo(
                title="Successful!", message="Credentials successfully saved!"
            )

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

website_input = Entry(width=19)
website_input.focus()
website_input.grid(column=1, row=1)

email_input = Entry(width=38)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=19)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
