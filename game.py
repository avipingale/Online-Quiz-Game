import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Online Quiz Game")

        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "Berlin", "London"], "correct": "Paris"},
            {"question": "What is the largest mammal?", "options": ["Elephant", "Blue Whale", "Giraffe"], "correct": "Blue Whale"},
            # Add more questions as needed
        ]

        self.current_question_index = 0
        self.score = 0

        self.label_question = tk.Label(root, text="")
        self.label_question.pack(pady=10)

        self.radio_var = tk.StringVar()
        self.radio_buttons = []
        for i in range(3):
            radio_button = tk.Radiobutton(root, text="", variable=self.radio_var, value="", command=self.check_answer)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        self.next_button = tk.Button(root, text="Next Question", command=self.next_question)
        self.next_button.pack(pady=10)

        self.update_question()

    def update_question(self):
        if self.current_question_index < len(self.questions):
            question_data = self.questions[self.current_question_index]
            self.label_question.config(text=question_data["question"])

            options = question_data["options"]
            random.shuffle(options)
            for i in range(3):
                self.radio_buttons[i].config(text=options[i], value=options[i])

            self.next_button.config(state=tk.DISABLED)
        else:
            self.show_score()

    def check_answer(self):
        selected_option = self.radio_var.get()
        correct_option = self.questions[self.current_question_index]["correct"]

        if selected_option == correct_option:
            self.score += 1

        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        self.update_question()

    def show_score(self):
        score_message = f"Your Score: {self.score}/{len(self.questions)}"
        messagebox.showinfo("Quiz Finished", score_message)
        self.root.destroy()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
