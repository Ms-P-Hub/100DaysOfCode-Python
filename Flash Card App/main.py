from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

data = pd.read_csv("./Flash Card App/data/zulu_words.csv")
to_learn = data.to_dict(orient="records")


def word_generate():
    row_chosen = random.choice(to_learn)
    canvas.itemconfig(language_canvas, text="Zulu")
    canvas.itemconfig(word_canvas, text=row_chosen["zulu"])
    
    
window = Tk()
window.title("Flash Card App")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)


canvas = Canvas(
    width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0
)
photo = PhotoImage(file="./Flash Card App/images/card_front.png")
canvas.create_image(400, 263, image=photo)
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
