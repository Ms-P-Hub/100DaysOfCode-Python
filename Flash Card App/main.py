from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./Flash Card App/data/zulu_words.csv")
to_learn = data.to_dict(orient="records")
word_chosen = {}

def word_generate():
    global word_chosen, flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(background_image, image=front_photo)
    word_chosen = random.choice(to_learn)
    canvas.itemconfig(language_canvas, text="Zulu", fill="black")
    canvas.itemconfig(word_canvas, text=word_chosen["zulu"], fill="black")
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(language_canvas, text="English", fill="white")
    canvas.itemconfig(word_canvas, text=word_chosen["english"], fill="white")
    canvas.itemconfig(background_image, image=back_photo)


window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
back_photo = PhotoImage(file="./Flash Card App/images/card_back.png")
front_photo = PhotoImage(file="./Flash Card App/images/card_front.png")
background_image = canvas.create_image(400, 263, image=front_photo)
language_canvas = canvas.create_text(
    400, 150, font=("Ariel", 20, "italic"), text="title"
)
word_canvas = canvas.create_text(400, 263, font=("Ariel", 40, "bold"), text=f"word")
canvas.grid(column=0, row=0, columnspan=2)


correct_pic = PhotoImage(file="./Flash Card App/images/right.png")
correct_button = Button(image=correct_pic, highlightthickness=0, command=word_generate)
correct_button.grid(column=1, row=1)

incorrect_pic = PhotoImage(file="./Flash Card App/images/wrong.png")
incorrect_button = Button(
    image=incorrect_pic, highlightthickness=0, command=word_generate
)
incorrect_button.grid(column=0, row=1)

window.mainloop()
