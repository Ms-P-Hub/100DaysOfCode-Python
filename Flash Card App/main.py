from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
photo = PhotoImage(file="./Flash Card App/images/card_front.png")
canvas.create_image(400, 263, image=photo)
canvas.grid(column=0, row=0, columnspan=2)

correct_pic = PhotoImage(file="./Flash Card App/images/right.png")
correct_button = Button(image=correct_pic, highlightthickness=0)
correct_button.grid(column=1, row=1)

incorrect_pic = PhotoImage(file="./Flash Card App/images/wrong.png")
incorrect_button = Button(image=incorrect_pic, highlightthickness=0)
incorrect_button.grid(column=0, row=1)

window.mainloop()
