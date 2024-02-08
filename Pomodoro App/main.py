from tkinter import *
import time
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
# ------------------------------------------------------#
def start_timer():
    count_down(WORK_MIN*60)
    
def count_down(count):
    
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    
    canvas.itemconfig(time_text,text=f"{count_min}:{count_sec}")
    if count > 0 : window.after(1000,count_down,count-1)
    
# ------------------------------------------------------#
window = Tk()
window.title("Pomorodo Clock")
window.configure(padx=100, pady=50, bg=YELLOW)

picture = PhotoImage(file="./Pomodoro App/tomato.png")

timer_label = Label(fg=GREEN, text="TIMER", bg=YELLOW, font=(FONT_NAME, 48, "bold"))
timer_label.grid(column=1, row=0)

tick_label = Label(fg=GREEN, text="✔️", bg=YELLOW, font=(FONT_NAME, 20, "normal"))
tick_label.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 110, image=picture)
time_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

canvas.grid(column=1, row=1)

start_button = Button(text="Start", bg=YELLOW, activebackground=GREEN,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", bg=YELLOW, activebackground=GREEN)
reset_button.grid(column=2, row=2)

window.mainloop()
