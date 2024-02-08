from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

rep = 0
timer = None


def reset():
    global rep
    global timer

    window.after_cancel(timer)
    timer_label.config(fg=GREEN, text="TIMER")
    canvas.itemconfig(time_text, text="00:00")
    tick_label.config()
    rep = 0


def start_timer():
    global rep

    rep += 1

    if rep == 8:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(fg=RED, text="LONG BREAK")
    elif rep % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(fg=PINK, text="BREAK")
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(fg=GREEN, text="WORK")


def count_down(count):
    global timer

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(rep / 2)):
            mark += "✔️"
            tick_label.config(fg=GREEN, text=mark)


window = Tk()
window.title("Pomorodo Clock")
window.configure(padx=100, pady=50, bg=YELLOW)

picture = PhotoImage(file="./Pomodoro App/tomato.png")

timer_label = Label(fg=GREEN, text="TIMER", bg=YELLOW, font=(FONT_NAME, 48, "bold"))
timer_label.grid(column=1, row=0)

tick_label = Label(fg=GREEN, text="", bg=YELLOW, font=(FONT_NAME, 20, "normal"))
tick_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110, image=picture)
time_text = canvas.create_text(
    100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)

start_button = Button(
    text="Start", bg=YELLOW, activebackground=GREEN, command=start_timer
)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, activebackground=GREEN, command=reset)
reset_button.grid(column=2, row=2)

window.mainloop()