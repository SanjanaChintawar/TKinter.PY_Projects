from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    checkmark_label.config(text=" ")
    title_label.config(text="Timer", fg=GREEN)
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Break", fg=PINK)
    elif reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Break", fg=RED)
    else:
        count_down(WORK_MIN * 60)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    global reps
    minutes = math.floor(count / 60)
    sec = math.floor(count % 60)
    if sec < 10:
        sec = f"0{sec}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = " "
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        checkmark_label.config(text=mark, font=(FONT_NAME, 35, "normal"))


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

checkmark_label = Label(fg=GREEN, bg=YELLOW)
checkmark_label.grid(column=1, row=3)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
