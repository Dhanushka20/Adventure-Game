import tkinter as tk
from tkinter import messagebox

def start_adventure():
    name = name_entry.get()
    messagebox.showinfo("Welcome", f"Welcome {name} to this adventure!")
    show_question1()

def show_question1():
    question_label.config(text="You are on a dirt road. Do you go left or right?")
    left_button.config(text="Left", command=choose_left)
    right_button.config(text="Right", command=choose_right)

def choose_left():
    question_label.config(text="You have to cross a river. Do you swim or walk?")
    left_button.config(text="Swim", command=choose_swim)
    right_button.config(text="Walk", command=choose_walk)

def choose_swim():
    messagebox.showinfo("Result", "An alligator caught you. You lose!")

def choose_walk():
    messagebox.showinfo("Result", "You walked for many miles. You lose!")

def choose_right():
    question_label.config(text="You come to a bridge. Do you cross the bridge or go back?")
    left_button.config(text="Cross", command=choose_cross)
    right_button.config(text="Back", command=choose_back)

def choose_cross():
    question_label.config(text="You meet a stranger. Do you talk or fight?")
    left_button.config(text="Talk", command=choose_talk)
    right_button.config(text="Fight", command=choose_fight)

def choose_talk():
    messagebox.showinfo("Result", "The stranger gives you gold. You win!")

def choose_fight():
    messagebox.showinfo("Result", "The stranger takes your money. You lose!")

def choose_back():
    messagebox.showinfo("Result", "You lose!")

# Main window
root = tk.Tk()
root.title("Adventure Game")

# Name entry
name_label = tk.Label(root, text="Type your name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Start button
start_button = tk.Button(root, text="Start Adventure", command=start_adventure)
start_button.pack()

# Question label
question_label = tk.Label(root, text="")
question_label.pack()

# Left and Right buttons
left_button = tk.Button(root, text="")
left_button.pack(side=tk.LEFT, padx=10)
right_button = tk.Button(root, text="")
right_button.pack(side=tk.RIGHT, padx=10)

root.mainloop()
