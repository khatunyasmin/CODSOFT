#!/usr/bin/env python
# coding: utf-8

# In[55]:


import tkinter as tk
from tkinter import ttk, messagebox

class QuizGame:
    def __init__(self, master):
        self.master = master
        self.score = 0
        self.current_question = 0
# Add a heading label
        self.heading_label = ttk.Label(master, text="Quiz App", font=("italic", 18, "bold"), background="blue", foreground="#d90429")
        self.heading_label.pack(pady=(20, 10))
        self.questions = [
            {
                "question": "What is the largest animal in the world?",
                "options": ["Elephant", "Giraffe","Blue Whale"," Gorilla"],
                "answer": "Blue Whale",
                "description": "The largest animal in the world is Blue Whale."
            },
            {
                "question": "Who wrote the play Romeo and Juliet?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
                "answer": "William Shakespeare",
                "description": "William Shakespeare is the playwright Romeo and Juliet."
            },
            {
                "question": "What is the capital of Japan?",
                "options": ["Tokyo", "Beijing", "Seoul", "Bangkok"],
                "answer": "Tokyo",
                "description": "The capital of Japan is Tokyo"
            },
            {
                "question": " What is the chemical symbol for the element gold?",
                "options": ["Go", "Ag", "Ge", " Au"],
                "answer": "Au",
                "description": "The chemical symbol for the element gold is Au"
            },
            {
                "question": "Who was the first Prime Minister of India?",
                "options": [" Mahatma Gandhi", "Jawaharlal Nehru", "Sardar Vallabhbhai Patel", " Subhas Chandra Bose"],
                "answer": "Jawaharlal Nehru",
                "description": "Jawaharlal Nehru was the first Prime Minister of India"
            },
            # Add more questions here
        ]
        
        self.master.configure(bg="blue") #blue
        self.master.title("Quiz Game Start")# Heading name
        self.master.geometry("500x400")# size of the box
        

        self.question_label = ttk.Label(master, text="Q.", font=("Arial", 12, "bold"), wraplength=500, foreground="#072ac8", background="#edf2f4")
        self.question_label.pack(pady=(60, 10))

        self.option_buttons = []
        for i in range(4):
            button = ttk.Button(master, text="", command=lambda i=i: self.check_answer(i), style='TButton')
            button.pack(pady=5, padx=8, ipadx=8, ipady=5, fill=tk.X)
            self.option_buttons.append(button)
    
        
        self.next_question()
        
        self.style = ttk.Style()
        self.style.configure('TButton', background='#ef476f', foreground='#5a0001')  # Set button colors

    def next_question(self):
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["question"])
            options = self.questions[self.current_question]["options"]
            for i in range(4):
                self.option_buttons[i].config(text=options[i])
            self.current_question += 1
        else:
            self.show_score()
            
    def enable_next(self):
        self.next_button.config(state=tk.NORMAL)
    
    def check_answer(self, selected_option):
        selected_answer = self.questions[self.current_question - 1]["options"][selected_option]
        correct_answer = self.questions[self.current_question - 1]["answer"]
        
        if selected_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Correct!", "You got it right!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is: {correct_answer}")
        
        self.next_question()

    def show_score(self):
        total_questions = len(self.questions)
        message = f"You got {self.score} out of {total_questions} questions correct.\n\n"

        custom_message_box = tk.Toplevel(self.master)
        custom_message_box.geometry("400x400")
        custom_message_box.title("Quiz Finished")
       # custom_message_box.configure(bg="#ba0473")background color
        ttk.Label(custom_message_box, text=message, font=("Arial", 12)).pack(pady=10, padx=10)
        
        for question in self.questions:
            ttk.Label(custom_message_box, text=f"Q: {question['question']} \nA: {question['answer']}", font=("Arial", 10), justify="left").pack(pady=5, padx=5,anchor="w")
        if self.score == total_questions:
            ttk.Label(custom_message_box, text="Congratulations! You got all the questions correct. Great job!", font=("Arial", 10, "bold"), foreground="#ff7900",justify="left").pack(pady=10, anchor="w")
        elif self.score >= total_questions // 2:
            ttk.Label(custom_message_box, text="Good job! You passed the quiz.", font=("Arial", 10, "bold"), foreground="#d90429",justify="left").pack(pady=10, anchor="w")
        else:
            ttk.Label(custom_message_box, text="You need more practice. Keep trying!", font=("Arial", 10, "bold"), foreground="#d90429",justify="left").pack(pady=10, anchor="w")
            
        ttk.Button(custom_message_box, text="OK", command=custom_message_box.destroy).pack(pady=9, padx=9)
        custom_message_box.transient(self.master)  # Set the message box to be dependent on the main window
        custom_message_box.grab_set()  
        
if __name__ == "__main__":
    root = tk.Tk()
    game = QuizGame(root)
    root.mainloop()


# In[ ]:





# In[ ]:




