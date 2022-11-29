from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, 'italic')


class QuizInterface():
    
    def __init__(self, quiz: QuizBrain):
        
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # score 
        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(row=0, column=1)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        # question
        self.question = self.canvas.create_text(150, 125, text="Some question", font=FONT, fill=THEME_COLOR, width=280)
        
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # wrong and right buttons
        self.wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, border=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=0, padx=20, pady=20)

        self.right_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, border=0, command=self.correct)
        self.right_button.grid(row=2, column=1, padx=20, pady=20)
        
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):

        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
                    
            q_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_txt)

        else:
            self.canvas.itemconfig(self.question, text=f"You've reached the end of the quiz. Final Score: {self.quiz.score}")
            self.window.after(500, func=self.window.destroy)
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.give_feedback(is_right)
        
            

    def wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, func=self.get_next_question)

        
# ui = QuizInterface("MY name")