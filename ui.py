from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain  # QuizBrain object
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.q_canvas = self.canvas.create_text(150, 125, width=280,
                                                text="Some", font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_button_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_image, highlightthickness=0,
                                   command=self.false_clicked)
        self.false_button.grid(row=2, column=0)

        right_button_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_button_image, highlightthickness=0,
                                   command=self.true_clicked)
        self.right_button.grid(row=2, column=1)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, font=('Ariel', 20, "normal"), fg="white")
        self.score.grid(row=0, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.q_canvas, text=self.quiz.next_question())
        else:
            self.right_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)
            self.canvas.itemconfig(self.q_canvas, text="You've reached the end of the quiz.")

    def true_clicked(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_clicked(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, response):
        if response:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, func=self.get_next_question)
