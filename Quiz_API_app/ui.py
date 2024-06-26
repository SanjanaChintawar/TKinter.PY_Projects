import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#673F69"
TEXT_COLOR = "#FCE9F1"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = tk.Tk()
        self.window.title("Right or Wrong ?")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = tk.Label(text=f"Score: {self.score}", font=("Arial", 15), fg="white", bg=THEME_COLOR,
                                    highlightthickness=0)
        self.score_label.grid(row=0, column=1)

        self.canvas = tk.Canvas(width=500, height=250, bg=TEXT_COLOR)
        self.question_text = self.canvas.create_text(250,
                                                     135,
                                                     width=280,
                                                     text="question",
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_img = tk.PhotoImage(file="images/true.png")
        self.right_button = tk.Button(image=self.right_img,
                                      bg=THEME_COLOR,
                                      highlightthickness=0,
                                      command=self.true_pressed)
        self.right_button.grid(row=2, column=0)

        self.wrong_img = tk.PhotoImage(file="images/false.png")
        self.wrong_button = tk.Button(image=self.wrong_img,
                                      bg=THEME_COLOR,
                                      highlightthickness=0,
                                      command=self.false_pressed)
        self.wrong_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg=TEXT_COLOR)
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've Reached the end of quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            self.score_label.config(text=f"Final Score: {self.quiz.score}", font=("Arial", 20))

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)


