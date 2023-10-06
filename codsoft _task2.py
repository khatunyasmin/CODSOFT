#!/usr/bin/env python
# coding: utf-8

# In[23]:


import tkinter as tk
from tkinter import font

def click(event):
    text = event.widget.cget("text")
    current_text = screen.get()

    if text == "=":
        try:
            # Evaluate the expression and update the display
            result = str(eval(current_text))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        # Clear the screen
        screen.set("")
    else:
        # Append the clicked button's text to the screen
        if current_text == "0" and text != "0":
            screen.set(text)
        elif current_text != "0":
            screen.set(current_text + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")
root.configure(bg='#333333')  # Set background color

# Create a variable to store the expression
screen = tk.StringVar()
screen.set("0")

# Entry widget to display the expression
entry_font = font.Font(family='Helvetica', size=24)
entry = tk.Entry(root, textvar=screen, font=entry_font, justify='right', bd=10, insertwidth=4, width=10)
entry.pack(fill=tk.BOTH, ipadx=8, padx=10, pady=10, expand=True)

# Create a frame for the buttons
button_frame = tk.Frame(root, bg='#fca311')
button_frame.pack()

# Buttons
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+',
]

row, col = 0, 0
button_font = font.Font(family='Helvetica', size=18)
for text in button_texts:
    if text.isnumeric():
        button = tk.Button(button_frame, text=text, font=button_font, padx=20, pady=20, bd=5, bg='#555555', fg='#FFFFFF')
    else:
        button = tk.Button(button_frame, text=text, font=button_font, padx=20, pady=20, bd=5, bg='#555555', fg='#FF0000')
    button.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
    button.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure row and column weights for resizing
for i in range(4):
    button_frame.grid_rowconfigure(i, weight=1)
    button_frame.grid_columnconfigure(i, weight=1)

# Styling
entry.configure(bg='#222222', fg='#FFFFFF')  # Set entry background and text color
entry.configure(insertbackground='#FFFFFF')  # Set cursor color

# Start GUI
root.mainloop()


# In[ ]:




