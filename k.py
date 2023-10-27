import tkinter as tk
from tkinter import messagebox
import random

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.title("Clean Interface")
root.geometry(f"{screen_width}x{screen_height-30}")  # Set the window size

# List of possible button labels
button_labels = [
    'yes', 'yeah', 'yah', 'yup', 'yeppers', 'no', 'nah', 'nope', 'nay', 'not at all', 'why', 'what', 'huh', 'maybe', 'possibly', 'sometimes', 'hah', 'absurd', 'stipud', 'stupid', 'mo', 'stop',
    'agree', 'disagree', 'ok', 'alright', 'sure', 'never', 'always', 'perhaps', 'certainly', 'probably', 'doubtful', 'definitely', 'indeed', 'no way', 'for sure', 'not really', 'no doubt', 'of course',
    'absolutely', 'not a chance', 'positive', 'negative', 'neutral', 'affirmative', 'uncertain', 'correct', 'incorrect', 'right', 'wrong', 'valid', 'invalid', 'truth', 'lie', 'faith', 'distrust',
    'certainty', 'uncertainty', 'validity', 'fallacy', 'fact', 'fiction', 'honest', 'dishonest', 'clear', 'blurry', 'visible', 'invisible', 'accurate', 'inaccurate', 'righteous', 'sinful',
    'heaven', 'hell', 'moral', 'amoral', 'ethical', 'unethical', 'principled', 'unprincipled', 'legal', 'illegal', 'ethical', 'unethical', 'obvious', 'ambiguous', 'explicit', 'implicit', 'known',
    'unknown', 'reasonable', 'unreasonable', 'logical', 'illogical', 'rational', 'irrational', 'sensible', 'nonsensical', 'reasonable', 'unreasonable', 'wise', 'foolish', 'sane', 'insane', 'smart',
    'dumb', 'intelligent', 'educated', 'uneducated', 'sophisticated', 'unsophisticated', 'polite', 'impolite', 'generous', 'stingy', 'kind', 'unkind', 'helpful', 'unhelpful', 'happy', 'sad',
]
# Create a function to display a message when a button is clicked
def button_click(label):
    messagebox.showinfo(f"{label}", f"{label}")
tk.Label(root, text="Do you want to continue?").pack()
# Create and place a large number of buttons with random labels
for i in range(2000):
    x_pos = random.randint(0, screen_width-50)  # Random X position (within the window width)
    y_pos = random.randint(3, screen_height-60)  # Random Y position (within the window height)
    label = random.choice(button_labels)
    
    button = tk.Button(root, text=label, command=lambda l=label: button_click(l))
    button.place(x=x_pos, y=y_pos)

root.mainloop()
