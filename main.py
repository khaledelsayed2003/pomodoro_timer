from tkinter import *
import time
import math
# ----CONSTANTS 
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# UI setup......
window = Tk()
window.title("Timer")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width= 200, height= 224, bg= YELLOW, highlightthickness=0) 
tomato_img = PhotoImage(file= "pomodoro_timer/tomato.png") # to read through a file to get hold of that image.
canvas.create_image(100, 112, image= tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# -------------------------------------------------------------------------------------------------------------
# Work - short break - long break sessions
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60 
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        title_label.config(text= "Break", fg= RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text= "Break", fg= PINK)
        count_down(short_break_sec)
    else:
        title_label.config(text= "Work")
        count_down(work_sec)
        
# Timer Mechanism......
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60 
    if int(count_sec) <= 9:
        count_sec = f"0{count_sec}"  # Apply Dynamic typing concept for sec..
    if int(count_min) <= 9:
        count_min = f"0{count_min}"  # Apply Dynamic typing concept for mins..
    canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1) # calls that fun after that amount of time in milliseconds.
    else:
        start_timer()
# -------------------------------------------------------------------------------------------------------------

start_button = Button(text="Start", width=8, font=(FONT_NAME, 15, "bold"), command= start_timer)
start_button.grid(column=0, row=2)

checkmark_label = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmark_label.grid(column=1, row=3)

reset_button = Button(text="Reset", width=8, font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2)























window.mainloop()
