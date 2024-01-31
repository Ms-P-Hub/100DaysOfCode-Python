from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=50, pady=50)

user = Entry(width=15)
user.config(width=10)
user.grid(column=1, row=0)

label_1 = Label(text="Miles", font=("Arial", 10, "normal"))
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to", font=("Arial", 10, "normal"))
label_2.grid(column=0, row=1)

label_3 = Label(text="0", font=("Arial", 10, "normal"))
label_3.config(width=10)
label_3.grid(column=1, row=1)

label_4 = Label(text="Km", font=("Arial", 10, "normal"))
label_4.grid(column=2, row=1)


def button_pressed():
    label_3.config(text=str(float(user.get()) * 1.689))


button = Button(text="Calculate", command=button_pressed)
button.grid(column=1, row=2)


window.mainloop()
